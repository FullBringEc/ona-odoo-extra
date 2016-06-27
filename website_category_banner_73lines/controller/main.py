# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import SUPERUSER_ID
from openerp.addons.web import http
from openerp.addons.web.http import request
import werkzeug
import datetime
import time

from openerp.tools.translate import _
from openerp.addons.website_mail.controllers.main import _message_post_helper


class category_cover_banner(http.Controller):

    @http.route(["/category/cover/<model('product.public.category'):banner>"], type='http', auth="user", website=True)
    def template_view(self, banner, **post):
        values = { 'template': banner }
        return request.website.render('website_category_banner_73lines.banner_template', values)

