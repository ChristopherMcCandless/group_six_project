from transformers import pipeline
import time as time


class Translator:
    """
    Перевод текста
    ru-en
    en-ru
    """

    def ru_en(self, text: str):
        start = time.time()
        print(f'translator ru_en started')

        model = pipeline("translation", 'Helsinki-NLP/opus-mt-ru-en')
        rslt = model(text)[0]['translation_text']

        end = time.time()
        print(f'translaror ru-en finished, elapsed: {end - start} sec')
        return rslt

    def en_ru(self, text: str):
        start = time.time()
        print(f'translator en-ru started')

        model = pipeline("translation", 'Helsinki-NLP/opus-mt-en-ru')
        rslt = model(text)[0]['translation_text']

        end = time.time()
        print(f'translaror en-ru finished, elapsed: {end - start} sec')
        return rslt
