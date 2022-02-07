from odoo import http
from odoo.http import request

class realEstate(http.Controller):

    @http.route('/real')
    def hello(self, **kw):
        return "Hello World"