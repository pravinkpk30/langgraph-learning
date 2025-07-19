# 8_HITL.py (Human in the loop) intervention

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Import required libraries
from langchain.chat_models import init_chat_model
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command

# Define the state of our application
# Using TypedDict for type safety and better code completion
class State(TypedDict):
    # Messages will be automatically appended to the list using add_messages
    messages: Annotated[list, add_messages]

# Tool to get stock price
@tool
def get_stock_price(symbol: str) -> float:
    '''Return the current price of a stock given the stock symbol'''
    # Mock data for demonstration
    return {"MSFT": 200.3, "AAPL": 100.4, "AMZN": 150.0, "RIL": 87.6}.get(symbol, 0.0)

# Tool to buy stocks with human intervention
@tool
def buy_stocks(symbol: str, quantity: int, total_price: float) -> str:
    '''Buy stocks given the stock symbol and quantity'''
    # This will pause execution and wait for human input
    decision = interrupt(f"Approve buying {quantity} {symbol} stocks for ${total_price:.2f}?")
    
    # Process the human decision
    if decision == "yes":
        return f"You bought {quantity} shares of {symbol} for a total price of {total_price}"
    else:
        return "Buying declined."

# Initialize tools list with our defined tools
tools = [get_stock_price, buy_stocks]

# Initialize the language model
llm = init_chat_model("google_genai:gemini-2.0-flash")
# Bind our tools to the language model
llm_with_tools = llm.bind_tools(tools)

# Define the chatbot node that processes messages
def chatbot_node(state: State):
    # Generate a response using the language model
    msg = llm_with_tools.invoke(state["messages"])
    return {"messages": [msg]}

# Initialize memory for state management
memory = MemorySaver()

# Build the state graph
builder = StateGraph(State)

# Add nodes to the graph
builder.add_node("chatbot", chatbot_node)  # Chatbot processing node
builder.add_node("tools", ToolNode(tools))  # Tools execution node

# Define the graph edges
builder.add_edge(START, "chatbot")  # Start with chatbot
builder.add_conditional_edges("chatbot", tools_condition)  # Decide next step after chatbot
builder.add_edge("tools", "chatbot")  # After tools, go back to chatbot
builder.add_edge("chatbot", END)  # End after chatbot processing

# Compile the graph with memory
graph = builder.compile(checkpointer=memory)

graph_image = graph.get_graph().draw_mermaid_png()
with open("8_HITL.png", "wb") as f:
    f.write(graph_image)
print("Graph visualization saved as '8_HITL.png'")

# Configuration for our conversation thread
config = {"configurable": {"thread_id": "buy_thread"}}

# Example usage:

# Step 1: User asks for stock price
state = graph.invoke(
    {"messages":[{"role":"user","content":"What is the current price of 10 MSFT stocks?"}]}, 
    config=config
)
print(state["messages"][-1].content)

# Step 2: User attempts to buy stocks
state = graph.invoke(
    {"messages":[{"role":"user","content":"Buy 10 MSFT stocks at current price."}]}, 
    config=config
)
# This will trigger the interrupt in buy_stocks function
print(state.get("__interrupt__"))

# Get user decision
decision = input("Approve (yes/no): ")

# Resume execution with user's decision
state = graph.invoke(Command(resume=decision), config=config)
print(state["messages"][-1].content)