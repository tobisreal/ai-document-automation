import json
import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def process_document(document_text):
    """Extract standardized business data using an LLM."""

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is required when PROCESSOR_MODE=ai"
        )

    client = OpenAI(api_key=api_key)

    schema = {
        "type": "object",
        "properties": {
            "document_type": {
                "type": "string",
                "enum": [
                    "invoice",
                    "purchase_order",
                    "unknown"
                ]
            },
            "vendor": {
                "type": ["string", "null"]
            },
            "document_number": {
                "type": ["string", "null"]
            },
            "document_date": {
                "type": ["string", "null"]
            },
            "due_date": {
                "type": ["string", "null"]
            },
            "amount": {
                "type": ["number", "null"]
            },
            "purchase_order": {
                "type": ["string", "null"]
            },
            "department": {
                "type": ["string", "null"]
            },
            "requested_by": {
                "type": ["string", "null"]
            }
        },
        "required": [
            "document_type",
            "vendor",
            "document_number",
            "document_date",
            "due_date",
            "amount",
            "purchase_order",
            "department",
            "requested_by"
        ],
        "additionalProperties": False
    }

    response = client.responses.create(
        model="gpt-5.6-luna",

        instructions=(
            "You are a business document processing system. "
            "Classify the document and extract its business data. "
            "Do not invent missing information. "
            "Use null when information is unavailable."
        ),

        input=document_text,

        text={
            "format": {
                "type": "json_schema",
                "name": "business_document",
                "strict": True,
                "schema": schema
            }
        }
    )

    return json.loads(response.output_text)