import sqlite3


connection = sqlite3.connect("output/documents.db")
cursor = connection.cursor()


cursor.execute("""
    SELECT
        id,
        document_type,
        vendor,
        document_number,
        document_date,
        amount,
        status,
        source_file
    FROM documents
    ORDER BY id
""")


records = cursor.fetchall()


print("\nDOCUMENT DATABASE\n")

for record in records:
    print(record)


connection.close()