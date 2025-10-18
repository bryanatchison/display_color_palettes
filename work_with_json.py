import json

# try:
    # with open('test2.txt', 'r') as file:
        # data = json.loads(file)
        # print(data)
    
# except FileNotFoundError:
#    print("The file was not found.")
# except json.JSONDecodeError:
#    print("Error decoding JSON.")

input_data = {
    "palette_colors": 
    [
        ["rgb(13, 59, 102)", "0D3B66"], 
        ["rgb(250, 240, 202)", "FAF0CA"], 
        ["rgb(244, 211, 94)", "F4D35E"], 
        ["rgb(238, 150, 75)", "EE964B"], 
        ["rgb(249, 87, 56)", "F95738"]
    ], 
    "palette_name": "My new palette"
    }

output_data = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

#  output_data = json.loads(input_data)
print(output_data)

