from flask import Flask
from flask_restful import Api, Resource, reqparse
import collections

app = Flask(__name__)
api = Api(app)

videos = {}
generic_response = {"Status" : "All OK"}
class Video(Resource):
    def get(self, video_id):
        if video_id in videos:
            return videos[video_id]

    def put(self, video_id):
        if video_id in videos:
            return generic_response
        else:
            videos[video_id] = "newVideo"


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
