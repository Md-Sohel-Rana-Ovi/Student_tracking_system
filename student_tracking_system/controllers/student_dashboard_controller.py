# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import json
import logging
import requests
from odoo import _, fields, http, release
from odoo.http import request, Response
from odoo.models import check_method_name
from odoo.tools.image import image_data_uri
from odoo.tools import misc, config

# from odoo.addons.muk_rest import validators, tools
# from odoo.addons.muk_rest.tools.common import parse_value
# from odoo.addons.muk_utils.tools.json import ResponseEncoder, RecordEncoder

_logger = logging.getLogger(__name__)


class StsDashboard(http.Controller):
    @http.route('/dashboard', auth='public', website=True)
    def dashboard(self, **kw):
        # print(kw)
        student_info = None
        if kw.get('student_id', False):
            student_info = self.get_student_info(kw['student_id'])

        return request.render('student_tracking_system.student_template_dashboard', {
            "student_info": student_info
        })

    def get_student_info(self, student_id):
        try:
            url = "http://api.diu.edu.bd/api/v1/studentDetails?clientId=kpiApp&clientSecret=r5ty45ehg56fger45tg4o&studentId=" + \
                str(student_id)
            headers = {
                "Content-Type": "application/json",
            }
            response = requests.get(url=url, headers=headers)
            if response.status_code == 200 or response.status_code == 201 or response.status_code == 302:
                data = response.json()
                return data
            return None
        except:
            return None


