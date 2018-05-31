from rwslib.rws_requests import ClinicalStudiesRequest
from rwslib.rws_requests import StudySubjectsRequest
from rwslib.rws_requests.odm_adapter import SitesMetadataRequest
from rwslib.rws_requests import biostats_gateway
from rwslib.rwsobjects import RWSException
from rwslib import RWSConnection
import configparser

# reading the innovate credentials from the application config files.

config = configparser.ConfigParser()
config.read(r'// path to configuration file')
generic_list = []

# making the connection using the rws connection object 

rws_connection = RWSConnection(domain=config.get('medidata','domain'), username=config.get('medidata','username'),password=config.get('medidata','password'))

class clinical_masters:
    def get_clinical_studies():
        study_data = rws_connection.send_request(ClinicalStudiesRequest())
        return study_data

    def get_studies_list():
        study_data = clinical_masters.get_clinical_studies()
        studies_list = []
        for study_object in study_data:
            studies_list.append(study_object.studyname)
        return studies_list            

    def get_site_data():
        final_list = clinical_masters.get_studies_list()
        for final in final_list:
            site_object = rws_connection.send_request(SitesMetadataRequest(project_name=final,environment_name='Prod'))
            

    def get_subject_data():
        final_list = clinical_masters.get_studies_list()   
        for final in final_list:
             subject_data = rws_connection.send_request(StudySubjectsRequest(project_name=final, environment_name='Prod'))