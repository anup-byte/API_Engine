# API_Engine

pip install fastapi uvicorn pdfkit

# Running the Project

Run the FastAPI server using Uvicorn:
uvicorn app.main:app --reload

# Testing the API
curl -X POST "http://127.0.0.1:8000/convert-to-pdf/" \
    -F "html=@templates/sample.html" \
    -F "css=@templates/style.css"
