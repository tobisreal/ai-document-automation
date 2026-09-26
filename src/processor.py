import os

from rule_processor import process_document as rule_process


PROCESSOR_MODE = os.getenv(
    "PROCESSOR_MODE",
    "rules"
).lower()


def process_document(document_text):
    """
    Select the configured document extraction engine.

    Available modes:
    - rules
    - ai
    """

    if PROCESSOR_MODE == "rules":

        return rule_process(document_text)

    elif PROCESSOR_MODE == "ai":

        from ai_processor import process_document as ai_process

        return ai_process(document_text)

    else:

        raise ValueError(
            f"Unknown processor mode: {PROCESSOR_MODE}"
        )