from src.models.punctuator import Punctuator
from src.models.summarizer import Summarizer

class TextSummaryService():
    
    def __init__(self):
        self.inited = False

    def setup(self):
        if self.inited == True:
            return
        
        self.inited = True
        self.punctuator = Punctuator()
        self.punctuator.setup()
        self.summarizer = Summarizer()
        self.summarizer.setup()
    
    def handle(self, text: str):
        blocks = list(filter(lambda x : x != '', text.split('\n\n')))
        preparedBlocks = list()
        for block in blocks:
            preparedBlock = self.punctuator.punctuate(block)
            preparedBlocks.append(preparedBlock)
        
        summary = self.summarizer.summarize(preparedBlocks)
        return preparedBlocks, summary

