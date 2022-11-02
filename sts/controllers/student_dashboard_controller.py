# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import json
import logging

_logger = logging.getLogger(__name__)


class StsDashboard(http.Controller):
    @http.route('/dashboard', auth='public', website=True)
    def dashboard(self, **kw):


        return request.render('sts.student_template_dashboard', {})



class PersonalInfo(http.Controller):
    @http.route('/personal/info', auth='public', website=True)
    def dashboard(self, **kw):


        return request.render('sts.student_personal_info_template', {})
         


