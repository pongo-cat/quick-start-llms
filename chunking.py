#Code from 2.3 - 2.6 of various chunking methods

import PyPDF2
import re
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

#2.4, Fixed size chunking, non-overlapping

#2.4, Fixed size chunking, overlapping

#2.5, Chunking based on a delimiter/ natural whitespace

#2.6, Chunking based on a clustering algorithm, semantic similarity