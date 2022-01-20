# -*- coding: utf-8 -*-
# from odoo import http


# class OdooModule(http.Controller):
#     @http.route('/odoo_module/odoo_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_module/odoo_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_module.listing', {
#             'root': '/odoo_module/odoo_module',
#             'objects': http.request.env['odoo_module.odoo_module'].search([]),
#         })

#     @http.route('/odoo_module/odoo_module/objects/<model("odoo_module.odoo_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_module.object', {
#             'object': obj
#         })
