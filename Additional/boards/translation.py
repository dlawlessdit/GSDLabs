from modeltranslation.translator import translator, TranslationOptions
from .models import Board

class BoardTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

translator.register(Board, BoardTranslationOptions)
