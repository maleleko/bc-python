class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gold_card_points = 0
        self.email = email
        self.age = age
        self.is_rewards_member = False

    def display_info(self): 
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}") 
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member? - {self.is_rewards_member}")
        print(f"Reward Points: {self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
        else:
            print("You're already a Rewards Member, thank you!")
        # self.gold_card_points = 200
        if self.gold_card_points == 0:
            self.gold_card_points = 200
            # return self.gold_card_points
        return self

    def spentpoints(self, amount):
        if self.gold_card_points < amount:
            print("Not enough points!")
            # return amount
        else: 
            self.gold_card_points -= amount
        return self

user_one = User("Maleko", "Osby", "osbydm18@gmail.com", 26)

# user_one.enroll()
# user_one.spentpoints(50)
# user_one.display_info()
# # print(f"Reward points after spending: {user_one.gold_card_points}")
# user_one.enroll()

#chaining the above
user_one.enroll().spentpoints(50).display_info().enroll()

print(" ")

user_two = User("koh", "ethereal", "fpsdemigod@gmail.com", 66)
# user_two.enroll()
# user_two.spentpoints(80)
# user_two.display_info()

#chaining
user_two.enroll().spentpoints(80).display_info()
# # print(user_two.gold_card_points)

print(" ")

user_three = User("ced", "gal", "cedgal94@gmail.com", 27)
# user_three.enroll()
# user_three.gold_card_points = 40
# user_three.display_info()
# user_three.spentpoints(50)

#chaining 
user_three.gold_card_points = 40
user_three.enroll().display_info().spentpoints(50)