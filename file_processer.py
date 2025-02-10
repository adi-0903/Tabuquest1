# import os
# import pandas as pd
# from logging_config import logger
# from pdf_processing import process_pdf
# from csv_processing import process_csv
# from excel_processing import process_excel
# from word_processing import process_word_text
# from txt_processing import process_text
# from utilities import config

# def process_all_files(data_folder, vector_db, openai_client, model_name, text_chunker):
#     """
#     Processes all supported file types (PDF, TXT, Word, CSV, Excel) in the specified data folder.
#     """

#     if not os.path.exists(data_folder):
#         logger.error(f"Data folder does not exist: {data_folder}")
#         return

#     for filename in os.listdir(data_folder):
#         file_path = os.path.join(data_folder, filename)

#         try:
#             if filename.lower().endswith('.pdf'):
#                 process_pdf(file_path, vector_db, openai_client, model_name, text_chunker)

#             elif filename.lower().endswith('.txt'):
#                 process_text(file_path, vector_db, text_chunker)

#             elif filename.lower().endswith('.docx'):
#                 process_word_text(file_path, vector_db, text_chunker)

#             elif filename.lower().endswith('.csv'):
#                 process_csv(file_path, vector_db, text_chunker)  # ✅ Fixed

#             elif filename.lower().endswith(('.xls', '.xlsx')):
#                 process_excel(file_path, vector_db, text_chunker)  # ✅ Fixed

#             else:
#                 logger.warning(f"Unsupported file type: {filename}")

#         except Exception as e:
#             logger.error(f"Error processing {filename}: {e}")

#     logger.info("All files processed.")


import os
import pandas as pd
from logging_config import logger
from pdf_processing import process_pdf
from csv_processing import process_csv
from excel_processing import process_excel
from word_processing import process_word_text
from txt_processing import process_text
from utilities import config

def process_all_files(data_folder, vector_db, openai_client, model_name, text_chunker):
    """
    Processes all supported file types (PDF, TXT, Word, CSV, Excel) in the specified data folder.
    """
    if not os.path.exists(data_folder):
        logger.error(f"Data folder does not exist: {data_folder}")
        return

    for filename in os.listdir(data_folder):
        file_path = os.path.join(data_folder, filename)

        try:
            if filename.lower().endswith('.pdf'):
                process_pdf(file_path, vector_db, openai_client, model_name, text_chunker)

            elif filename.lower().endswith('.txt'):
                process_text(file_path, vector_db, text_chunker)

            elif filename.lower().endswith('.docx'):
                process_word_text(file_path, vector_db, text_chunker)

            elif filename.lower().endswith('.csv'):
                process_csv(file_path, vector_db, text_chunker)

            elif filename.lower().endswith(('.xls', '.xlsx')):
                process_excel(file_path, vector_db, text_chunker)

            else:
                logger.warning(f"Unsupported file type: {filename}")

        except Exception as e:
            logger.error(f"Error processing {filename}: {e}")

    logger.info("All files processed.")
