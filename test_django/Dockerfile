FROM python:3

RUN mkdir /test_server
RUN mkdir /test_server/test_django

WORKDIR /test_server/test_django

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]