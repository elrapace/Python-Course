import json

#ES 1
g_data = {"key1" : "value1", "key2" : "value2"}
g_result = json.dumps(g_data)
print(f'JSON: {g_result}')

#ES 2
g_sampleJson = """{"key1": "value1", "key2": "value2"}"""
g_result = json.loads(g_sampleJson)
print(g_result['key2'])

#ES 3
g_result = json.dumps(g_data, indent=2, separators=(',',' = '))
print(g_result)

#ES 4
g_sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
g_result = json.dumps(g_sampleJson, indent=4, sort_keys=True)
print(g_result)

#ES 5
g_sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
        }
      }
   }
}"""
g_result = json.loads(g_sampleJson)
g_salary = g_result['company']['employee']['payble']['salary']
print(f'SALARY: {g_salary}')

#Es 6
from json import JSONEncoder
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
vehicleJson = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
print(vehicleJson)