#JSON stand for Javascript Object Notation

import json

json_content_python = {"one":1, "two":2, "three":3}

print(type(json_content_python))
print(json_content_python)
json_not_python = json.dumps(json_content_python)

print(type(json_not_python))
print(json_not_python)

with open("new_json_file_numbers.json","w") as json_file:
    json.dump(json_content_python, json_file)

    #to get it in we use .dump and to get it out we use .load

with open("new_json_file_numbers.json","w") as json_file:
    json.load(json_content_python, json_file)


print(type(numbers))
Print(numbers["one"])
print(numbers["three"])

class RatesParser:
    def __init__(self, rates_file):
        rates_info = self._open_file(rates_file)
        self.base = rates_info["base"]
        self.date = rates_info["date"]
        self.rates = rates_info["rates"]
        self.aud = self.rates["AUD"]
        self.gbp = self.rates["GBP"]
    def _open_file(self, file):
        with open(file) as rates:
            return json.load(rates)
rates_exchange = RatesParser("new_json_file.json")
print(rates_exchange.gbp)
print(rates_exchange.rates)