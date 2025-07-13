from odoo import http
from odoo.http import request as req


class Products(http.Controller):
    @http.route('/new_product', auth='public', type='json')
    def new_product_f(self):
        new_product = req.env['theme_tutorial.new_product']
        print(len(new_product))
        return new_product
