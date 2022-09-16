# what is a dictionary? it is another mutable sequence type that can store any number of Python object. They consist of pairs(called items) of KEYS and their -CORRESPONDING VALUES- youll see the same structre referred to as an associative array/hash in other languages.

#general summary
#a dictionary is an unordered collection of objects
#values are accessed using a key(typically a string)
#can shrink or grow as needed
#the contents of dictionarys can be modified(unlike tuples)
#can be nested
#sequence ops such a slice cannot be used

#KEYS VS INDEXES
#keys are typically strings - Index are always integers
#keys are not in any sort of order. not stored sequentially in memory - indexes are ordered as list and tuple values which are stored
#dictionaries ONLY have keys. NEVER indexes

#dictionaries are enclosed by braces. {}

# #examples


person = {"first": 'maleko', "last": 'osby', "age": 42, "is_skateboarder": True}
hobbies = {} #create an empty dict incase we want to add key values later


                    #adding new key-value pairs
#dictionaries have no .append() method.
person = {"first": 'maleko', "last": 'osby', "age": 42, "is_skateboarder": True}
hobbies["game"] = 'pc gaming'
hobbies["skate"] = 'skateboarding'
hobbies["music"] = 'anything good'

#"first": is a string and "maleko", is a value.
#we created an empty dictionary and added some keys in the square brackets and the values are located on the right side



                    #list syntax
            # my_list[0] = 4
                    #dictionary syntax
            #my_dict["man im tired"] = tired_val


                    #dictionary manipulation
person = {"first": 'maleko', "last": 'osby', "age": 25, "is_skateboarder": True}
#adding a new k,v pair for email to person
person["email"] = 'osbydm18@gmail.com'
#this should now print "email" and 'osbydm18@gmail.com respectively

#we can manipulate an already existing key
person["last"] = 'koh'
print(person)
#"osby" should now be replaced with "koh"

                    #testing for existing key
if "email" not in person:
    person["email"] = "newmail@email.com"
else:
    print("Would you like to replace existing email")



                    #updating/addition on a key value's value would look like
# person["age"] += 1

person = {"first": 'maleko', "last": 'osby', "age": 25, "is_skateboarder": True}
if "email" not in person:
    person["email"] = "newmail@email.com"
else:
    print("Would you like to replace existing email")
person["age"] += 1
print(person)


                    #accessing values
#to do so, use familiar square brackets [] along with the key to obtain the value
#example
print(person["first_name"])
full_name = person["first_name"] + " " + person["last_name"]

                    #removing values
#2 ways, examples below
value_removed = person.pop("last") #access the key. will remove the key and return its value
#or
del person("first") #still access key but deletes the key and wont return anything


                    #multi line syntax
person = {"first": 'maleko', "last": 'osby', "age": 25, "is_skateboarder": True}
#can be written like
person = {
    "first": 'maleko',
    "last": 'osby',
    "age": 25,"is_skateboarder": True
} #this is prob better for readability purposes


                    #common built in functions/methods
#len() gives the total length of the dictionary
#str() produce a string rep
#type() returns the type of the passed var. if passed var is a dict, will return a DICT type

#python disctionary methods
#.clear() - removes all elements from the dict

#.get(key, default=None) - safe way to get a value, if the key might not exist. returns the value for specidied key or -None- (or value you specify) if the key is not in the dict

#.update(pairs_to_update) - add and update multiple key-value pairs at once, by passing in another dictionary of the pairs to update and add



                    #NESTING
#nesting is also allowed in dicts. in other words, dicts may contain lists and tuples as well as other dictionaries. likewise, lists may contain dictionaries. all of these may be many levels deep!

# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}

#accessing values in nested dicts
#to access a value in a nested data structure, how would we access the fist user's last name
print(users[0]["last"])
#how it works. users[0] access the first user in the nested dict. then ["last"] calls on the key value pair of last which is in this case, the value is "lovelace." we will get "Lovelace" as an output.

print(resume_data["skills"][1])
#should print "back-end" maybe an error as well? two options, but i think the former.
print(users[2]["first"])
#this for sure should output "eric"

#i was right