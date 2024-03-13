FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install redis
RUN pip install requests
CMD ["python", "app.py"]
