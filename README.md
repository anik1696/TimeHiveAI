# TimeHive AI

An agentic AI application that retrieves the current local time for any city in the world. Built using LangGraph to construct a multi-step pipeline and Gradio for the web interface.

---

## Overview

You type a city name, and the agent runs through a pipeline — parsing the input, geocoding the location, fetching the timezone, and formatting the result. The whole thing runs as a LangGraph graph with distinct nodes for each step.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-000000?style=for-the-badge&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-FF7C00?style=for-the-badge&logo=python&logoColor=white)

---

## Features

- Takes any city name as input
- Multi-node agentic pipeline: `parse → geocode → timezone → format`
- Returns current local time with timezone info
- Quick-example buttons for common cities (Dhaka, Tokyo, London, Dubai)
- Clean Gradio-based web UI

---

## Dependencies

| Package | Purpose |
|---|---|
| `gradio` | Web UI |
| `langgraph` | Agentic pipeline / graph execution |
| `requests` | HTTP calls for geocoding/timezone APIs |
| `tzfpy` | Timezone lookup from coordinates |

---

## Run Locally

**Requirements:** Python 3.9+

```bash
# Clone the repository
git clone https://github.com/anik1696/TimeHiveAI.git
cd TimeHiveAI

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
```

Gradio will launch the app and print a local URL (usually `http://127.0.0.1:7860`). If `share=True` is set, you also get a temporary public link.

---

## Repository

[github.com/anik1696/TimeHiveAI](https://github.com/anik1696/TimeHiveAI)