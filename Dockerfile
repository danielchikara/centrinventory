# Dockerfile

FROM python:3.10-slim

COPY requirements.txt requirements.txt
RUN  pip install --no-cache-dir -r requirements.txt

COPY  . code
WORKDIR /code

EXPOSE 8000

ENTRYPOINT [ "python3" ,"centrinventory/manage.py" ]
CMD [ "runserver","0.0.0.0:8000" ]

