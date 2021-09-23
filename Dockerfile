FROM python:latest

RUN apt-get update
RUN apt-get -y install \
 tesseract-ocr \
 tesseract-ocr-eng \
 tesseract-ocr-rus \
 libgl1-mesa-dev; 
RUN apt-get clean

RUN pip install --upgrade pip; \
 pip install \
 pillow \
# opencv-python \
 pytesseract \
 clic \
 flask \
 gunicorn

COPY . /OCR_WEB
WORKDIR /OCR_WEB
