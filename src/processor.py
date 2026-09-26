from rule_processor import process_document as rule_process


PROCESSOR_MODE = "rules"


def process_document(document_text):
    """
    Process a document using the configured extraction engine.

    Available modes:
    - rules
    - ai (planned)
    """

    if PROCESSOR_MODE == "rules":
        return rule_process(document_text)

    elif PROCESSOR_MODE == "ai":
        raise NotImplementedError(
            "AI processing has not been configured yet."
        )

    else:
        raise ValueError(
            f"Unknown processor mode: {PROCESSOR_MODE}"
        )