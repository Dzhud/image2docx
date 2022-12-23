import pytesseract
from PIL import Image, ImageFilter
from docx import Document

# To take care of possible unrecognized characters
def valid_xml_char_ordinal(c):
    codepoint = ord(c)
    return (
            0x20 <= codepoint <=0xD7FF or
            codepoint in (0x9, 0xA,0xD) or
            0xE000 <= codepoint <= 0xFFFD or
            0x10000 <= codepoint <= 0x10FFFF
        )

def convertImageToDoc(image:str, path:str, new_image_name_dot_jpeg:str, new_doc_name_dot_doc:str):
    img = Image.open(image).filter(ImageFilter.MinFilter(3)) # Filters image incase it isn't clear enough
    img.save(new_image_name_dot_jpeg)
    pytesseract.pytesseract.tesseract_cmd = path # Directory where Pytesseract's executable is located on your machine
    get_string_from_image = pytesseract.image_to_string(img)
    cleaned_string = ''.join(c for c in get_string_from_image if valid_xml_char_ordinal(c))
    my_doc = Document()
    my_doc.add_paragraph(cleaned_string)
    my_doc.save(new_doc_name_dot_doc)
    print('Image Read and Doc written')

 # Pass in the necessary arguments accordingly 
convertImageToDoc()

    
