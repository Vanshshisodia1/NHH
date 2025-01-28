from PIL import Image
import pytesseract

def digitize_prescription(file):
    try:
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"Error processing image: {str(e)}"
