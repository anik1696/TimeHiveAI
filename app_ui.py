# app_ui.py — CLEAN VERSION (Recent Queries removed)
# Gradio 6.x compatible — stable

import gradio as gr
from agent_graph import run_agent


CUSTOM_CSS = """
#main-card {
    max-width: 980px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 14px;
    background: #ffffff;
    box-shadow: 0 14px 40px rgba(2, 6, 23, 0.08);
}

/* Top bar */
.top-name {
    text-align:center;
    padding: 12px;
    border-radius: 10px;
    background: linear-gradient(90deg,#071028,#0f172a);
    color: #fff;
    font-weight: 800;
    font-size: 20px;
    margin-bottom: 14px;
}

/* big response box */
#response_md {
    border-radius: 14px;
    padding: 20px;
    background: linear-gradient(180deg,#071a2f,#0b1c2d);
    color: white;
    font-size: 15px;
    line-height: 1.5;
    min-height: 150px;
    box-shadow: 0 12px 28px rgba(0,0,0,0.25);
}

/* example buttons */
.example-btn {
    width: 100%;
    background: #5e646f;
    color: white;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 10px;
}
"""


def build_ui():
    with gr.Blocks() as demo:

        gr.HTML(f"<style>{CUSTOM_CSS}</style>")

        with gr.Column(elem_id="main-card"):

            gr.HTML("<div class='top-name'>⏱️ TimeHive — Time Zone Finder</div>")

            with gr.Row():
                # LEFT
                with gr.Column(scale=2):
                    city_input = gr.Textbox(label="City", placeholder="e.g., Dhaka, Tokyo, London")

                    get_btn = gr.Button("Get Time")
                    clear_btn = gr.Button("Clear")

                    response_md = gr.Markdown("**No result yet**", elem_id="response_md")

                # RIGHT (quick examples only)
                with gr.Column(scale=1):
                    gr.Markdown("**Quick examples**")
                    btn_dhaka = gr.Button("Dhaka", elem_classes="example-btn")
                    btn_tokyo = gr.Button("Tokyo", elem_classes="example-btn")
                    btn_london = gr.Button("London", elem_classes="example-btn")
                    btn_dubai = gr.Button("Dubai", elem_classes="example-btn")

            state = gr.State([])

            # Quick example buttons
            btn_dhaka.click(lambda: "Dhaka", None, city_input)
            btn_tokyo.click(lambda: "Tokyo", None, city_input)
            btn_london.click(lambda: "London", None, city_input)
            btn_dubai.click(lambda: "Dubai", None, city_input)

            # main execution
            def submit(city):
                city = (city or "").strip()

                if not city:
                    return "❗ Please enter a city name."

                result = run_agent(city)
                reply = result.get("reply", "No reply returned.")
                return reply

            get_btn.click(submit, city_input, response_md)
            city_input.submit(submit, city_input, response_md)

            clear_btn.click(lambda: "**No result yet**", None, response_md)

        return demo


if __name__ == "__main__":
    ui = build_ui()
    ui.launch(share=True)
