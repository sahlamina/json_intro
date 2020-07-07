# python json module Javascript object notation
# why - we create an object

import json

# ENCODING from dictionary and writing to jsonfile

car_data = {"name": "tesla", "engine": "electric"} # dictionary
print(car_data)

print(type(car_data))
# checking the type of dictionary

#print(car_data)

car_data_json_string = json.dumps(car_data) #dumps
# json.dumps changes python dict to json str

print(type(car_data_json_string)) # json format changed the type to a string

#let's create a jsonfile with writing permission
with open("new_json_file.json", "w") as jsonfile:
    # enter the name of the file", permission type write 'w'
    # Encoding and creating and writing into json_file

    json.dump(car_data, jsonfile) # using dump as opposed to dumps. This method takes 2 args
    # 1st is the dictionary, 2nd is the file_type jsonfile on this occasion

with open("new_json_file.json") as jsonfile: # Decoding
# Reading from the file we just created
    car = json.load(jsonfile) # storing data from file to car variable
    print(type(car))    # checking the type of data again
    print(car["name"])    # to get the value stored in key called name
    print(car["engine"])  # to get the value of second key value pair

# we have decoded our file new_json.json that we created earlier
# we have used dumps(), dump() and load() methods
