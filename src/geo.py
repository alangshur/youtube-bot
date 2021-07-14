import requests

class IPGeolocation:

    def __init__(self, 
                 api_address: str='https://api.ipgeolocation.io/ipgeo',
                 api_key='6fada961a9334668872162dfc78639c5'):

        self.api_address = api_address
        self.api_key = api_key

    def get_ip_geolocation(self, ip_address):

        response = requests.get(
            url=self.api_address, 
            params={
                'apiKey': self.api_key,
                'ip': ip_address
            }
        )

        response = response.json()
        return response