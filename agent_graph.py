# agent_graph.py
# Build and compile the LangGraph StateGraph and expose a simple runner function.

from langgraph.graph import StateGraph, END
from typing import Dict
from nodes import parse_node, geocode_node, timezone_node, format_node

def build_graph():
    """
    Construct a StateGraph with 4 nodes:
    - parse -> geocode -> timezone -> format
    Returns compiled app.
    """
    graph = StateGraph(dict)
    graph.add_node("parse", parse_node)
    graph.add_node("geocode", geocode_node)
    graph.add_node("timezone", timezone_node)
    graph.add_node("format", format_node)
    graph.set_entry_point("parse")
    graph.add_edge("parse", "geocode")
    graph.add_edge("geocode", "timezone")
    graph.add_edge("timezone", "format")
    graph.add_edge("format", END)
    return graph.compile()

# Compile at import time for fast runner
APP = build_graph()

def run_agent(query: str) -> Dict:
    """
    Run the compiled graph with the given query and return the final state dict.
    Example returned dict contains keys: reply, lat, lon, tz_name, ...
    """
    state = APP.invoke({"query": query})
    return state
