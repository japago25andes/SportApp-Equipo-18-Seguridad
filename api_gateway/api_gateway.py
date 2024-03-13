from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/<service>/<action>/<port>', methods=['GET', 'POST'])
def gateway(service, action, port=5000):
    if request.method == 'POST':
        data = request.json
        response = requests.post(f'http://{service}:{port}/{action}',
                                 json=data)
        return response.content
    else:
        response = requests.get(f'http://{service}:{port}/{action}')
        return response.content

@app.route('/', methods=['GET'])
def health_check():
    return "API Gateway is up"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
