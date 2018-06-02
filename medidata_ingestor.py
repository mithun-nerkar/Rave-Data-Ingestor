from rwslib.rws_requests import ClinicalStudiesRequest
from rwslib.rws_requests import StudySubjectsRequest
from rwslib.rws_requests.odm_adapter import *
from rwslib.rws_requests.biostats_gateway import *
from rwslib.rwsobjects import RWSException
from rwslib import RWSConnection
import configparser
from rwslib.extras.audit_event.parser import parse

# reading the innovate credentials from the application config files.

config = configparser.ConfigParser()
config.read(r'F:\Codebase\Rave-Data-Ingestor\applicationconfig.ini')
generic_list = []

# making the connection using the rws connection object 

rws_connection = RWSConnection(domain=config.get('medidata','domain'), username=config.get('medidata','username'),password=config.get('medidata','password'))
study_list = []

# maintaining the generic list for all the studies in the CRO
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
                
    def get_subject_data(study_list = []):   
        for final in study_list:
             subject_data = rws_connection.send_request(StudySubjectsRequest(project_name=final, environment_name='Prod')) 

class odm_service_requests:
    def audit_record_request(study_list =  [] ):
        for final in study_list:
            audit = rws_connection.send_request(AuditRecordsRequest(project_name= final,environment_name='Prod',startid=1,per_page=100))  

    def version_folder_request(study_list =  []):
        for final in study_list:
            version_data = rws_connection.send_request(VersionFoldersRequest(project_name=final,environment_name="Prod"))

    def signature_definations_request(study_list =  []):
        for final in study_list:
            signature_data = rws_connection.send_request(SignatureDefinitionsRequest(final))

    def get_site_data(study_list = []):
        for final in study_list:
            site_object = rws_connection.send_request(SitesMetadataRequest(project_name=final,environment_name='Prod'))

class biostat_adapter_requests:
    def cv_metadata_request(study_list = []):
        for final in study_list:
            cv_data = rws_connection.send_request(CVMetaDataRequest(project_name= final ,environment_name= 'Prod', rawsuffix= 'RAW'))

    def form_data_request(study_list =[]):
        for  final in  study_list:
             form_data = rws_connection.send_request(FormDataRequest(project_name =final,environment_name="Prod",dataset_type="REGULAR",form_oid="",dataset_format="csv"))  

    def metadata_request():
        all_metadata = rws_connection.send_request(MetaDataRequest(dataset_format=".csv"))     

    def project_metadata_request(study_list = []):
        for final in study_list:
            project_metadata_request = rws_connection.send_request(ProjectMetaDataRequest(project_name= final, dataset_format="csv"))

    def comments_data_request(study_list = []):
        for final in study_list:
            comments_data = rws_connection.send_request(CommentDataRequest(project_name= final, environment_name=config.get('medidata','environment')))  

    def protocol_deviation(study_list=[]):
        for final in study_list:
            protocol_data = rws_connection.send_request(ProtocolDeviationsRequest(project_name= final , environment_name= config.get('medidata','environment')))

    def data_dictionaries_request(study_list = []):
        for final in study_list:
            data_dictionaries = rws_connection.send_request(DataDictionariesRequest(project_name=final , environment_name= config.get('medidata','environment')))            
                          