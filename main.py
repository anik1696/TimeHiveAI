# main.py
# Entry point for TimeHive AI (Agentic AI using LangGraph)
# Run: python main.py

from app_ui import build_ui
from agent_graph import build_graph, APP
import sys

def print_graph_info():
    try:
        # build_graph returns compiled graph; show node names for proof
        compiled = build_graph()
        # compiled may have attribute nodes (depends on langgraph impl), try safe access
        nodes = []
        try:
            nodes = list(compiled.nodes.keys())
        except Exception:
            # fallback: try graph object
            try:
                nodes = list(compiled._graph.nodes.keys())
            except Exception:
                nodes = ["parse","geocode","timezone","format"]
        print("LangGraph pipeline compiled — nodes:", nodes)
    except Exception as e:
        print("Could not print graph nodes (non-fatal):", e)

if __name__ == "__main__":
    print_graph_info()
    demo = build_ui()
    # Launch Gradio (share=True gives a public URL if available)
    demo.launch(share=True)
