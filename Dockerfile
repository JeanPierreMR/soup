FROM python:3-alpine
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY README.md /app
COPY soup.py /app
CMD [ "python", "./soup.py" ]
#ENV DEVELOPER="Marcos Cano"