# Invoice OCR Extraction API Project

# Overview

This project extracts data from invoice PDFs using OCR and provides cleaned and corrected structured output in JSON format.

It includes:
- OCR extraction using Tesseract
- Invoice field parsing (invoice number, date, total)
- Rule-based correction logic (e.g., date formatting, amount validation)
- FastAPI endpoint for uploading and processing PDFs
- CLI script for direct testing from terminal
- Postman collection for API testing

---

# How to Run (FastAPI)

# 1. Install dependencies:
```bash
pip install -r requirements.txt
