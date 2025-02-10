from langchain.schema import Document
from typing import Any, List
import os
from logging_config import logger
from utilities import config

def image_db_insetter(vector_db: Any, image_summaries_texts: List[str], image_path: str, pdf_name: str, page_no: int) -> None:
    if not image_summaries_texts:
        raise ValueError("The image summaries list cannot be empty.")
    if page_no < 1:
        raise ValueError("Page number must be a positive integer.")
    
    documents = []
    for text in image_summaries_texts:
        documents.append(Document(page_content=text, metadata={
            "Source": os.path.basename(pdf_name),
            "PageNo": page_no,
            "ImagePath": image_path,
            "Type": "Image"
        }))
    
    try:
        vector_db.add_documents(documents=documents)
    except Exception as e:
        raise Exception(f"An error occurred while adding documents to the vector database: {e}")

def text_db_insetter(vector_db: Any, texts: List[str], pdf_name: str, page_no: int) -> None:
    if not texts:
        raise ValueError("The texts list cannot be empty.")
    if page_no < 1:
        raise ValueError("Page number must be a positive integer.")
    
    documents = []
    for text in texts:
        documents.append(Document(page_content=text, metadata={
            "Source": os.path.basename(pdf_name),
            "PageNo": page_no,
            "Type": "Text"
        }))
    
    try:
        vector_db.add_documents(documents=documents)
    except Exception as e:
        raise Exception(f"An error occurred while adding documents to the vector database: {e}")

def create_retriever(vector_db: Any, search_type: str, top_k: int) -> Any:
    # Validate the search_type
    valid_search_types = ['similarity', 'similarity_score_threshold', 'mmr']
    if search_type not in valid_search_types:
        raise ValueError(f"Invalid search_type '{search_type}'. Valid values are: {valid_search_types}")
    
    retriever = vector_db.as_retriever(search_type=search_type, search_kwargs={"k": top_k})
    return retriever

def retrieve_documents(retriever: Any, question: str) -> List[Document]:
    if not question or not isinstance(question, str):
        logger.error("Invalid question provided: %s", question)
        raise ValueError("The question must be a non-empty string.")
    
    try:
        results = retriever.invoke(input=question)
        logger.info("Retrieved %d documents for question: %s", len(results), question)
        return results
    except Exception as e:
        logger.error("Error retrieving documents: %s", str(e))
        return []
