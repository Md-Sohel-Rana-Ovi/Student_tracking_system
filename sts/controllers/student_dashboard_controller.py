# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import json
import logging
import requests

_logger = logging.getLogger(__name__)


class StsDashboard(http.Controller):
    @http.route('/dashboard', auth='public', website=True)
    def dashboard(self, **kw):
        print(kw)
        print(kw)
        print(kw)
        student_info = None
        if kw.get('student_id',False):
            student_info = self.get_student_info(kw['student_id'])
            print(student_info)

        return request.render('sts.student_template_dashboard', {
            "student_info":student_info
        })


    def get_student_info(self, student_id):
        try:
            url = "http://api.diu.edu.bd/api/v1/studentDetails?clientId=kpiApp&clientSecret=r5ty45ehg56fger45tg4o&studentId=" + str(student_id)
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
        # print(kw)
        # print(kw)
        # user = requests.Session()
        student_info = None
        if kw.get('student_id',False):
            student_info = self.get_student_info(kw['student_id'])
            print(student_info)


        return request.render('sts.student_personal_info_template', {
             "student_info":student_info
        })


    def get_student_info(self, student_id):
        try:
            url = "http://api.diu.edu.bd/api/v1/studentDetails?clientId=kpiApp&clientSecret=r5ty45ehg56fger45tg4o&studentId=" + str(student_id)
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
        

    @http.route('/educational/info', auth='public', website=True)
    def educational_info(self, **kw):


        return request.render('sts.student_educational_info_template', {})  

    @http.route('/academic/info', auth='public', website=True)
    def academic_info(self, **kw):


        return request.render('sts.student_academic_info_template', {})      

    @http.route('/registration_and_exam/clearence', auth='public', website=True)
    def registration_and_exam_clearence(self, **kw):


        return request.render('sts.student_registration_and_exam_clearence_template', {})

    @http.route('/financial_and_ledger/info', auth='public', website=True)
    def financial_and_ledger_info(self, **kw):


        return request.render('sts.student_financial_and_ledger_info_template', {})

    @http.route('/waiver_and_scholarship/info', auth='public', website=True)
    def waiver_and_scholarship_info(self, **kw):


        return request.render('sts.student_waiver_and_scholarship_info_template', {})         
    


    @http.route('/extra_curriculam/activity', auth='public', website=True)
    def extra_curriculam_activity(self, **kw):


        return request.render('sts.student_extra_curriculam_activity_template', {}) 

    @http.route('/disciplinary/action', auth='public', website=True)
    def disciplinary_action(self, **kw):


        return request.render('sts.student_disciplinary_action_template', {}) 

    @http.route('/hall/info', auth='public', website=True)
    def hall_info(self, **kw):


        return request.render('sts.student_hall_info_template', {}) 


    @http.route('/laptop/info', auth='public', website=True)
    def laptop_info(self, **kw):


        return request.render('sts.student_laptop_info_template', {}) 
   
    @http.route('/mentoring/system', auth='public', website=True)
    def mentoring_system(self, **kw):


        return request.render('sts.student_mentoring_system_template', {}) 

    @http.route('/alumni/data', auth='public', website=True)
    def alumni_data(self, **kw):


        return request.render('sts.student_alumni_data_template', {}) 
