from pdf2docx import Converter

def convert_pdf_to_word(pdf_path, word_path):
    try:
        cv = Converter(pdf_path)
        cv.convert(word_path, start=0, end=None)
        print(f"Successfully converted {pdf_path} to {word_path}")
    except Exception as e:
        print(f"Conversion failed: {e}")
    finally:
        cv.close()

pdf_path = r"pdf_2_word\CHAPTER4 (3).pdf"
word_path = r"pdf_2_word\CHAPTER 4.docx"  # Use raw string (or double backslashes)

convert_pdf_to_word(pdf_path, word_path)