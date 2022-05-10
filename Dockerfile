FROM python:3.9.4-buster

#INSTRUCCIONES QUE TIENE QUE SEGUIR CUANDO SE INICIALIZA
EXPOSE 8000

COPY . /app

WORKDIR /app

RUN pip install -r /app/requirements.txt

CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload

