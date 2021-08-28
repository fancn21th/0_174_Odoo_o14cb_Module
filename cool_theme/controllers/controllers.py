# -*- coding: utf-8 -*-
# from odoo import http


# class CoolTheme(http.Controller):
#     @http.route('/cool_theme/cool_theme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cool_theme/cool_theme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cool_theme.listing', {
#             'root': '/cool_theme/cool_theme',
#             'objects': http.request.env['cool_theme.cool_theme'].search([]),
#         })

#     @http.route('/cool_theme/cool_theme/objects/<model("cool_theme.cool_theme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cool_theme.object', {
#             'object': obj
#         })
