import requests

# desired Endpoint(s)
DATA_GOVT = 'https://catalogue.data.govt.nz/api/action/package_show'

# desired Dataset(s)
PUBLIC_SECTOR_WEBSITES = 'new-zealand-public-sector-websites'
WGTN_CC_DEFENCE = 'wellington-city-civil-defence-centres'

def get_database(endpoint, package_id):
    query_params = {'id': package_id}
    response = requests.get(endpoint, params=query_params)
    return response

def print_database(response):
    response_dict = response.json()
    result = response_dict['result']
    print(result)

response1 = get_database(DATA_GOVT, PUBLIC_SECTOR_WEBSITES)
print_database(response1)

response2 = get_database(DATA_GOVT, WGTN_CC_DEFENCE)
print_database(response2)

