import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

"""
DEFAULT KEYWORD
"""
DEFAULT = "default"
"""
DATABASE KEYWORD
"""
DB_SELFLEARNING = "SelfLearning"
"""
COLLECTION KEYWORD
"""

DUHUITEST = "duhuiTest"

CUSTOMER_FAQ = "customerCenter_faq"
CUSTOMER_NOTICE = "customerCenter_notice"

DATALEARNING_DATABACKGROUNDMODEL_INFO = "dataLearning_databackgroundmodelinfo"
DATALEARING_DATATEST_RESULT = "dataLearning_datatestresult"
DATAMODELMANAGEMENT_DATAMODEL_INFO = "dataModelManagement_datamodelinfo"
DATAMODELMANAGEMENT_MODELDATAS_INFO = "dataModelManagement_modeldatasinfo"
    
IMGLEARNING_IMGBACKGROUNDMODEL_INFO = "imgLearning_imgbackgroundmodelinfo"
IMGLEARING_IMGCROP_INFO = "imgLearning_imgcropinfo"
IMGLEARING_TESTIMG_INFO = "imgLearning_testimgsinfo"
IMGMODELMANAGEMENT_IMGMODEL_INFO = "imgModelManagement_imgmodelinfo"
IMGMODELMANAGEMENT_MODELCLASS_INFO = "imgModelManagement_modelclassinfo"
IMGMODELMANAGEMENT_MODELIMGS_INFO = "imgModelManagement_modelimgsinfo"

LOG_DATAMODEL = "log_datamodellog"
LOG_DATAREPORT = "log_datareportlog"
LOG_DATATESTFILE = "log_datatestfilelog"
LOG_IMGREPORT = "log_imgreportlog"
LOG_IMGTRAIN = "log_imgtrainlog"
LOG_LOGIN = "log_loginlog"

MEMBERSHIP_INFO = "membershipPlan_membershipinfo"

PAYMENT = "payment_payment"

TESTREPORT_DATAREPORTINFO = "testReport_datareportinfo"

USER_ACCOUNT = "user_account"

SERVER_LOCAL_PATH = 'input your path'


def getMessageResponse(custom_code):
    return {
        #success messages
        '200': {"code":"200","message":"successfully get."},
        '200_1': {"code":"200","message":"successfully save."},
        '200_2': {"code": "200", "message": "successfully update."},
        '200_3': {"code": "200", "message": "successfully delete."},


        #not found related messages
        '404': {"code": "400", "message": "Function not found."},

        #dataframe related messages
        '500': {"code": "500", "message": "Dataframe is empty."},
        '500_1': {"code": "500", "message": "Dataframe doesn't contains selected field."},
        '500_2': {"code": "500", "message": "Bad type of data delivered."},
        '500_3': {"code": "500", "message": "Error while operation."},

    }.get(custom_code, "this code is not available in our message response directory. Please add it.")