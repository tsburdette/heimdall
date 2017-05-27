from flask import Flask
from flask_restful import Resource, Api
from crontab import CronTab
import json
import diagnostics

cron = CronTab(user='root')
job = cron.new(command='python ./diagnostics.py')
job.minute.every(1)

cron.write

#diags = diagnostics.Diagnostics()
#diags.record_all_metrics()

app = Flask(__name__)
api = Api(app)

class CurrentMetrics(Resource):
    def get(self):
        with open('diags.json', 'r') as diags_json:
            return json.load(diags_json)

api.add_resource(CurrentMetrics, '/CurrentMetrics')

if __name__ == '__main__':
    app.run(debug=True)
