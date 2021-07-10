# -*- coding: utf-8 -*-
# from odoo import http


# class KeenTheme(http.Controller):
#     @http.route('/keen_theme/keen_theme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/keen_theme/keen_theme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('keen_theme.listing', {
#             'root': '/keen_theme/keen_theme',
#             'objects': http.request.env['keen_theme.keen_theme'].search([]),
#         })

#     @http.route('/keen_theme/keen_theme/objects/<model("keen_theme.keen_theme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('keen_theme.object', {
#             'object': obj
#         })
