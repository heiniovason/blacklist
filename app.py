import falcon

from test_resource import TestResource
from blacklist_resource import BlacklistResource
 
api = falcon.API()
api.add_route('/test_resource', TestResource())
api.add_route('/blacklist', BlacklistResource())