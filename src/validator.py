def validate_document(data):
    """Validate extracted document information."""

    document_type = data.get("document_type")

    if document_type not in ["invoice", "purchase_order"]:
        return "REVIEW_REQUIRED", ["document_type"]

    required_fields = [
        "vendor",
        "document_number",
        "document_date",
        "amount"
    ]

    missing_fields = []

    for field in required_fields:
        value = data.get(field)

        if value is None or value == "":
            missing_fields.append(field)

    if missing_fields:
        return "REVIEW_REQUIRED", missing_fields

    return "APPROVED", []