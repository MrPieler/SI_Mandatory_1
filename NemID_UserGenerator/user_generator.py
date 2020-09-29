from flask import request, Response, Flask
import json
from random import randint


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/generate-nemID", methods=["POST"])
def api_nemID_generator():

    # exstract data
    cpr = request.args.get("cpr")
    email = request.args.get("email")

    if (cpr is None or email is None):
        # create response body
        response_body = {
            "status": "Missing parameters",
            "error_message" : "To generate a nemID you need to specify a cpr and email"
        }

        # create response
        response = Response()
        response.status_code = 401
        response.data = json.dumps(response_body)
        return response
    else:
        # generate random 5 digit code 
        random_digits = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"

        # create response body
        response_body = {
            "nemId": f"{random_digits}-{cpr[-4:]}"
        }

        # create response
        response = Response()
        response.status_code = 201
        response.data = json.dumps(response_body)
        return response

if __name__ == "__main__":
    # begin server
    app.run(port = 8088)
    