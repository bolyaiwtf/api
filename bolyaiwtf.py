import falcon, json, random
from falcon_cors import CORS

cors = CORS(
  allow_all_origins=True,
  allow_all_headers=True,
  allow_methods_list=['GET']
)

class WtfResource:
  def on_get(self, req, resp):
    with open('content.json', encoding='utf8') as content:
      data = json.load(content)
      resp.media = {
        'ok': True,
        'wtf': random.choice(data)
      }

api = falcon.API(middleware=[cors.middleware])
api.add_route('/', WtfResource())
