import requests

# OpenSky API endpoint
ENDPOINT = 'https://opensky-network.org/api/states/all'

# Country of choice
COUNTRY = 'New Zealand'

def get_states(endpoint):
    response = requests.get(endpoint)
    response_dict = response.json()
    states = response_dict['states']
    return states

def print_country_states(states, country):
    for aircraft in states:
        if aircraft[2] == country:
            print(aircraft)

states = get_states(ENDPOINT)
print_country_states(states, COUNTRY)