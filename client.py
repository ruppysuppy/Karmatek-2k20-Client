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
# USER DETAILS + VALIDATION ########################
####################################################

# DEFAULT ACCEPTED VALUES FOR USERNAME AND PASSWORD
# username: 'admin', 
# password: 'password'

user = input("Enter user-name: ")
password = input("Enter password: ")

header['user'] = user
header['password'] = password

try:
        r = requests.patch(url, headers=header)

        if (r.json()["status"] == "Accepted"):
                print('Access Granted...')
        else:
                print("Access Denied. Closing program...")
                exit()

except:
        print("Connection Error!")
        print("Unable to connect to server. Make sure Karmatek Site is running in case of local server, otherwise, check the url variable.")
        print("Closing program...")
        exit()

####################################################
# DATA FETCH & EXCEL SHEET CREATION ################
####################################################

def data_gen():
        choice = input("Generate the paticipation details? (y/n): ").lower()

        if (choice == 'y'):
                try:
                        r = requests.get(url, headers=header)
                        if (r.status_code == 200):
                                data = r.json()
                                if (len(data[0]) and len(data[1])):
                                        generate_data(data)
                                        print('Task Complete!')
                                else:
                                        print("Participants hasn't registered for any event")
                        else:
                                raise RuntimeError

                except requests.exceptions.ConnectionError:
                        print('Connection Error!'.upper())
                        print('Closing Program...'.upper())
                        exit()

                except:
                        print("Some Error has occoured!".upper())

####################################################
# EMAIL RESEND REQUEST #############################
####################################################

def email_resend():
        choice = input("Are you sure you want to resend mails to the unconfirmed participants? (y/n): ").lower()

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
                        exit()

                except:
                        print("Some Error has occoured!".upper())

####################################################
# UPDATE ADMIN DETAILS REQUEST ######################
####################################################

def update_admin():
        choice = input("Are you sure you want to update admin details? (y/n): ").lower()

        if (choice == 'y'):
                header_update = {}

                user_confirm = input("Enter user-name for re-confirmation: ")
                password_confirm = input("Enter password for re-confirmation: ")

                header_update['user'] = user_confirm
                header_update['password'] = password_confirm

                r = requests.patch(url, headers=header_update)

                if (r.json()["status"] == "Accepted"):
                        print('Access Granted...')
                else:
                        print("Access Denied. Check the username and password")
                        return

                header_update['user_new'] = input('Enter the new username (Leave blank for no change): ')

                if (header_update['user_new'] == ""):
                        header_update['user_new'] = None
                
                header_update['password_new'] = input('Enter the new password (Leave blank for no change): ')

                if (header_update['password_new'] == ""):
                        header_update['password_new'] = None

                r = requests.put(url, headers=header_update)
                
                if (r.status_code == 200):
                        if (header_update['user_new'] != None):
                                header['user'] = header_update['user_new']
                        if (header_update['password_new'] != None):
                                header['password'] = header_update['password_new']
                        print('Task Complete!')
                else:
                        print('Error! Couldn\'t update details')

####################################################
# DRIVER CODE ######################################
####################################################

while True:
        print("\nChoose from the following options:")
        print('(1) Generate Paricipation Data')
        print('(2) Resend emails to the unconfirmed participants')
        print('(3) Update admin detials')
        print('(4) Close program')
        choice = input('Enter your choice: ')

        if (choice == '1'):
                data_gen()
        
        elif (choice == '2'):
                email_resend()

        elif (choice == '3'):
                update_admin()

        elif (choice == '4'):
                print(f'Bye {header["user"]}!')
                print('Have a nice day')
                break

        else:
                print('Sorry could not undertand what you wanted to say')