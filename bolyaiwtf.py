import falcon
import json
import random

class WtfResource:
  def on_get(self, req, resp):
    with open('content.json', encoding='utf8') as content:
      data = json.load(content)
      resp.media = random.choice(data)

api = falcon.API()
api.add_route('/', WtfResource())
