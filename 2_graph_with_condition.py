from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END
# from IPython.display import Image, display

class PortfolioState(TypedDict):
    amount_usd: float
    total_usd: float
    target_currency: Literal["INR", "EUR"]
    total: float

def calc_total(state: PortfolioState) -> PortfolioState:
    state['total_usd'] = state['amount_usd'] * 1.08
    return state

def convert_to_inr(state: PortfolioState) -> PortfolioState:
    state['total'] = state['total_usd'] * 85
    return state

def convert_to_eur(state: PortfolioState) -> PortfolioState:
    state['total'] = state['total_usd'] * 0.9
    return state

def choose_conversion(state: PortfolioState) -> str:
    return state["target_currency"]

builder = StateGraph(PortfolioState)

builder.add_node("calc_total_node", calc_total)
builder.add_node("convert_to_inr_node", convert_to_inr)
builder.add_node("convert_to_eur_node", convert_to_eur)

builder.add_edge(START, "calc_total_node")
builder.add_conditional_edges("calc_total_node", choose_conversion, {
    "INR": "convert_to_inr_node",
    "EUR": "convert_to_eur_node",
})
builder.add_edge("convert_to_inr_node", END)
builder.add_edge("convert_to_eur_node", END)

graph = builder.compile()

# display(Image(graph.get_graph().draw_mermaid_png()))

# graph.invoke({"amount_usd": 100000})

# Save the graph visualization as an image
graph_image = graph.get_graph().draw_mermaid_png()
with open("2_graph_with_condition.png", "wb") as f:
    f.write(graph_image)
print("Graph visualization saved as '2_graph_with_condition.png'")

# Run the graph with input and print results
result = graph.invoke({"amount_usd": 1000, "target_currency": "INR"})
# result = graph.invoke({"amount_usd": 1000, "target_currency": "EUR"})
print(result)
print("\nResults:")
print(f"Initial USD: ${result['amount_usd']:,.2f}")
print(f"After 8% growth: ${result['total_usd']:,.2f}")
print(f"Converted to INR: ₹{result['total']:,.2f}")
# print(f"Converted to EUR: €{result['total']:,.2f}")
print(f"Target currency: {result['target_currency']}")
