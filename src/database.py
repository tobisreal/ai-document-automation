import sqlite3
from pathlib import Path


DATABASE_PATH = Path("output/documents.db")


def create_database():
    """Create the document database."""

    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            document_type TEXT NOT NULL,
            vendor TEXT,

            document_number TEXT,
            document_date TEXT,
            due_date TEXT,

            amount REAL,

            purchase_order TEXT,
            department TEXT,
            requested_by TEXT,

            source_file TEXT UNIQUE NOT NULL,

            status TEXT NOT NULL,

            processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def document_exists(source_file):
    """Check whether a source file has already been processed."""

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
    """Save processed document information."""

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO documents (
            document_type,
            vendor,
            document_number,
            document_date,
            due_date,
            amount,
            purchase_order,
            department,
            requested_by,
            source_file,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("document_type"),
        data.get("vendor"),
        data.get("document_number"),
        data.get("document_date"),
        data.get("due_date"),
        data.get("amount"),
        data.get("purchase_order"),
        data.get("department"),
        data.get("requested_by"),
        data.get("source_file"),
        data.get("status")
    ))

    connection.commit()
    connection.close()