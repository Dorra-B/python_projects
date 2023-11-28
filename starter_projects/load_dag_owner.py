import json

# Step 1: Read the JSON File
with open('/Users/elboukdo/Documents/labEssays/python/PythonProjects/30 Great Projects udemy/python_projects/starter_projects/team_config.json', 'r') as file:
    conf = json.load(file)

print(conf)  # This will print the Python dictionary loaded from the JSON file
print(type(conf))

# To access a specific variable (e.g., 'owner' from your previous example)
# owner_value = conf.get('dag_owner', None)
# print(owner_value)  # This will print the value of 'owner' if it exists

# dag = ""

# if not(dag):
#     print("aaaaa")
# else:
#     print("bbbbbbbb")