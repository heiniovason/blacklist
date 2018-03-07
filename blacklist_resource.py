import falcon
import json
from dao import DAO

class BlacklistResource(object):

    def on_post(self, req, resp):
        """Handles POST requests"""

        pnr = json.load(req.stream).get('input')

        # TODO: Validate input

        DAO.open_connection
        # result = DAO.is_pnr_blacklisted(pnr=pnr)
        DAO.close_connection

        # TODO: Perform check

        # TODO: Based check result perform dispatch process, or forward request.__name__

        # TODO: serve result...?

        # Console output.
        info = '{0} {1} {2} {3}'.format(
                req.method, 
                resp.status, 
                req.host, 
                input
                ) 
        print(info)

        doc = { 
                'api_resource': __class__.__name__,
                'request_method': req.method,
                'response_status': resp.status
        }
        resp.body = json.dumps(doc)