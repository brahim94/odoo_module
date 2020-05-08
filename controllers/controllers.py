# -*- coding: utf-8 -*-
# from odoo import http


# class Secondmodule(http.Controller):
#     @http.route('/secondmodule/secondmodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/secondmodule/secondmodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('secondmodule.listing', {
#             'root': '/secondmodule/secondmodule',
#             'objects': http.request.env['secondmodule.secondmodule'].search([]),
#         })

#     @http.route('/secondmodule/secondmodule/objects/<model("secondmodule.secondmodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('secondmodule.object', {
#             'object': obj
#         })
