# import os
# import logging
# import json
# from dotenv import load_dotenv

# # Import from existing modules
# from csv_processing import process_csv_file
# #from xlsx_processing import process_xlsx_file
# from file_processer import process_all_files
# from logging_config import logger
# from utilities import config

# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Load configuration from JSON
# with open('config.json', 'r') as config_file:
#     config = json.load(config_file)

# def initialize_gemini_client():
#     """
#     Initialize the Google Gemini client.

#     Returns:
#         genai (Google Gemini Client)
#     """
#     api_key = os.getenv("GEMINI_API_KEY")
#     if not api_key:
#         raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
    
#     # Configure Google Gemini API
#     genai.configure(api_key=api_key)
#     return genai

# def main():
#     """
#     Main function to run the application.
#     """
#     input_folder = config['settings']['input_folder']
#     output_folder = config['settings']['output_folder']

#     # Initialize Gemini Client
#     gemini_client = initialize_gemini_client()

#     # Process input files
#     try:
#         logger.info(f"Processing files in input folder: {input_folder}")
#         process_all_files(input_folder, output_folder, gemini_client)
#         logger.info("File processing completed successfully.")
#     except FileNotFoundError as e:
#         logger.error(f"File not found: {e}")
#     except Exception as e:
#         logger.error(f"Unexpected error during file processing: {e}")

# if __name__ == "__main__":
#     main()
import os
import logging
import json
import chromadb  # ✅ Using ChromaDB
from dotenv import load_dotenv
from file_processer import process_all_files
from logging_config import logger
from utilities import config
from text_splitter import TextSplitter  # ✅ Ensure this module exists

import google.generativeai as genai

# Load environment variables
load_dotenv()

# Load configuration from JSON
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# ✅ Initialize ChromaDB Vector Storage
chroma_client = chromadb.PersistentClient(path="vector_db")
vector_db = chroma_client.get_or_create_collection("my_collection")

# ✅ Define model name for Gemini API
model_name = "gemini-pro"

# ✅ Initialize text chunker
text_chunker = TextSplitter(chunk_size=512)  # Ensure this class exists

def initialize_gemini_client():
    """
    Initialize the Google Gemini client.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
    
    genai.configure(api_key=api_key)
    return genai

def main():
    """
    Main function to run the application.
    """
    input_folder = config['settings']['input_folder']
    output_folder = config['settings']['output_folder']

    # Initialize Google Gemini Client
    gemini_client = initialize_gemini_client()

    # Process input files
    try:
        logger.info(f"Processing files in input folder: {input_folder}")
        process_all_files(input_folder, vector_db, gemini_client, model_name, text_chunker)  # ✅ FIXED
        logger.info("File processing completed successfully.")
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
    except Exception as e:
        logger.error(f"Unexpected error during file processing: {e}")

if __name__ == "__main__":
    main()
