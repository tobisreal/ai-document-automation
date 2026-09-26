import re


def extract_value(pattern, document_text):
    """Extract a value using a regular expression."""

    match = re.search(
        pattern,
        document_text,
        re.IGNORECASE
    )

    return match.group(1).strip() if match else None


def classify_document(document_text):
    """Determine the type of business document."""

    text = document_text.lower()

    if "purchase order" in text:
        return "purchase_order"

    if "invoice" in text:
        return "invoice"

    return "unknown"


def process_invoice(document_text):
    """Extract information from an invoice."""

    vendor = extract_value(
        r"Vendor:\s*(.+)",
        document_text
    )

    invoice_number = extract_value(
        r"Invoice Number:\s*(.+)",
        document_text
    )

    invoice_date = extract_value(
        r"Invoice Date:\s*(.+)",
        document_text
    )

    due_date = extract_value(
        r"Due Date:\s*(.+)",
        document_text
    )

    purchase_order = extract_value(
        r"Purchase Order:\s*(.+)",
        document_text
    )

    department = extract_value(
        r"Department:\s*(.+)",
        document_text
    )

    total = extract_value(
        r"Total:\s*\$?([\d,]+\.\d{2})",
        document_text
    )

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


def process_purchase_order(document_text):
    """Extract information from a purchase order."""

    purchase_order = extract_value(
        r"Purchase Order Number:\s*(.+)",
        document_text
    )

    supplier = extract_value(
        r"Supplier:\s*(.+)",
        document_text
    )

    order_date = extract_value(
        r"Order Date:\s*(.+)",
        document_text
    )

    expected_delivery = extract_value(
        r"Expected Delivery:\s*(.+)",
        document_text
    )

    department = extract_value(
        r"Department:\s*(.+)",
        document_text
    )

    requested_by = extract_value(
        r"Requested By:\s*(.+)",
        document_text
    )

    total = extract_value(
        r"Total:\s*\$?([\d,]+\.\d{2})",
        document_text
    )

    if total:
        total = float(total.replace(",", ""))

    return {
        "document_type": "purchase_order",
        "vendor": supplier,
        "invoice_number": None,
        "invoice_date": order_date,
        "due_date": expected_delivery,
        "amount": total,
        "purchase_order": purchase_order,
        "department": department,
        "requested_by": requested_by
    }


def process_document(document_text):
    """Classify and process a business document."""

    document_type = classify_document(document_text)

    if document_type == "invoice":
        return process_invoice(document_text)

    elif document_type == "purchase_order":
        return process_purchase_order(document_text)

    else:
        return {
            "document_type": "unknown"
        }