    
import re
from datetime import datetime

def correct_invoice_data(data):
    corrected = data.copy()

    # --- 1. Date format correction ---
    if data.get("date"):
        try:
            # Try to parse known format and convert to YYYY-MM-DD
            parsed_date = datetime.strptime(data["date"], "%d %B %Y")
            corrected["date"] = parsed_date.strftime("%Y-%m-%d")
        except Exception:
            corrected["date"] = data["date"]  # Leave unchanged if parsing fails

    # --- 2. Total field correction (convert to int if numeric) ---
    if data.get("total"):
        total_clean = re.sub(r"[^\d]", "", data["total"])
        if total_clean.isdigit():
            corrected["total"] = int(total_clean)

    # --- 3. Clean invoice number ---
    if data.get("invoice_no"):
        corrected["invoice_no"] = data["invoice_no"].strip().upper()

    return corrected
