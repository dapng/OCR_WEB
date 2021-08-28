try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    photo = Image.open(filename)
    text = pytesseract.image_to_string(photo, lang='rus+eng')
    return text