#for loops through dictionaries
#dicts are also iterable. when we interate thru a dict, the iterator is each of the KEYS of the dict

my_dict = {
    "name": 'maleko',
    "language": 'python'
}
for each_key in my_dict:
    print(each_key)

#if we want VALUES of our dictionary we want
my_dict = {
    "name": 'maleko',
    "language": 'python'
}
for each_key in my_dict:
    print(my_dict[each_key])

#dicts also have a few additional methods that allow us to iterate through them and have the keys and/or values as the iterator. test these below
capitals = {
    "Washington":"Olympia",
    "California":"Sacramento",
    "Idaho":"Boise",
    "Illinois":"Springfield",
    "Texas":"Austin",
    "Oklahoma":"Oklahoma City",
    "Virginia":"Richmond"
    }
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

