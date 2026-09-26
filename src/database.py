import sqlite3
from pathlib import Path


DATABASE_PATH = Path("output/documents.db")


def create_database():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_type TEXT,
            vendor TEXT,
            invoice_number TEXT,
            invoice_date TEXT,
            due_date TEXT,
            amount REAL,
            purchase_order TEXT,
            department TEXT,
            source_file TEXT UNIQUE,
            status TEXT,
            processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def document_exists(source_file):
    """Check whether a file has already been processed."""

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT 1 FROM documents WHERE source_file = ?",
        (source_file,)
    )

    exists = cursor.fetchone() is not None

    connection.close()

    return exists


def save_document(data):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO documents (
            document_type,
            vendor,
            invoice_number,
            invoice_date,
            due_date,
            amount,
            purchase_order,
            department,
            source_file,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("document_type"),
        data.get("vendor"),
        data.get("invoice_number"),
        data.get("invoice_date"),
        data.get("due_date"),
        data.get("amount"),
        data.get("purchase_order"),
        data.get("department"),
        data.get("source_file"),
        data.get("status")
    ))

    connection.commit()
    connection.close()