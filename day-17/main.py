class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0
    def  follow(self, user ):
        user.followers += 1
        self.following+=1

user_1=User("001", "Vishnu")
user_2=User("002", "Alok")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# print("User_1")
# print("User_id: ",user_1.id)
# print("User_name: ",user_1.name)
# print("User_followers: ",user_1.followers)
# print()
# print("User_2")
# print("User_id: ",user_2.id)
# print("User_name: ",user_2.name)
# print("User_followers: ",user_2.followers)








# user_1 = User()
# user_1.id = "001"
# user_1.username = "Vishnu"
#
# print(user_1.id)
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Alok"
# print(user_1.username)
