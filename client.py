from flask import Flask
from flask_restful import Resource, Api
from crontab import CronTab
import getpass
import json
import diagnostics

""" Run cron to record new diagnostics periodically.
TODO: Add arguments for user and time interval.
"""
cron = CronTab(user=getpass.getuser())
job = cron.new(command='python ./diagnostics.py')
job.minute.every(1)

cron.write()

#diags = diagnostics.Diagnostics()
#diags.record_all_metrics()

app = Flask(__name__)
api = Api(app)

class CurrentMetrics(Resource):
    def get(self):
        try:
            with open('diags.json', 'r') as diags_json:
                return json.load(diags_json)
        except IOError:
            return json.dumps({'Error': 'No data recorded yet.'})
	def post(self):
		os.system("python ./diagnostics.py")

api.add_resource(CurrentMetrics, '/CurrentMetrics')

if __name__ == '__main__':
    app.run(debug=True)
