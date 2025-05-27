from hashlib import md5
from requests import get
from datetime import datetime

class RestMarvel:
    timestamp = datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    pub_key = '45e22497192f866c8c970665ace91bd0'
    priv_key = '817ff8ab3675acf7321f0a4f6659d80d6849c325'

    def hash_params(self):
        hash_md5 = md5()
        hash_md5.update(f'{self.timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params = hash_md5.hexdigest()
        hashed_params = hash_md5.hexdigest()
        return hashed_params
    
    def get_heroes(self):
        params = {'ts':self.timestamp,'apikey':self.pub_key,'hash':self.hash_params()}
        result = get('https://gateway.marvel.com:443/v1/public/characters',
                    params=params)

        data = result.json()
        print(data)
        print(data["status"])

rest=RestMarvel()
rest.get_heroes()