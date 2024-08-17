from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/service_api', methods=['GET'])
def get_data():
    data = {"message": "Worked!"}
    return jsonify(data)

@app.route('/service_api', methods=['POST'])
def post_data():
    received_data = request.get_json()
    response_data = {"received": received_data}
    return jsonify(response_data), 201

if __name__ == '__main__':
    app.run(debug=True)



#url http://127.0.0.1:5000/service_api