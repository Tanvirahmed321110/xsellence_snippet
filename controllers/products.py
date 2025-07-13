from odoo import http

class Products(http.Controller):
    @http.route('/all_products', auth='public', type='json')
    def all_products(self):
        all_products = ['pd1', 'pd2', 'pd3']
        return all_products