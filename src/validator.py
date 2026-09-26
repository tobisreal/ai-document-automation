def validate_document(data):
    """Validate fields according to document type."""

    document_type = data.get("document_type")

    if document_type == "invoice":
        required_fields = [
            "vendor",
            "invoice_number",
            "invoice_date",
            "amount"
        ]

    elif document_type == "purchase_order":
        required_fields = [
            "vendor",
            "purchase_order",
            "invoice_date",
            "amount"
        ]

    else:
        return "REVIEW_REQUIRED", ["document_type"]

    missing_fields = []

    for field in required_fields:
        if data.get(field) is None:
            missing_fields.append(field)

    if missing_fields:
        return "REVIEW_REQUIRED", missing_fields

    return "APPROVED", []