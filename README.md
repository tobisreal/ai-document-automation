# AI Document Automation

A Python-based business document processing system that extracts, classifies, validates, and stores structured data from invoices and purchase orders.

The project demonstrates how document-processing workflows can be automated using Python, PDF extraction, data validation, SQLite, and CSV reporting. It is being developed toward LLM-powered document understanding and business-process automation.

## Project Overview

Businesses often receive invoices, purchase orders, and other documents in different formats. Manually reviewing these documents and entering their information into spreadsheets or business systems can be repetitive, time-consuming, and error-prone.

This project automates that workflow by processing documents and converting their contents into structured data.

## Current Features

- Batch processing of multiple documents
- TXT document processing
- PDF text extraction
- Invoice classification
- Purchase order classification
- Rule-based field extraction
- Document-specific data validation
- `APPROVED` and `REVIEW_REQUIRED` statuses
- Duplicate document detection
- SQLite database storage
- CSV export
- Error handling
- Modular Python architecture

## How It Works

```text
Business Documents
    TXT / PDF
        |
        v
  Text Extraction
        |
        v
Document Classification
        |
   +----+----+
   |         |
   v         v
Invoice   Purchase Order
   |         |
   +----+----+
        |
        v
 Field Extraction
        |
        v
 Data Validation
        |
   +----+-------------+
   |                  |
   v                  v
APPROVED        REVIEW_REQUIRED
   |                  |
   +--------+---------+
            |
            v
     Duplicate Check
            |
            v
     SQLite Database
            |
            v
        CSV Export
```

## Example

An invoice such as:

```text
INVOICE

Invoice Number: INV-2026-001
Vendor: Prairie Industrial Supplies Ltd.
Invoice Date: September 15, 2026
Due Date: October 15, 2026

Total: $2,415.00

Purchase Order: PO-8831
Department: Operations
```

is converted into structured information:

```json
{
  "document_type": "invoice",
  "vendor": "Prairie Industrial Supplies Ltd.",
  "invoice_number": "INV-2026-001",
  "invoice_date": "September 15, 2026",
  "due_date": "October 15, 2026",
  "amount": 2415.0,
  "purchase_order": "PO-8831",
  "department": "Operations"
}
```

## Project Structure

```text
ai-document-automation/
│
├── documents/
│   ├── invoice_001.txt
│   ├── invoice_002.txt
│   ├── invoice_003.pdf
│   └── purchase_order_001.txt
│
├── output/
│   └── extracted_data.csv
│
├── src/
│   ├── extractor.py
│   ├── ai_processor.py
│   ├── database.py
│   ├── validator.py
│   ├── view_database.py
│   └── main.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Technologies

- Python
- SQLite
- SQL
- pandas
- PyPDF
- Regular Expressions
- Git
- GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/tobisreal/ai-document-automation.git
cd ai-document-automation
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Place supported documents inside the `documents` directory.

Run the processing pipeline:

```bash
python src/main.py
```

View stored database records:

```bash
python src/view_database.py
```

Processed data is stored in the SQLite database and exported to:

```text
output/extracted_data.csv
```

## Validation and Human Review

The system validates required fields based on the detected document type.

Documents containing the required information are marked:

```text
APPROVED
```

Documents with missing required information are marked:

```text
REVIEW_REQUIRED
```

This prevents incomplete data from being silently treated as valid and provides a basic human-review workflow.

## Current Limitation

The current version primarily uses rule-based extraction with regular expressions.

This approach works when document layouts and field names are predictable but becomes less reliable when different suppliers use different formats.

For example:

```text
Invoice Number: INV-100
```

and:

```text
Invoice #INV-100
```

contain the same business information but have different structures.

This limitation is one of the reasons the project is being extended with LLM-based document understanding.

## Planned Improvements

- LLM-powered document extraction
- Structured AI outputs
- Improved database schema
- Scanned PDF and image processing
- Confidence and human-review workflow
- Additional business document types
- Reporting/dashboard interface
- API integrations
- Business-system/ERP integration concepts

## Purpose

This project demonstrates practical experience with:

- Python automation
- Business-process automation
- Document processing
- Data extraction and transformation
- SQL and database storage
- Data validation
- Error handling
- System integration concepts
- Designing workflows that can later incorporate AI and LLM technologies