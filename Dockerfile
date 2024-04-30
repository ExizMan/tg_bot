FROM python:alpine
LABEL authors="exiz"
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt


CMD ["python", "/bot/main.py"]

