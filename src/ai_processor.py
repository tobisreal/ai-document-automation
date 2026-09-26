import re


def process_document(document_text):
    """
    Mock document processor.

    Extracts invoice information locally without calling an AI API.
    Later, this function will be replaced with an LLM-powered processor.
    """

    def extract(pattern):
        match = re.search(pattern, document_text, re.IGNORECASE)
        return match.group(1).strip() if match else None

    vendor = extract(r"Vendor:\s*(.+)")
    invoice_number = extract(r"Invoice Number:\s*(.+)")
    invoice_date = extract(r"Invoice Date:\s*(.+)")
    due_date = extract(r"Due Date:\s*(.+)")
    purchase_order = extract(r"Purchase Order:\s*(.+)")
    department = extract(r"Department:\s*(.+)")

    total = extract(r"Total:\s*\$?([\d,]+\.\d{2})")

    if total:
        total = float(total.replace(",", ""))

    return {
        "document_type": "invoice",
        "vendor": vendor,
        "invoice_number": invoice_number,
        "invoice_date": invoice_date,
        "due_date": due_date,
        "amount": total,
        "purchase_order": purchase_order,
        "department": department
    }