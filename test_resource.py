import falcon, json

class TestResource(object):

    def on_get(self, req, resp):
        """Handles GET requests"""

        doc = {'message': 'GET works.'}
        resp.body = json.dumps(doc)

        # Console output. 
        print('{0} {1} {2}'.format(req.method, resp.status, req.host))
        