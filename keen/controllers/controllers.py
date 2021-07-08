# -*- coding: utf-8 -*-
from odoo import http


class Keen(http.Controller):

    @http.route('/keen/keen/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['keen.teachers']
        return http.request.render('keen.index', {
            'teachers': Teachers.search([])
        })

    # @http.route('/keen/keen/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('keen.listing', {
    #         'root': '/keen/keen',
    #         'objects': http.request.env['keen.keen'].search([]),
    #     })

    # @http.route('/keen/keen/objects/<model("keen.keen"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('keen.object', {
    #         'object': obj
    #     })
