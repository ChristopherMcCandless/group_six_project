from sbert_punc_case_ru import SbertPuncCase

class Punctuator:

    def setup(self):
        #TODO тож неуверен что эта модель подходит почекать еще
        self.model = SbertPuncCase()

    def punctuate(self, text: str):
        return self.model.punctuate(text)