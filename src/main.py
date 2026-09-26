from extractor import read_document
from ai_processor import process_document
from database import create_database, save_document, document_exists
from validator import validate_document
from pathlib import Path
import pandas as pd


DOCUMENT_FOLDER = Path("documents")
OUTPUT_FILE = Path("output/extracted_data.csv")


def main():
    results = []

    create_database()

    supported_extensions = {".txt", ".pdf"}

    documents = [
    file
    for file in DOCUMENT_FOLDER.iterdir()
    if file.suffix.lower() in supported_extensions
]

    print(f"Found {len(documents)} document(s).\n")

    for file_path in documents:

        print(f"Processing: {file_path.name}")

        # Check for duplicates
        if document_exists(file_path.name):
            print("Skipped - document already processed.\n")
            continue

        try:
            # Read document
            document_text = read_document(file_path)

            # Extract information
            extracted_data = process_document(document_text)

            extracted_data["source_file"] = file_path.name

            # Validate extracted information
            status, missing_fields = validate_document(extracted_data)

            extracted_data["status"] = status

            if status == "REVIEW_REQUIRED":
                print(
                    f"Review required - missing: "
                    f"{', '.join(missing_fields)}"
                )
            else:
                print("Validation passed.")

            # Store result
            results.append(extracted_data)

            save_document(extracted_data)

            print("Successfully processed.\n")

        except Exception as error:
            print(
                f"Failed to process {file_path.name}: "
                f"{error}\n"
            )

    # Export new results
    if results:
        dataframe = pd.DataFrame(results)

        dataframe.to_csv(OUTPUT_FILE, index=False)

        print("--------------------------------")
        print("PROCESSING COMPLETE")
        print(f"New documents processed: {len(results)}")
        print(f"CSV saved to: {OUTPUT_FILE}")
        print("Database saved to: output/documents.db")
        print("--------------------------------")

    else:
        print("No new documents to process.")



if __name__ == "__main__":
    main()