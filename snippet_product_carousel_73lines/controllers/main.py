# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by 73lines
# See LICENSE file for full copyright and licensing details.

from openerp.addons.web.http import request
from openerp.addons.web import http

from openerp.addons.website_sale.controllers.main import QueryURL

from openerp.addons.snippet_object_carousel_73lines.controllers.main import snippet_object_carousel_73lines_controller

class snippet_product_carousel_73lines_controller(snippet_object_carousel_73lines_controller):
    
    def get_rating_stat(self,product,context=None):
        rating_product = product.rating_get_stats([('website_published', '=', True)])
        return rating_product 
    
    @http.route(['/snippet_object_carousel_73lines/render/product.template'], type='json', auth='public', website=True , csrf=False,cache=300)
    def render_product_carousel(self, template, filter_id=False, objects_in_slide=4, limit=1, object_name=False,in_row=1):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        category=None
        
        if context and not context.get('pricelist'):
            pricelist = request.website.get_current_pricelist()
            context['pricelist'] = int(pricelist)
        
        from_currency = pool['res.users'].browse(cr, uid, uid, context=context).company_id.currency_id
        to_currency = pricelist.currency_id
        
        compute_currency = lambda price: pool['res.currency']._compute(cr, uid, from_currency, to_currency, price, context=context)
        
        values = {
                      'compute_currency':compute_currency,
                      'pricelist':pricelist.id,
                      'get_rating_stat' : self.get_rating_stat
                      }
        request.context.update(values)
        res = super(snippet_product_carousel_73lines_controller,self).render_object_carousel(template, filter_id=filter_id, 
                                                                                            objects_in_slide=objects_in_slide, limit=limit, 
                                                                                            object_name=object_name,in_row=in_row)
        
        return res