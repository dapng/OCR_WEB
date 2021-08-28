# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract


from PIL import Image
import pytesseract


# def ocr_core(filename):
#     photo = Image.open(filename)
#     text_go = pytesseract.image_to_string(photo, lang='rus+eng')
#     text = text_go
#     return text
# print(ocr_core('images/2.jpg'))

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename), lang='rus+eng')
    return text
# print(ocr_core('images/1.jpg'))