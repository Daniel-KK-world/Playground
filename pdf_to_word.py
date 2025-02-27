from pdf2docx import Converter

def convert_pdf_to_word(pdf_path, word_path):
    # Create a converter object
    cv = Converter(pdf_path)  # Use Converter, not converter
    
    # Convert the PDF to a Word file
    cv.convert(word_path, start=0, end=None)
    
    # Close the converter
    cv.close()

# Example usage
pdf_path = r"C:\Users\user\Desktop\Playground\BGEC 103 WEEK 5-BUSINESS LETTERS.txt.pptx"  # Ensure this is a PDF file
word_path = "week5.docx"  # Desired output Word file

convert_pdf_to_word(pdf_path, word_path)
