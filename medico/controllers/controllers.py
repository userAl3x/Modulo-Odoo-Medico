# -*- coding: utf-8 -*-
# from odoo import http


# class Medico(http.Controller):
#     @http.route('/medico/medico', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/medico/medico/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('medico.listing', {
#             'root': '/medico/medico',
#             'objects': http.request.env['medico.medico'].search([]),
#         })

#     @http.route('/medico/medico/objects/<model("medico.medico"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('medico.object', {
#             'object': obj
#         })

