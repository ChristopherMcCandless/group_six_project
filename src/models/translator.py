from transformers import pipeline

class Translator:
    
    def ru_en(self, text: str):
        model = pipeline("translation", 'Helsinki-NLP/opus-mt-ru-en')
        return model(text)[0]['translation_text']
    
    def en_ru(self, text: str): 
        model = pipeline("translation", 'Helsinki-NLP/opus-mt-en-ru')
        return model(text)[0]['translation_text']
