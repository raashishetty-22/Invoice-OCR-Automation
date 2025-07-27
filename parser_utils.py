import re

def parse_invoice_data(text: str) -> dict:
    # Try multiple patterns to catch different invoice formats
    invoice_no_match = re.search(r"(?:Invoice\s*(?:No|#)[:\s]*)\s*([A-Za-z0-9\-]+)", text, re.IGNORECASE)
    date_match = re.search(r"Date[:\s]*([0-9]{1,2}\s+\w+\s+[0-9]{4})", text)
    total_match = re.search(r"(?:Total Amount|Total Due)[:\s]*Rs\.?\s*([0-9]+)", text)

    invoice_no = invoice_no_match.group(1) if invoice_no_match else None
    date = date_match.group(1) if date_match else None
    total = total_match.group(1) if total_match else None

    return {
        "invoice_no": invoice_no,
        "date": date,
        "total": total
    }
