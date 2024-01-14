FROM python:latest

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python", "./main.py" ]