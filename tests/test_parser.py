from app.parser import parse_resume

def test_parse_pdf_returns_text():
    filename = "test.pdf"
    fake_pdf_bytes = b"%PDF-1.4\n%Fake PDF Content here\n%%EOF"
    
    result = parse_resume(filename, fake_pdf_bytes)

    assert "text" in result
    assert isinstance(result["text"], str)
    assert len(result["text"]) > 0
