import gradio as gr

def analyze_sentiment(text):
    if "good" in text:
        return "positive"
    elif "bad" in text:
        return "negative"
    else:
        return "neutral"

app = gr.Interface(fn=analyze_sentiment, inputs="text", outputs="label")

app.launch()
