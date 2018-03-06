import falcon

from test_resource import TestResource
 
api = falcon.API()
api.add_route('/test_resource', TestResource())