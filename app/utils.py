import os
import pdfkit

def html_to_pdf(html_content: str, css_content: str = None) -> str:
    """
    Convert HTML content to a PDF file.

    Args:
        html_content: The HTML string.
        css_content: Optional CSS string.

    Returns:
        The file path to the generated PDF.
    """
    output_path = "output.pdf"
    
    # Save HTML and CSS content to temporary files
    html_path = "temp.html"
    css_path = "temp.css" if css_content else None

    with open(html_path, "w") as f:
        f.write(html_content)
    
    if css_content:
        with open(css_path, "w") as f:
            f.write(css_content)
    
    # PDF options
    options = {
        'quiet': ''
    }

    # Generate PDF
    if css_path:
        pdfkit.from_file(html_path, output_path, css=css_path, options=options)
    else:
        pdfkit.from_file(html_path, output_path, options=options)

    # Clean up temporary files
    os.remove(html_path)
    if css_path:
        os.remove(css_path)

    return output_path
