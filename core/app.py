import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse

from core.utils.pdf_action import extract_text_from_pdf
from core.utils.openai_api import summarize_text

# Initialize the FastAPI app
app = FastAPI()


# Define a POST endpoint to summarize the content of an uploaded PDF file
@app.post("/summarize")
async def summarize(file: UploadFile = File(...)) -> JSONResponse:
    # Check if the uploaded file is a PDF
    if file.content_type != 'application/pdf':
        # Raise an HTTP 400 error if the file is not a PDF
        raise HTTPException(
            status_code=400,
            detail="Invalid file type, only PDFs are allowed"
        )
    try:
        # Read the content of the uploaded PDF file
        pdf_bytes = await file.read()
        # Extract text from the PDF
        text = extract_text_from_pdf(pdf_bytes)
        # Check if the extracted text is a dictionary (indicating an error)
        if isinstance(text, dict):
            # Return the error message as a JSON response
            return JSONResponse(text)
        # Summarize the extracted text using an external API
        summary = summarize_text(text)
        # Return the summary as a JSON response
        return JSONResponse(content={"summary": summary})
    except Exception as e:
        # Raise an HTTP 500 error if any exception occurs
        raise HTTPException(status_code=500, detail=str(e))


# Start the Uvicorn server to run the FastAPI app
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
