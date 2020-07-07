import requests
import json

# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

# print(post_codes_req.json())

json_data = post_codes_req.json()
# storing data from json()
print(type(json_data))  # checking what data type it is
for key in json_data:
    print(key)



# print(post_codes_req.status_code)
# print(post_codes_req.content)
# print(type(post_codes_req.content) # gives us the
# print(post_codes_req.headers)
# print(type(post_codes_req.headers)
# print(post_codes_req.status_code)

# why should we use built-in packages - because we don't have to declare the conditions manually
# we can use if control flow without the == and it works justthe same

#first iteration - manual check
# if post_codes_req.status_code == 200:
#     print(" success ")
# elif post_codes_req.status_code == 400:
#     print(" Sorry page unavailable ")
#
# second iteration
#
# if post_codes_req.status_code:
#     print(" success ")
# elif post_codes_req.status_code:
#     print(" Sorry page unavailable ")

# Third iteration: create the same functionality with OOP - class and a method

# class Status_code:
#     def check_status_code(self):
#         if post_codes_req.status_code:
#             print(" success ")
#         elif post_codes_req.status_code:
#             print(" Sorry page unavailable ")

# sc = Status_code()
# sc.check_status_code()

# class Live_web_status_code(Status_code):
#     pass
# sc = Live_web_status_code()
# sc.check_status_code()