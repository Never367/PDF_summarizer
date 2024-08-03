import io
from typing import Union

import PyPDF2


# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file: bytes) -> Union[str, dict]:
    # Initialize a PDF reader object from the byte stream of the PDF file
    reader = PyPDF2.PdfFileReader(io.BytesIO(pdf_file))
    text = ""
    if reader.numPages > 1:
        # Return an error message if the uploaded PDF has more than one page
        return {
            'error': (
                'A PDF file with a length of more than 1 page was uploaded. '
                'Please upload a PDF file that is 1 page long.'
            )
        }
    # Iterate through each page of the PDF
    for page_num in range(reader.numPages):
        # Get the page object
        page = reader.getPage(page_num)
        # Extract text from the page and append it to the text variable
        text += page.extract_text()
    # Return the extracted text
    return text
