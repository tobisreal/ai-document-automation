import os
import json

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def process_document(document_text):
    """
    Extract structured business information
    from an unstructured document using an LLM.
    """

    prompt = f"""
You are a business document processing system.

Analyze the document below.

First determine whether the document is:
- invoice
- purchase_order
- unknown

Then extract the information into the following JSON structure:

{{
    "document_type": "invoice or purchase_order or unknown",
    "vendor": "vendor or supplier name",
    "document_number": "invoice number or purchase order number",
    "document_date": "invoice date or order date",
    "due_date": "payment due date or expected delivery date",
    "amount": 0.00,
    "purchase_order": "purchase order reference if available",
    "department": "department if available",
    "requested_by": "requester if available"
}}

Rules:

1. Return ONLY valid JSON.
2. Do not include markdown.
3. Do not invent missing information.
4. Use null when information is unavailable.
5. Amount must be a number, not a string.
6. For invoices, document_number means the invoice number.
7. For purchase orders, document_number means the purchase order number.

DOCUMENT:

{document_text}
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    result = response.output_text

    return json.loads(result)