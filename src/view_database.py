import sqlite3


connection = sqlite3.connect("output/documents.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT
        id,
        document_type,
        vendor,
        invoice_number,
        amount,
        source_file
    FROM documents
""")


records = cursor.fetchall()

print("\nDOCUMENT DATABASE\n")

for record in records:
    print(record)


connection.close()