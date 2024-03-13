FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install redis requests flask flask_jwt_extended flask_cors
CMD ["python", "api_gateway.py"]
