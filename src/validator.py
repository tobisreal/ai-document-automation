def validate_document(data):
    """
    Validate extracted document information.

    Returns APPROVED when all required fields exist.
    Otherwise returns REVIEW_REQUIRED.
    """

    required_fields = [
        "vendor",
        "invoice_number",
        "invoice_date",
        "amount"
    ]

    missing_fields = []

    for field in required_fields:
        if data.get(field) is None:
            missing_fields.append(field)

    if missing_fields:
        return "REVIEW_REQUIRED", missing_fields

    return "APPROVED", []