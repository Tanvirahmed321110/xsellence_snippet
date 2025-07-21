from odoo import models, fields, api


class YourModelName(models.Model):
    _name = 'xsellence_snippets.new_product'  # This is the technical name for your model
    _description = 'New Product'  # Description of what this model represents

    name = fields.Char(string='Name', required=True)
    price = fields.Float(string='Price', digits='Product Price')
    image_1920 = fields.Binary(string='Image')
    description = fields.Text(string='Description')