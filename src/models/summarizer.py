from transformers import pipeline

class Summarizer:
       
    def summarize(self, text: str):
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        rslt = summarizer(text, do_sample=False)
        return rslt[0]['summary_text']