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

try:
        r = requests.get(url, headers=header)
        data = r.json()
        generate_data(data)

except requests.exceptions.ConnectionError:
        print('Connection Error!'.upper())
        print('Closing Program...'.upper())

except:
        print("Error!".upper())
        print('Closing Program...'.upper())
