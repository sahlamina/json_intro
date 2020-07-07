import requests
import json

# exercise is to fetch data by key value pairs within dictionaries

key_value_pc = requests.get("https://api.postcodes.io/postcodes/se120nb")
data = key_value_pc.json()
class Dict_Parse:
    # create a function to return the above values (k/v)
    def post_code_kv(self, data):
        for key, value in data.items():
            if type(value) is dict:
                self.post_code_kv(value)
            else:
                print(key, value)

            print(key, value)
# create a class and move the code block inside the class
postcodeparse = Dict_Parse()
postcodeparse.post_code_kv(data)