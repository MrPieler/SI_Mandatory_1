from flask import request, Response, Flask
import json


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/generate-password-nemID", methods=["POST"])
def api_nemID_generator():

    # exstract data
    nemID = request.args.get("nemId")
    cpr = request.args.get("cpr")

    if (cpr is None or nemID is None):
        # create response body
        response_body = {
            "status": "Missing parameters",
            "error_message" : "To generate a nemID you need to specify a cpr and a nemId"
        }

        # create response
        response = Response()
        response.status_code = 401
        response.data = json.dumps(response_body)
        return response
    else:

        # create response body with password
        response_body = {
            "nemIdPassword": f"{nemID[:2]}{cpr[-2:]}"
        }

        # create response
        response = Response()
        response.status_code = 200
        response.data = json.dumps(response_body)
        return response

if __name__ == "__main__":
    # begin server
    app.run(port = 8089)
    