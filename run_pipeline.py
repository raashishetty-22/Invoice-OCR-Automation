import sys
import os
from ocr_utils import extract_text_from_pdf
from parser_utils import parse_invoice_data
from correction_utils import correct_invoice_data

def run_pipeline(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"❌ File not found: {pdf_path}")
        return

    # Step 1: OCR
    print("🔍 Performing OCR...")
    raw_text = extract_text_from_pdf(pdf_path)

    # Step 2: Parsing
    print("🧠 Parsing data...")
    parsed_data = parse_invoice_data(raw_text)

    # Step 3: Correction
    print("🛠️ Applying corrections...")
    corrected_data = correct_invoice_data(parsed_data)

    # Final Output
    result = {
        "raw_text": raw_text,
        "parsed": parsed_data,
        "corrected": corrected_data
    }

    print("\n✅ Final Output:")
    print(result)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_pipeline.py path/to/invoice.pdf")
    else:
        run_pipeline(sys.argv[1])
