# import speech_recognition as sr

# def speech_to_text(audio_file):
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(audio_file) as source:
#         audio = recognizer.record(source)
#     try:
#         return recognizer.recognize_google(audio)
#     except sr.UnknownValueError:
#         return "Speech not understood"
#     except sr.RequestError as e:
#         return f"Error with speech recognition service: {str(e)}"
