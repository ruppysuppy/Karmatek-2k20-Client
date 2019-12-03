####################################################
# LOCAL IMPORT #####################################
####################################################

from Data_Gen import generate_data

####################################################
# IMPORTS (FROM LIBRARY) ###########################
####################################################

import requests

####################################################
# DECALRING NECESSARY VARIABLES ####################
####################################################

url = ' http://127.0.0.1:5000/api'
header = {}


####################################################
# USER DETAILS #####################################
####################################################

# DEFAULT ACCEPTED VALUES FOR USERNAME AND PASSWORD
# username: 'admin', 
# password: 'supersecretpassword'

user = input("Enter user-name: ")
password = input("Enter password: ")

header['user'] = user
header['password'] = password

####################################################
# DATA FETCH & EXCEL SHEET CREATION ################
####################################################

choice = input("Do you want to generate the paticipation details? (y/n): ").lower()

if (choice == 'y'):
        try:
                r = requests.get(url, headers=header)
                if (r.status_code == 200):
                        data = r.json()
                        generate_data(data)
                        print('Task Complete!')
                else:
                        raise RuntimeError

        except requests.exceptions.ConnectionError:
                print('Connection Error!'.upper())
                print('Closing Program...'.upper())

        except:
                print("Error!".upper())
                print('Closing Program...'.upper())
                exit()

####################################################
# EMAIL RESEND REQUEST #############################
####################################################

choice = input("Do you want to resend mails to the unconfirmed participants? (y/n): ").lower()

if (choice == 'y'):
        try:
                r = requests.post(url, headers=header)
                if (r.status_code == 200):
                        if (len(r.json()) > 0):
                                print('Task Complete!')
                        else:
                                print('No unconfirmed user found.')
                else:
                        raise RuntimeError
        
        except requests.exceptions.ConnectionError:
                print('Connection Error!'.upper())
                print('Closing Program...'.upper())

        except:
                print("Error!".upper())
                print('Closing Program...'.upper())
                exit()