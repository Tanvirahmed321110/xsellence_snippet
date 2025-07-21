from odoo import http
from odoo.http import request

class DynamicProductSnippet(http.Controller):

    @http.route('/dynamic_cart1/', type='json', auth='public', website=True, methods=['POST'])
    def dynamic_product_snippet(self):
        products = request.env['res.country'].sudo().search_read([], limit=12)
        # result = [{'id': p.id, 'name': p.name} for p in products]
        return products
