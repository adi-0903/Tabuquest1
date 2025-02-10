#mport pandas as pd
#rom logging_config import logger
#
#ef process_csv(file_path, vector_db, text_chunker):
#   """
#   Processes a CSV file, extracts its text, splits it into chunks, and stores it in the vector database.
#   """
#   try:
#       df = pd.read_csv(file_path, dtype=str)  # Read CSV as text to avoid type issues
#       text_data = df.to_string(index=False)  # Convert entire DataFrame to a string
#
#       # Chunk the extracted text
#       chunks = text_chunker.split_text(text_data)
#       for chunk in chunks:
#           vector_db.add_documents([chunk])  # ✅ FIX: Properly add text chunks
#
#       logger.info(f"CSV file processed: {file_path}")
#
#   except Exception as e:
#       logger.error(f"Error processing CSV file {file_path}: {e}")

import pandas as pd
from logging_config import logger

def process_csv(file_path, vector_db, text_chunker):
    """
    Processes a CSV file, extracts text, splits it into chunks, and stores it in the vector database.
    """
    try:
        df = pd.read_csv(file_path, dtype=str)
        text_data = df.to_string(index=False)

        # Chunk the extracted text
        chunks = text_chunker.split_text(text_data)
        for i, chunk in enumerate(chunks):
            vector_db.add(  # ✅ Using ChromaDB
                ids=[f"{file_path}_{i}"],  # Unique ID
                documents=[chunk]  # Store text
            )

        logger.info(f"CSV file processed: {file_path}")

    except Exception as e:
        logger.error(f"Error processing CSV file {file_path}: {e}")
