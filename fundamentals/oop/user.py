class User: 
    def __init__(self,first_name,last_name,email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_members = False
        self.gold_card_points = 0


    def display_info(self):
        print(f'first_name {self.first_name}')
        print(f'last_name {self.last_name}')
        print(f'email {self.email}')
        print(f'age {self.age}')

    def enroll(self):
        self.is_rewards_members = False
        self.gold_card_points = 200
        if self.is_rewards_members:
            print('already a member')
            return True

    def spend_points(self,amount):
        self.gold_card_points -= amount #Add if statement to check points balance, if insufficient points, return (insufficent points) if self.gold_cardpints < amount print

my_user = User('Mikey', 'The_TA', 'michael@codingdojo.com','85')
my_user.display_info()
my_user.enroll()

user_2 = User('Jerry','Jordan','jj@noemail.com','102')

user_2.spend_points(50)







