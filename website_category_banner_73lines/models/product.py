# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by 73lines
# See LICENSE file for full copyright and licensing details.

from openerp import fields, models

class product_public_category(models.Model):
    _inherit = "product.public.category"
    
    cover_banner = fields.Html("Cover Banner")
    cover_image = fields.Binary("Cover Image", attachment=True,)
    
    def open_template(self, cr, uid, category_id, context=None):
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': '/category/cover/%d' % category_id[0]
        }