# LangGraph Learning

This project demonstrates the use of LangGraph to create and visualize workflow graphs. It includes two examples that show different aspects of building and executing graphs with LangGraph.

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
- `.gitignore`: Git ignore file for Python projects

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