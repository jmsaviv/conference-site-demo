from registrant.models import Registrant
import json

try:
    with open('registrant/registrant_data_full.json', 'r') as registrantData:
        dataObject = json.load(registrantData)

    for registrant in dataObject['registrants']:
        data = Registrant(**registrant)
        data.save()
        print("Added registrant: ", data)

except IOError:
    print ('File not found')