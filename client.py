from flask import Flask
from flask_restful import Resource, Api
from scheduler import Scheduler
import json
import os

if not os.path.exists('logs'):
    os.makedirs('logs')

scheduler = Scheduler()

app = Flask(__name__)
api = Api(app)

class CurrentHourlyMetrics(Resource):
    def get(self):
        file_name = scheduler.log.file_name
        print "Current log is located at " + str(file_name)
        try:
            with open('logs/' + file_name, 'r') as latest_log:
                return json.load(latest_log)
        except IOError:
            return json.dumps({'Error': 'No data recorded yet.'})

class DeleteLogs(Resource):
    def post(self):
        os.system("rm -rf logs/*")

api.add_resource(CurrentHourlyMetrics, '/CurrentHourlyMetrics')
api.add_resource(DeleteLogs, '/DeleteLogs')

if __name__ == '__main__':
    app.run(debug=True)
