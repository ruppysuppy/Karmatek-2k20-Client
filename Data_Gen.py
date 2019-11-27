####################################################
# IMPORTS (FROM LIBRARY) ###########################
####################################################

from pandas import DataFrame

####################################################
# FUNCTION TO GENERATE THE PARTICIPATION DATA ######
####################################################

def generate_data(data):
    users = list(data[0])
    events = list(data[1])

    data = []

    for user in users:
        for event in events:
            if (user['Id'] == event['Id']):
                temp = dict(user)
                temp['Event'] = event['Event']
                data.append(temp)

    df = DataFrame(data)

    df.to_excel('Paticipation_Data.xlsx', index=False)
