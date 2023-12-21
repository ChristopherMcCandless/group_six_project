from src.models.summarizer import Summarizer
from src.models.translator import Translator


class TextSummaryService():
    """
    Оркестратор пайплайна суммаризации
    """

    def __init__(self):
        self.translator = Translator()
        self.summarizer = Summarizer()

    def handle_ru(self, text: str):
        enText = self.translator.ru_en(text)
        original_summary = self.summarizer.summarize(enText)
        ruSummary = self.translator.en_ru(original_summary)
        return original_summary, ruSummary
