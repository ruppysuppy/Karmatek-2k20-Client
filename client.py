####################################################
# LOCAL IMPORT #####################################
####################################################

from Data_Gen import generate_data

####################################################
# IMPORTS (FROM LIBRARY) ###########################
####################################################

import requests

####################################################
# DATA FETCH & EXCEL SHEET CREATION ################
####################################################

url = ' http://127.0.0.1:5000/api'
header = {'user': 'admin',
        'password': 'supersecretpassword'}

r = requests.get(url, headers=header)

data = r.json()

generate_data(data)