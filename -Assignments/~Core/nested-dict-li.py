
# # 1) Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# #1) Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1][0] = 15
# print(x)

# #2) Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0]["last_name"] = "Bryant" #updated
# print(students)

# #3) In the sports_directory, change 'Messi' to 'Andres'
# sports_directory["soccer"][0] = "Andres" #updated
# print(sports_directory)

# #4) Change the value 20 in z to 30
# z[0]['y'] = 30
# print(z)

# print("___________________________________________")
# print(" ")

# #2) Iterate Through a List of Dictionaries
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name': "Mark", 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]
# def iterateDict(list):
#     for first in students:
#         for key,val in first.items():
#             print(f'{key} - {val}')
# iterateDict(students)

# print("______________________________________________")
# print(" ")

#3) Get Values From a List of Dictionaries
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name': "Mark", 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictfirst(firstname, list):
    print("First Names Below")
    for first in students:
        print(first['first_name'])
iterateDictfirst('first_name', students)

# print(" ")

# def iterateDictlast(lastname, list):
#     print("Last Names Below")
#     for last in students:
#         print(last['last_name'])
# iterateDictlast('last_name', students)

# print("__________________________________________________")
# print(" ")

# #4 Iterate Through a Dictionary with List Values
# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# # hmm = dojo['locations']
# # print(len(hmm))
# # length = dojo
# # for key in dojo.get('locations'):
# #     print(key)
# #LETS GO DEBUGGING AND TINKERING/MESSING AROUND WITH CODE

# def printInfo(some_dict):
#     length = dojo['locations']
#     print(len(length), "LOCATIONS")
#     for places in dojo.get('locations'):
#         print(places)
# printInfo('instructors')

# print(" ")

# def printInfo(some_dict):
#     length2 = dojo['instructors']
#     print(len(length2), "INSTRUCTORS")
#     for teach in dojo.get("instructors"):
#         print(teach)
# printInfo('instructors')