from flask import Flask
from flask_restful import Api, Resource
import collections

app = Flask(__name__)
api = Api(app)

names = collections.defaultdict(lambda:{})
names["shrikanth"] = {"age":25, "gender":"M", "status":"active"},
names["Barry"] = {"age":99, "gender":"M", "status":"not active"}

class HelloWorld(Resource):
    def get(self, name):
        return names[name]

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
