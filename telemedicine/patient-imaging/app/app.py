from flask import Flask, jsonify, request,render_template
import pydicom
import requests
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
headers = {  'Authorization': 'Basic b3J0aGFuYzpvcnRoYW5j' }

ORTHANC_URL = 'http://orthanc:8042'
ORTHANC_SSL = False

@app.route('/patient_imaging/health', methods=['GET'])
def get_health():
    return("ok")

@app.route('/patient_imaging/getAllPatients', methods=['GET'])
def get_all_patient_imaging():
    if ORTHANC_SSL == True:
      response = requests.get(f'{ORTHANC_URL}/patients', headers=headers, verify='rootCA.pem')
    else:
      response = requests.get(f'{ORTHANC_URL}/patients', headers=headers) 

    response_decoded=response.content.decode('utf-8')
    data=json.loads(response_decoded)
    return json.dumps(data)


@app.route('/patient_imaging/getPatientImagingInfo/<string:patient_id>', methods=['GET'])
def get_patient_imaging(patient_id):
    if ORTHANC_SSL == True:
        patient = requests.get(f'{ORTHANC_URL}/patients/{patient_id}',headers=headers,verify='rootCA.pem')
    else:
         patient = requests.get(f'{ORTHANC_URL}/patients/{patient_id}',headers=headers)
    return patient.json()

@app.route('/patient_imaging/getPatientStudyInfo/<string:study_id>', methods=['GET'])
def get_patient_study(study_id):
    if ORTHANC_SSL == True:
        study = requests.get(f'{ORTHANC_URL}/studies/{study_id}',headers=headers,verify='rootCA.pem')
    else:
        study = requests.get(f'{ORTHANC_URL}/studies/{study_id}',headers=headers)

    return study.json()

@app.route('/instances', methods=['POST'])
def post_instances():
    url = 'http://orthanc:8042/instances'
    headers = {'Content-Type': 'application/dicom'}
    data = request.get_data()
    if ORTHANC_SSL==True:
        response = requests.post(url, headers=headers, data=data, verify=False)
    else:
         response = requests.post(url, headers=headers, data=data)

    return response.content, response.status_code


@app.route('/patient_imaging/deletePatientData/<string:patient_id>', methods=['DELETE'])
def delete_patient_imaging(patient_id):
   if ORTHANC_SSL==True:
       response=requests.delete(f'{ORTHANC_URL}/patients/{patient_id}',headers=headers,verify='rootCA.pem')
   else:
       response=requests.delete(f'{ORTHANC_URL}/patients/{patient_id}',headers=headers)
   return response.json()



if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
