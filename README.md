# LangGraph Learning

This project demonstrates the use of LangGraph to create and visualize workflow graphs. It includes three examples that show different aspects of building and executing graphs with LangGraph.

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