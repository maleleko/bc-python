#nesting
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