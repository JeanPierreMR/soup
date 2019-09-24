FROM python:3-alpine
ENV DEVELOPER="Jean Mejicanos"
WORKDIR /app
RUN mkdir /logs
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY soup.py /app
CMD [ "python", "./soup.py" ]
