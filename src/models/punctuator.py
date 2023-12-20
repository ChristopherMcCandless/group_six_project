from sbert_punc_case_ru import SbertPuncCase

class Punctuator:
    """
    Модель для востановления транскрибированного текста
    На данный момент не используется
    Восстанавливает пунктуацию, регистр.
    """
    
    def __init__(self):
        self.model = SbertPuncCase()

    def punctuate(self, text: str):
        return self.model.punctuate(text)