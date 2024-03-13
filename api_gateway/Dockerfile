FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install redis requests flask
CMD ["python", "api_gateway.py"]
