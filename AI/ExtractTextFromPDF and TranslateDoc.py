from PIL import Image
import pytesseract
from googletrans import Translator
from langdetect import detect
from pdf2image import convert_from_path

# Load document (image or PDF)
is_pdf = True  # change this if you're working with image

if is_pdf:
    pages = convert_from_path(r"D:\Education\Datascience\PYTHON_BIGINNER\AI\Dead Copy.pdf", 300)
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page) + "\n"
else:
    image = Image.open("registration_image.jpg")
    text = pytesseract.image_to_string(image)

# Detect original language
lang = detect(text)

# Translate
translator = Translator()
translated = translator.translate(text, src=lang, dest='en')

# Output
print("Original Language:", lang)
print("\nTranslated Text:\n", translated.text)
