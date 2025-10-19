import json

try:
    with open('Coolors Palettes.json', 'r') as file:
        content = file.read()
        data = json.loads(content)
        print(data)
    
except FileNotFoundError:
   print("The file was not found.")
except json.JSONDecodeError:
   print("Error decoding JSON.")
