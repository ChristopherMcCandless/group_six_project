from models.punctuator import Punctuator
from models.summarizer import Summarizer

class TextSummaryService():
    
    def __init__(self):
        self.inited = False

    def setup(self):
        if self.inited == True: return
        self.inited = True
        self.punctuator = Punctuator()
        self.summarizer = Summarizer()
    
    def handle(self, text: str):        
        preparedText = self.punctuator.punctuate(text)
        summary = self.summarizer.summarize(text)
        return preparedText, summary

