import requests
import json

#
# user = requests.get('https://jsonplaceholder.typicode.com/users/5')
# print(type(user))


# name = {'name': 'Vader'}
#
# n_json=json.dumps(name)
# print(type(n_json))
# l_json=json.loads(n_json)
# print(type(l_json))
#
# _json = json.dumps(name)
# print(type(_json))
# print(_json)
# _dict = json.loads(_json.encode())
# print(_dict)

# with open("first_json.json", 'w') as file:
#     name=json.dumps(name, indent=4)
#     file.write(name)
# d=''
# with open("first_json.json", 'r') as file:
#     d=json.load(file)
#     print(d)
# from rest_framework.renderers import JSONRenderer

# class A:
#     def __init__(self, name, username, email):
#         self.name = name
#         self.username = username
#         self.email = email
#
#     def get_name(self):
#         return self.name
#
#
# user = requests.get('https://jsonplaceholder.typicode.com/users/1')
# a1 = user.json()
# a = A(a1['name'], a1['username'], a1['email'])
#
# res=json.dumps(a.__dict__)
# content = JSONRenderer().render(res.__dict__)
# print(content)

# d = {'id': 1, 'name': 'Johan'}
# _json=json.dumps(d)
# print(type(_json))

# a = {"A", "B", "C"}
# b = {"C", "D", "E"}
# print(type(a))
# print(a | b)
# print(a & b)
# print(a ^ b)
# print(a - b)
