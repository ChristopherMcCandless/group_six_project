from sbert_punc_case_ru import SbertPuncCase

class Punctuator:
    
    def __init__(self):
        self.model = SbertPuncCase()

    def punctuate(self, text: str):
        return self.model.punctuate(text)