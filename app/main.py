from fastapi import FastAPI, HTTPException, UploadFile, Form
from fastapi.responses import FileResponse
from app.utils import html_to_pdf
import os

app = FastAPI()

@app.post("/convert-to-pdf/")
async def convert_to_pdf(
    html: UploadFile,
    css: UploadFile = None
):
    """
    Endpoint to convert HTML (and optional CSS) to a PDF.
    """
    try:
        # Read HTML content
        html_content = await html.read()
        css_content = await css.read() if css else None

        # Convert to PDF
        output_file = html_to_pdf(html_content.decode(), css_content.decode() if css_content else None)

        # Return the PDF file
        return FileResponse(
            output_file, 
            media_type="application/pdf", 
            filename="output.pdf"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
