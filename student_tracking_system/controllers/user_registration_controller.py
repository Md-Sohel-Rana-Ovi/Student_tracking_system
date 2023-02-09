# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http
from odoo.http import request

from odoo.addons.web.controllers.main import ensure_db
from odoo.addons.website.controllers.main import Home


from odoo.addons.portal.controllers.web import \
    Home as home

# _logger = logging.getLogger(__name__)


class StudentTrackingHome(home):

    @http.route()
    def web_login(self, redirect=None, *args, **kw):
        response = super(StudentTrackingHome, self).web_login(redirect=redirect, *args, **kw)

        if not redirect and request.params['login_success']:
            if request.env['res.users'].browse(request.uid).has_group(
                    'base.group_user'):
                redirect = '/dashboard?' + request.httprequest.query_string.decode()
            else:
                if kw.get("redirect"):
                    redirect = kw.get("redirect")
                else:
                    redirect = '/'

            return request.redirect(redirect)
        return response

    def _login_redirect(self, uid, redirect=None):
        # if request.env.user.is_parent:
        #     return '/my/child'
        if redirect:
            return redirect
        return '/dashboard'