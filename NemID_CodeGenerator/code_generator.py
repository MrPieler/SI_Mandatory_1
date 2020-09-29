# Created by Jakob

from flask import request, Response, Flask
import json
from db_handler import authenticate_nem_id, generate_auth_log
from random import randint


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/nemid-auth', methods=['POST'])
def api_code_generator():

    # parse body to json
    nem_id_entity = json.loads(request.data)

    # exstract data
    nem_id_code = nem_id_entity.get('nemIdCode')
    nem_id = nem_id_entity.get('nemId')

    # authenticate user
    user_id = None
    if (nem_id is not None and nem_id_code is not None):
        user_id = authenticate_nem_id(nem_id, nem_id_code)

    if user_id is None:
        # create response body
        response_body = {
            "status": "Invalid credentials",
            "error_message" : "The provided NemID and Password does not belong to any user"
        }

        # create response
        response = Response()
        response.status_code = 401
        response.data = json.dumps(response_body)
        return response
    else:
        # generate random 6 digit code 
        code = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"

        # generate auth log
        generate_auth_log(user_id, code)

        # create response body
        response_body = {
            "generatedCode": code
        }

        # create response
        response = Response()
        response.status_code = 200
        response.data = json.dumps(response_body)
        return response

# begin server
app.run(port = 8090)