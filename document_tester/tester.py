from docx import Document


def test_document(document):
    with document.open() as d:
        doc = Document(d)
        for p in doc.paragraphs:
            print(p.text)
