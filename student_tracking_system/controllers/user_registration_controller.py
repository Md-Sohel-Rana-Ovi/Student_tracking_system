from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)



# class UserRegistration(http.Controller):
#     @http.route('/', auth='user', website=True, csrf=False)
#     def sbac_user_registration(self, **kw):
#         _logger.info(kw)
#         user_id = request.session.uid
#         user_obj = request.env['res.users'].sudo().browse(user_id)

#         if user_obj.partner_id:
#             return request.redirect('/dashboard')


