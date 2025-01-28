from fastapi import APIRouter, File, UploadFile
from utils.ocr_utils import extract_text_from_image
from utils.translate_utils import translate_text

router = APIRouter()

@router.post("/upload/")
async def upload_prescription(file: UploadFile = File(...), lang: str = "es"):
    # Save the uploaded file temporarily
    file_location = f"static/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(file.file.read())

    # Extract text using OCR
    extracted_text = extract_text_from_image(file_location)

    # Translate the extracted text
    translated_text = translate_text(extracted_text, target_language=lang)

    return {
        "original_text": extracted_text,
        "translated_text": translated_text,
    }
