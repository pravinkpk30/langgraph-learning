# LangGraph Learning

This project demonstrates the use of LangGraph to create and visualize workflow graphs. It includes six examples that show different aspects of building and executing graphs with LangGraph.

## Prerequisites

- Python 3.8+
- [UV Package Manager](https://github.com/astral-sh/uv) (A fast Python package installer and resolver)

## Installation

1. **Install UV** (if not already installed):
   ```bash
   curl -sSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd langgraph-learning
   ```

3. **Create and activate a virtual environment** (recommended):
   ```bash
   uv init
   ```

4. **Install dependencies**:
   ```bash
   uv add <dependency-name list>
   ```

## Project Structure

- `1_simple_graph.py`: Basic example of a linear workflow graph
- `2_graph_with_condition.py`: Example with conditional branching
- `3_chatbot.py`: Interactive chatbot using LangGraph and a language model
- `4_tool_call.py`: Example of tool calling with LangGraph
- `5_tool_call_agent.py`: Advanced tool calling with agentic behavior
- `6_memory.py`: Multi-session memory and checkpointing example
- `7_langsmith_tracing.py`: LangSmith integration for monitoring and tracing  
- `.gitignore`: Git ignore file for Python projects
- `sample.env`: Example environment variables file

## Examples

### 1. Simple Linear Graph (`1_simple_graph.py`)

This example demonstrates a basic linear workflow that:
1. Takes a USD amount as input
2. Applies an 8% growth to the amount
3. Converts the resulting amount to INR (Indian Rupees)

**To run**:
```bash
uv run 1_simple_graph.py
```

**Output**:
- Saves a visualization of the graph as `1_simple_graph.png`
- Prints the calculation results to the console

### 2. Graph with Conditional Branching (`2_graph_with_condition.py`)

This example extends the first one by adding conditional branching to convert USD to either INR or EUR based on user input.

**To run**:
```bash
# For INR conversion
uv run 2_graph_with_condition.py

# For EUR conversion
# Uncomment the relevant line in the script and run again
```

**Output**:
- Saves a visualization of the graph as `2_graph_with_condition.png`
- Prints the calculation results to the console with the selected currency

### 3. Interactive Chatbot (`3_chatbot.py`)

This example demonstrates how to build an interactive chatbot using LangGraph with a language model (Google's Gemini). It features:

1. Conversation state management with message history
2. Integration with Google's Gemini model
3. Interactive command-line interface
4. Graph visualization of the conversation flow

**Prerequisites**:
- Set up your Google API key in a `.env` file (use `sample.env` as a template)
- Install required dependencies (see Installation section)

**To run**:
```bash
# First, create a .env file with your Google API key
cp sample.env .env
# Then edit .env and replace GOOGLE_API_KEY with your actual API key

# Run the chatbot
uv run 3_chatbot.py
```

**Usage**:
- Type your message and press Enter to chat with the bot
- Type `quit` or `exit` to end the session
- The conversation history is maintained throughout the session

**Output**:
- Saves a visualization of the conversation graph as `3_chatbot.png`
- Displays responses in an interactive chat interface

**Note**: Make sure to keep your API key secure and never commit it to version control.

### 4. Tool Calling with LangGraph (`4_tool_call.py`)

This example demonstrates how to integrate custom tools with LangGraph and a language model. It features:

1. Custom tool definition for stock price lookup
2. Dynamic tool calling based on user input
3. Conditional graph edges for tool execution
4. Interactive command-line interface

**Key Features**:
- Defines a custom `get_stock_price` tool that returns mock stock prices
- Uses `ToolNode` for handling tool execution
- Implements conditional edges for dynamic workflow routing
- Visualizes the tool-calling workflow

**To run**:
```bash
uv run 4_tool_call.py
```

**Usage**:
- Ask about stock prices using company symbols (e.g., "What is AAPL stock price?")
- The bot will respond with the current price if the company is in its database
- Type `quit` or `exit` to end the session

**Example Queries**:
```
What is the current price of MSFT?
I want to buy 20 AMZN stocks
What is the price of RIL?
```

**Note**: This example uses a mock implementation of stock prices. In a production environment, you would connect to a real financial API.

### 5. Advanced Tool Calling with Agent (`5_tool_call_agent.py`)

This example extends the basic tool calling with agentic behavior, allowing for more complex interactions and multi-step tool usage.

**Key Features**:
- Maintains conversation context across multiple interactions
- Handles multi-step tool usage in a single query
- Demonstrates agentic behavior with tool calling
- Visualizes the agent's decision-making process

**To run**:
```bash
uv run 5_tool_call_agent.py
```

**Example Queries**:
```
I want to buy 20 AMZN stocks using current price. Then 15 MSFT. What will be the total cost?
What's the current price of AAPL and MSFT combined?
```

### 6. Multi-session Memory and Checkpointing (`6_memory.py`)

This example demonstrates how to implement persistent memory and checkpointing in LangGraph, enabling multi-session conversations and state management.

**Key Features**:
- Uses `MemorySaver` for persistent conversation state
- Implements separate conversation threads with their own memory
- Demonstrates state persistence across multiple interactions
- Shows how to maintain context in complex workflows

**To run**:
```bash
uv run 6_memory.py
```

**Key Concepts**:
- **Checkpointing**: Saves the state of the conversation at specific points
- **Thread Management**: Maintains separate conversation threads with independent states
- **Context Persistence**: Remembers previous interactions within the same thread

**Example Use Case**:
```python
# First thread
config1 = {'configurable': {'thread_id': '1'}}
state = graph.invoke({"messages": [{"role": "user", "content": "What's the price of AAPL?"}]}, config=config1)

# Second thread (independent of the first)
config2 = {'configurable': {'thread_id': '2'}}
state = graph.invoke({"messages": [{"role": "user", "content": "What's the price of MSFT?"}]}, config=config2)
```

### 7. LangSmith Integration and Tracing ([7_langsmith_tracing.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langgraph-learning/7_langsmith_tracing.py:0:0-0:0))

This example demonstrates how to integrate LangSmith for monitoring, tracing, and debugging your LangGraph applications.

**Key Features**:
- Tracks and visualizes the execution flow of your LangGraph applications
- Records inputs, outputs, and intermediate steps for debugging
- Provides performance metrics and latency tracking
- Enables collaboration and sharing of traces with team members

**Prerequisites**:
1. Sign up for LangSmith at [https://smith.langchain.com](https://smith.langchain.com)
2. Get your API key from the LangSmith settings
3. Update the [.env](cci:7://file:///Users/praveenkumar/Desktop/Studies/langgraph-learning/sample.env:0:0-0:0) file with your LangSmith credentials (use [sample.env](cci:7://file:///Users/praveenkumar/Desktop/Studies/langgraph-learning/sample.env:0:0-0:0) as a template)

**To run**:
```bash
# First, update your .env file with LangSmith credentials
cp sample.env .env
# Edit .env and add your LangSmith API key and project details

# Install additional dependencies
uv add langsmith

# Run the example with tracing enabled
uv run 7_langsmith_tracing.py

## Understanding the Code

### Key Concepts

1. **State Management**:
   - Both examples use a `PortfolioState` TypedDict to manage the state throughout the graph execution
   - State is passed between nodes and modified by each processing step

2. **Graph Construction**:
   - `StateGraph` is used to define the workflow
   - Nodes are added with `add_node`
   - Edges define the flow between nodes
   - Conditional edges allow for branching logic

3. **Visualization**:
   - The graph is visualized using Mermaid.js through the `draw_mermaid_png()` method
   - Images are saved to disk for reference

## Dependencies

- `langgraph`: For building and executing the workflow graphs
- `typing_extensions`: For type hints (used by LangGraph)
- `IPython`: For displaying the graph (uncomment if using Jupyter notebooks)

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.