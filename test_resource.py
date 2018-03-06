import falcon

class TestResource(object):

    def on_get(self, req, resp):
        resp.body = ('Here you go!')
        resp.status = falcon.HTTP_200