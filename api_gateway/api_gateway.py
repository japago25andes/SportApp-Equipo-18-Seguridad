from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import requests

def create_app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "frase-secreta"
    app.config["PROPAGATE_EXCEPTIONS"] = True

    #CORS(app)
    jwt = JWTManager(app)

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return ""


    return app

app = create_app()




@app.route('/<service>/<action>/<port>', methods=['GET', 'POST'])
@jwt_required()
def gateway(service, action, port=5000):
    if request.method == 'POST':
        data = request.json
        response = requests.post(f'http://{service}:{port}/{action}',
                                 json=data)
        return response.content
    else:
        print(f'salida: http://{service}:{port}/{action}')
        response = requests.get(f'http://{service}:{port}/{action}')
        print(response.content)
        #return response.content
        return "perfecto"

@app.route('/login', methods=['POST'])
def token():
   user = request.json['user']
   password = request.json['password']

   if (user != "sportApp" or password != "123456"):
        return {"error": "Invalid user or password"}, 401

   token = create_access_token(identity=user)
   print(token)
   return {"token": token, "error": ""}, 200


@app.route('/', methods=['GET'])
def health_check():
    return "API Gateway is up"




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
