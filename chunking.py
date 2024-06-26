#Code from 2.3 - 2.6 of various chunking methods

import PyPDF2
import tiktoken
import numpy
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.pairwise import cosine_similarity

#2.3, No chunking
def no_chunking(file):
    """
    Function to extract text from a PDF file without chunking
    __________
    Parameters:
    file: str
        Path to the PDF file
    __________
    Returns:
    text: str
        Text extracted from the PDF file

    """
    with open(file, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in range(reader.pages):
            new_text = page.extract_text()
            text += '\n\n' + new_text #Edit to add starting point
        text = text.strip()

    return text

#2.4, Fixed size chunking

def fixed_size_chunking(file, chunk_size, overlap = 0, text = None):
    """
    Function to extract text from a PDF file with fixed size chunking
    __________
    Parameters:
    file: str
        Path to the PDF file
    chunk_size: int
        Number of characters in each chunk
    overlap: int
        Number of characters to overlap between chunks
    text: str
        Text extracted from the PDF file (if already extracted)
    __________
    Returns:
    chunks: str
        Chunks extracted from the PDF file

    """
    if text is None:
        with open(file, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in range(reader.pages):
                new_text = page.extract_text()
                text += '\n\n' + new_text #Edit to add starting point
            text = text.strip()

    chunks = []
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
    n_tokens = [len(sentence.split()) for sentence in sentences]

#2.5, Chunking based on a delimiter/ natural whitespace

#2.6, Chunking based on a clustering algorithm, semantic similarity