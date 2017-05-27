from flask import Flask
from flask_restful import Resource, Api
import json
import diagnostics

diags = diagnostics.Diagnostics()
diags.record_cpu_percent()
diags.store_diags()

app = Flask(__name__)
api = Api(app)

class Metrics(Resource):
    def get(self):
        with open('diags.json', 'r') as diags_json:
            return json.load(diags_json)

api.add_resource(Metrics, '/Metrics')

if __name__ == '__main__':
    app.run(debug=True)
