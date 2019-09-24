import falcon, json, random
from falcon_cors import CORS

cors = CORS(
  allow_all_origins=True,
  allow_all_headers=True,
  allow_methods_list=['GET']
)

def load_wtfs():
  with open('content.json', encoding='utf8') as content:
    return json.load(content)

class WtfResource:
  def on_get(self, req, resp):
    resp.media = {
      'ok': True,
      'wtf': random.choice(load_wtfs())
    }

class AllWtfsResource:
  def on_get(self, req, resp):
    resp.media = {
      'ok': True,
      'wtfs': load_wtfs()
    }

api = falcon.API(middleware=[cors.middleware])
api.add_route('/', WtfResource())
api.add_route('/all', AllWtfsResource())
