# -*- coding: utf-8 -*-
# from odoo import http


# class MyTheme(http.Controller):
#     @http.route('/my__theme/my__theme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my__theme/my__theme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my__theme.listing', {
#             'root': '/my__theme/my__theme',
#             'objects': http.request.env['my__theme.my__theme'].search([]),
#         })

#     @http.route('/my__theme/my__theme/objects/<model("my__theme.my__theme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my__theme.object', {
#             'object': obj
#         })