class StsStudentInfo(http.Controller):
    @http.route('/personal/info', auth='public', website=True)
    def pesonal_info(self, **kw):
        print(kw)
        student_info = None
        if kw.get('student_id', False):
            student_info = self.get_student_info(kw['student_id']) 

        return request.render('student_tracking_system.student_personal_info_template', {
            "student_info": student_info
        })

    # def get_student_info(self, student_id):
    #     try:
    #         url = "http://api.diu.edu.bd/api/v1/studentDetails?clientId=kpiApp&clientSecret=r5ty45ehg56fger45tg4o&studentId=" + str(student_id)
    #         headers = {
    #             "Content-Type": "application/json",
    #         }
    #         response = requests.get(url=url, headers=headers)
    #         if response.status_code == 200 or response.status_code == 201 or response.status_code == 302:
    #             data = response.json()
    #             return data
    #         return None
    #     except:
    #         return None

    def get_student_info(self, student_id):
        try:
            url = "http://apps.diu.edu.bd:8043/rest/smis/v3/student-basic-info/student/" + \
                str(student_id)
            headers = {
                "Content-Type": "application/json",
                "clientId": "30a95867787d446e9dd0bb7b06d61c54",
                "clientSecret": "d4b2538a-1398-470c-859e-4fb11ee296c7",
            }
            response = requests.get(url=url, headers=headers)
            if response.status_code == 200 or response.status_code == 201 or response.status_code == 302:
                data = response.json()
                return data
            return None
        except:
            return None

    @http.route('/educational/info', auth='public', website=True)
    def educational_info(self, **kw):

        return request.render('student_tracking_system.student_educational_info_template', {})

    @http.route('/academic/info', auth='public', website=True)
    def academic_info(self, **kw):

        return request.render('student_tracking_system.student_academic_info_template', {})

    @http.route('/academic/info/details', auth='public', website=True)
    def academic_info_detail(self, **kw):

        return request.render('student_tracking_system.academic_info_detail_template', {})

    @http.route('/registration_and_exam/clearence', auth='public', website=True)
    def student_clearance(self, **kw):
        # print(kw)
        student_clearance = None
        student_info = None
        if kw.get('student_id', False):
            student_clearance = self.get_student_clearance(kw['student_id'])
            student_info = self.get_student_info(kw['student_id']) 

        return request.render('student_tracking_system.student_registration_and_exam_clearence_template', {
            "student_clearance": student_clearance,
            "student_info": student_info
        })

    def get_student_clearance(self, student_id):
        try:
            url = "http://apps.diu.edu.bd:8043/rest/smis/v2/student-clearance/student/" + str(student_id)
            headers = {
                "Content-Type": "application/json",
                "clientId": "6ea9ab1baa0efb9e19094440c317e21b",
                "clientSecret": "bf222fb5-b155-50d5-b8c9-940df99dc580",
            }
            response = requests.get(url=url, headers=headers)
            if response.status_code == 200 or response.status_code == 201 or response.status_code == 302:
                data = response.json()
                return data
            return None
        except:
            return None

    @http.route('/financial_and_ledger/info', auth='public', website=True)
    def financial_and_ledger_info(self, **kw):

        return request.render('student_tracking_system.student_financial_and_ledger_info_template', {})

    @http.route('/waiver_and_scholarship/info', auth='public', website=True)
    def waiver_and_scholarship_info(self, **kw):
        print(kw)
        student_waiver_info = None
        student_info = None
        if kw.get('student_id', False):
            student_waiver_info = self.get_student_waiver(kw['student_id'])
            student_info = self.get_student_info(kw['student_id']) 

       
        return request.render('student_tracking_system.student_waiver_and_scholarship_info_template', {
             "student_waiver_info": student_waiver_info,
            "student_info": student_info
        })

    def get_student_waiver(self, student_id):
        try:
            url = "http://empapp.daffodilvarsity.edu.bd/api.student.track/api/Students/GetWaiver/" + str(student_id)
            headers = {
                "Content-Type": "application/json",
                "clientId": "755435CF682C3787927BB3F3EF16A",
                "clientSecret": "m5GQzjsTuR5Z84Al8Z44beA3gcZw6UvH",
            }
            response = requests.get(url=url, headers=headers)
            if response.status_code == 200 or response.status_code == 201 or response.status_code == 302:
                data = response.json()
                print(data)
                return data
            return None
        except:
            return None    

    @http.route('/extra_curriculam/activity', auth='public', website=True)
    def extra_curriculam_activity(self, **kw):
        print(kw)
        extra_curriculam = None
        student_info = None
        if kw.get('student_id',False):
            extra_curriculam = self.get_student_extra_curriculum_info(kw['student_id'])
            student_info = self.get_student_info(kw['student_id'])

        return request.render('student_tracking_system.student_extra_curriculam_activity_template', {
            "extra_curriculam": extra_curriculam,
            "student_info": student_info
        })

    def get_student_extra_curriculum_info(self, student_id):
        try:
            url = "https://pd.daffodilvarsity.edu.bd/student/curriculumn/status" 
            params = {
                "response_type": "token",
                "client_id": "5A5RZahzru8XbzWuaUysc5kKRe5uLL",
                "redirect_uri": "https://pd.daffodilvarsity.edu.bd/",
                "student_id": student_id,
                "Accept" : "*/*"
            }
            
            response = requests.get(url=url, params=params)
            print("======================================================")
            print(response.content)
            print(type(response))
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None

    @http.route('/disciplinary/action', auth='public', website=True)
    def disciplinary_action(self, **kw):
        print(kw)
        disciplinary_info = None
        student_info = None
        if kw.get('student_id',False):
            disciplinary_info = self.get_student_disciplin_info(kw['student_id'])
            student_info = self.get_student_info(kw['student_id'])  

        return request.render('student_tracking_system.student_disciplinary_action_template', {
            "disciplinary_info":disciplinary_info,
            "student_info":student_info
        })

    def get_student_disciplin_info(self, student_id):
        try:
            url = "https://pd.daffodilvarsity.edu.bd/student/discipline/status" 
            params = {
                "response_type": "token",
                "client_id": "5A5RZahzru8XbzWuaUysc5kKRe5uLL",
                "redirect_uri": "https://pd.daffodilvarsity.edu.bd/",
                "student_id": student_id,
                "Accept" : "*/*"
            }
            
            response = requests.get(url=url, params=params)
            print("======================================================")
            print(response.content)
            print(type(response))
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None

    @http.route('/hall/info', auth='public', website=True)
    def hall_info(self, **kw):
        hall_info = None
        student_info = None
        if kw.get('student_id', False):
            hall_info = self.get_student_hall_info(kw['student_id'])
            student_info = self.get_student_info(kw['student_id'])
            
          
        return request.render('student_tracking_system.student_hall_info_template', {
            "hall_info": hall_info,
            "student_info": student_info
        })

    def get_student_hall_info(self, student_id):
        try:
            url = "http://apps.diu.edu.bd:8043/rest/hall/v1/payment-collection/get-due/student/" + \
                str(student_id)
            headers = {
                "Content-Type": "application/json",
                "clientId": "6ea9ab1baa0efb9e19094440c317e21b",
                "clientSecret": "bf222fb5-b155-50d5-b8c9-940df99dc580",
            }
            response = requests.get(url=url, headers=headers)
            if response.status_code == 200 or response.status_code == 201 or response.status_code == 302:
                data = response.json()
                return data
            return None
        except:
            return None

    @http.route('/laptop/info', auth='public', website=True)
    def laptop_info(self, **kw):
        laptop_info = None
        student_info = None
        if kw.get('student_id', False):
            laptop_info = self.get_student_laptop_info(kw['student_id'])
            student_info = self.get_student_info(kw['student_id'])
           
        return request.render('student_tracking_system.student_laptop_info_template', {
            "laptop_info": laptop_info,
            "student_info": student_info
        })

    def get_student_laptop_info(self, student_id):
        try:
              
            url = "https://pd.daffodilvarsity.edu.bd/student/laptop/status"
            params = {
                "response_type": "token",
                "client_id": "5A5RZahzru8XbzWuaUysc5kKRe5uLL",
                "redirect_uri": "https://pd.daffodilvarsity.edu.bd/",
                "student_id": student_id,
                "Accept" : "*/*"
            }
            
            response = requests.get(url=url, params=params)
            print("======================================================")
            print(response.content)
            print(type(response))
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None

   

    @http.route('/mentoring/system', auth='public', website=True)
    def mentoring_system(self, **kw):

        return request.render('student_tracking_system.student_mentoring_system_template', {})

    @http.route('/alumni/data', auth='public', website=True)
    def student_alumni_info(self, **kw):
        print(kw)
        student_alumni_info = None
        student_info = None
        if kw.get('student_id', False):
            student_alumni_info = self.get_student_alumni_info(kw['student_id'])
            student_info = self.get_student_info(kw['student_id']) 

        return request.render('student_tracking_system.student_alumni_data_template', {
            "student_alumni_info": student_alumni_info,
            "student_info": student_info
        })
       
    def get_student_alumni_info(self, student_id):
        try:
            url = "http://empapp.daffodilvarsity.edu.bd/api.student.track/api/Students/" + str(student_id)
            headers = {
                "Content-Type": "application/json",
                "clientId": "755435CF682C3787927BB3F3EF16A",
                "clientSecret": "m5GQzjsTuR5Z84Al8Z44beA3gcZw6UvH",
            }
            response = requests.get(url=url, headers=headers)
            if response.status_code == 200 or response.status_code == 201 or response.status_code == 302:
                data = response.json()
                print(data)
                return data
            return None
        except:
            return None 

    @http.route('/search', auth='public', website=True)
    def search_view(self, **kw):

        return request.render('student_tracking_system.student_student_search_template', {})
