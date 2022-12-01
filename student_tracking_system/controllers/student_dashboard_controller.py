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
        # print(kw)
        student_info = None
        if kw.get('student_id',False):
            student_info = self.get_student_info(kw['student_id'])

        return request.render('student_tracking_system.student_template_dashboard', {
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
        print(kw)
        student_info = None
        if kw.get('student_id',False):
            student_info = self.get_student_info(kw['student_id'])
            print("**********")
            print("**********")
            print("**********")
            print("**********")
            print(student_info)
            print(student_info)
            print(student_info)
            


        return request.render('student_tracking_system.student_personal_info_template', {
             "student_info":student_info
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
            url = "http://apps.diu.edu.bd:8043/rest/smis/v3/student-basic-info/student/" + str(student_id)
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
        if kw.get('student_id',False):
            student_clearance = self.get_student_clearance(kw['student_id'])
           
        return request.render('student_tracking_system.student_registration_and_exam_clearence_template', {
             "student_clearance":student_clearance
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


        return request.render('student_tracking_system.student_waiver_and_scholarship_info_template', {})         
    


    @http.route('/extra_curriculam/activity', auth='public', website=True)
    def extra_curriculam_activity(self, **kw):


        return request.render('student_tracking_system.student_extra_curriculam_activity_template', {}) 

    @http.route('/disciplinary/action', auth='public', website=True)
    def disciplinary_action(self, **kw):
        # print(kw)
        # student_info = None
        # if kw.get('student_id',False):
        #     student_info = self.get_student_info(kw['student_id'])

        #     print("************")
        #     print(student_info)
        
            
 
        return request.render('student_tracking_system.student_disciplinary_action_template', {
            # "student_info":student_info
        }) 

    # def get_student_info(self, student_id):
    #     try:
    #         url = "http:/rana:8013/student/discipline/status/" + str(student_id)
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


    @http.route('/hall/info', auth='public', website=True)
    def hall_info(self, **kw):
        hall_info = None
        if kw.get('student_id',False):
            hall_info = self.get_student_hall_info(kw['student_id'])


        return request.render('student_tracking_system.student_hall_info_template', {
            "hall_info":hall_info
        }) 

    def get_student_hall_info(self, student_id):
        try:
            url = "http://apps.diu.edu.bd:8043/rest/hall/v1/payment-collection/get-due/student/" + str(student_id)
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
        if kw.get('student_id',False):
            laptop_info = self.get_student_laptop_info(kw['student_id'])


        return request.render('student_tracking_system.student_laptop_info_template', {
            "laptop_info":laptop_info
        }) 

    def get_student_laptop_info(self, student_id):
        try:
            url = "https://pd.daffodilvarsity.edu.bd/student/laptop/status?student_id={}".format(student_id)
            headers = {"Authorization": "Bearer KcMPJ1yGpnULwNPh58l44pjoItC2Ro"}
            # headers = {
            #     "Content-Type": "application/json",
            #     "clientId": "6ea9ab1baa0efb9e19094440c317e21b",
            #     "clientSecret": "bf222fb5-b155-50d5-b8c9-940df99dc580",
            # }
            
            response = requests.get(url=url, headers=headers)
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None          
   
    @http.route('/mentoring/system', auth='public', website=True)
    def mentoring_system(self, **kw):


        return request.render('student_tracking_system.student_mentoring_system_template', {}) 

    @http.route('/alumni/data', auth='public', website=True)
    def alumni_data(self, **kw):


        return request.render('student_tracking_system.student_alumni_data_template', {}) 


    @http.route('/search', auth='public', website=True)
    def search_view(self, **kw):


        return request.render('student_tracking_system.student_student_search_template', {})     


        
