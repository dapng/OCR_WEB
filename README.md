# OCR WEB
With love, using Linux :heart:

[ОТКРЫТЬ OCR WEB](https://recognitionwebapp.herokuapp.com)
##### Веб приложение для распознавания текста
###### Реализовано:

+ Веб интерфейс
+ Распознавание с использованием нейронной сети
+ Single Page Application (частично)
+ Деплой
+ Buildpack для русского и английского языков
###### Использовано:
+ Python 3.9.6
+ Flask, Jinja2, Pillow, Pytesseract, Gunicorn
+ Сервер: Gunicorn

## Установка

Любая из Unix-подобных операционных систем на базе ядра Linux
(я ненавижу Windows, но использую эту операционную систему, в таком случае использовать Windows Subsystem for Linux + Ubuntu)
Установить [Python](https://www.python.org/downloads/) v3.9+ для работы.
Установить apt (для *Linux) и requirements.txt (для Python).

Установка и запуск.

Linux (or WSL)
```sh
sudo apt update
```
```sh
sudo apt install tesseract-ocr
```
```sh
sudo apt install tesseract-ocr-eng
```
```sh
sudo apt install tesseract-ocr-rus
```
```sh
sudo apt install python3.9
```
```sh
pip install requirements.txt
```

Запуск после установки.

```sh
python3 app.py
```

# Скриншоты проекта
### Главная
![](https://i.postimg.cc/JzRJ89n0/photo-2021-08-29-13-07-02.jpg)
***
### В работе
![](https://i.postimg.cc/ZRPHj6sD/photo-2021.jpg)
***

## Использовано:
https://devcenter.heroku.com/articles/buildpacks
https://elements.heroku.com/buildpacks/matteotiziano/heroku-buildpack-tesseract
https://github.com/pathwaysmedical/heroku-buildpack-tesseract
https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-apt
https://github.com/tesseract-ocr/tesseract

## License
**Free Software**
