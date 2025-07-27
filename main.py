from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ocr_utils import extract_text_from_pdf
from parser_utils import parse_invoice_data
from correction_utils import correct_invoice_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process_invoice/")
async def process_invoice(file: UploadFile = File(...)):
    contents = await file.read()

    # Step 1: OCR
    raw_text = extract_text_from_pdf(contents)

    # Step 2: Parsing
    parsed_data = parse_invoice_data(raw_text)

    # Step 3: Correction
    corrected_data = correct_invoice_data(parsed_data)

    return {
        "raw_text": raw_text,
        "parsed": parsed_data,
        "corrected": corrected_data
    }
