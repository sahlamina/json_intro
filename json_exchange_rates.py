# import json
# create a class Exchange_Rates
# with required attributes
# fetch the data from exchange_rates.json
# display the data
# display the type of the data
# method to return the exchange rates
# display exchange rates with specific currencies

import json


# create a class to  begin the process
# class Exchange_Rates:
#     # method which doesnt take any arguments to begin the parse
#     def rates(self):
#         with open("exchange_rates.json", "r") as exchange_files:
#             data = json.load(exchange_files)
#             # for loop to iterate through the exchange rates
#             for e in data:
#                 if e == 'base':
#                     print(data['base'])
#                     print(data)
#
# er = Exchange_Rates
# er.rates()

# method to return the exchange rates
class Exchange_Rates:
    def fetch_exchange_rates(self):
        with open("exchange_rates.json", "r") as jsonfile:
            dataset = json.load(jsonfile)
            # For loop to get all exchange rates
            for key in dataset:
                if key == "rates":
                    print(dataset["rates"])
            currency = input("What currency would you like the exchange rate of, please see list.\n")
            # display exchange rates with specific currencies
            print(dataset["rates"][currency])