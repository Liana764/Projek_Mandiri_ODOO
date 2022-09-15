# -*- coding: utf-8 -*-
# from odoo import http


# class Liana(http.Controller):
#     @http.route('/liana/liana', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/liana/liana/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('liana.listing', {
#             'root': '/liana/liana',
#             'objects': http.request.env['liana.liana'].search([]),
#         })

#     @http.route('/liana/liana/objects/<model("liana.liana"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('liana.object', {
#             'object': obj
#         })
