import easyocr
import numpy as np
from pdf2image import convert_from_bytes

reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_pdf(file_bytes: bytes) -> str:
    images = convert_from_bytes(file_bytes)
    full_text = ""

    for img in images:
        result = reader.readtext(np.array(img), detail=0, paragraph=True)
        full_text += "\n".join(result) + "\n"

    return full_text
