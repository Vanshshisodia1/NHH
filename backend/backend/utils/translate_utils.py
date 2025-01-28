from googletrans import Translator

def translate_text(text, target_language="es"):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text
