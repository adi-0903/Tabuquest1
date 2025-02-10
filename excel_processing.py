# import pandas as pd
# from logging_config import logger

# def process_excel(file_path, vector_db, text_chunker):
#     """
#     Processes an Excel (.xls/.xlsx) file, extracts its text, splits it into chunks, and stores it in the vector database.
#     """
#     try:
#         df = pd.read_excel(file_path, dtype=str)  # Read Excel as text
#         text_data = df.to_string(index=False)

#         # Chunk the extracted text
#         chunks = text_chunker.split_text(text_data)
#         for chunk in chunks:
#             vector_db.add_documents([chunk])  # ✅ FIX: Properly add text chunks

#         logger.info(f"Excel file processed: {file_path}")

#     except Exception as e:
#         logger.error(f"Error processing Excel file {file_path}: {e}")
import pandas as pd
from logging_config import logger

def process_excel(file_path, vector_db, text_chunker):
    """
    Processes an Excel file, extracts text, splits it into chunks, and stores it in the vector database.
    """
    try:
        df = pd.read_excel(file_path, dtype=str)
        text_data = df.to_string(index=False)

        # Chunk the extracted text
        chunks = text_chunker.split_text(text_data)
        for i, chunk in enumerate(chunks):
            vector_db.add(  # ✅ Using ChromaDB
                ids=[f"{file_path}_{i}"],  # Unique ID
                documents=[chunk]
            )

        logger.info(f"Excel file processed: {file_path}")

    except Exception as e:
        logger.error(f"Error processing Excel file {file_path}: {e}")
