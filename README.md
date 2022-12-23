# image2docx
OCR Python script that reads filtered images and writes texts to a document. 

## Requirements
- Pillow==7.2.0
- pytesseract==0.3.7
- python-docx==0.8.11

## Guide
- `pip install python-docx`
- `pip install Pillow`
- `pip install pytesseract`

You'll need to install Pytesseract on your machine and note the path of it's executable. This tool is Google’s Tesseract-OCR engine. Python-docx is a library for creating and updating Microsoft Word (.docx) files. Pillow helps with manipulating and saving images. Images in this script are filtered in case pictures do not have clear texts.
Example:
```
path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
convertImageToDoc('image044.jpg', path, 'new_image.jpg', 'new_doc.docx')
```
