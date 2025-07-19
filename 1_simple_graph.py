from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from IPython.display import Image, display

class PortfolioState(TypedDict):
    amount_usd: float
    total_usd: float
    total_inr: float

def calc_total(state: PortfolioState) -> PortfolioState:
    state['total_usd'] = state['amount_usd'] * 1.08
    return state

def convert_to_inr(state: PortfolioState) -> PortfolioState:
    state['total_inr'] = state['total_usd'] * 85
    return state

builder = StateGraph(PortfolioState)

builder.add_node("calc_total_node", calc_total)
builder.add_node("convert_to_inr_node", convert_to_inr)

builder.add_edge(START, "calc_total_node")
builder.add_edge("calc_total_node", "convert_to_inr_node")
builder.add_edge("convert_to_inr_node", END)

graph = builder.compile()

# display(Image(graph.get_graph().draw_mermaid_png()))

# graph.invoke({"amount_usd": 100000})

# Save the graph visualization as an image
graph_image = graph.get_graph().draw_mermaid_png()
with open("1_simple_graph.png", "wb") as f:
    f.write(graph_image)
print("Graph visualization saved as '1_simple_graph.png'")

# Run the graph with input and print results
result = graph.invoke({"amount_usd": 100000})
print(result)
print("\nResults:")
print(f"Initial USD: ${result['amount_usd']:,.2f}")
print(f"After 8% growth: ${result['total_usd']:,.2f}")
print(f"Converted to INR: ₹{result['total_inr']:,.2f}")