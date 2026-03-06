# ==========================================
# TUGAS PBO - CLASS RESTAURANT DAN USER
# ==========================================

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
       self.restaurant_name = restaurant_name
       self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_type} food")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now!")

restaurant = Restaurant('Ramen','Japanese')

print(f"The restaurant name is, {restaurant.restaurant_name}.")
print(f"This restaurant provides, {restaurant.cuisine_type}food.")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()

a_restaurant = Restaurant ('Pizza','Italian')

print(f"The restaurant name is, {a_restaurant.restaurant_name}.")
print(f"This restaurant provides, {a_restaurant.cuisine_type}food.")
a_restaurant.describe_restaurant()
a_restaurant.open_restaurant()
print()

b_restaurant = Restaurant ('Bibimbap','Korean')
print(f"The restaurant name is, {b_restaurant.restaurant_name}.")
print(f"This restaurant provides, {b_restaurant.cuisine_type}food.")
b_restaurant.describe_restaurant()
b_restaurant.open_restaurant()
print()

class User:
    def __init__(self, first_name, last_name, city):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city

    def describe_user(self):
        print(f"User full name is {self.first_name} {self.last_name}.")
        print(f"This user lives in {self.city}.")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome back!")
        
user = User('Hanifah', 'Afrilia', 'PekanBaru')

print(f"The user first name is {user.first_name}.")
print(f"The user last name is {user.last_name}.")
print(f"The user lives in {user.city}.")
user.describe_user()
user.greet_user()
print()

a_user = User('Aisyah', 'Putri', 'Jakarta')

print(f"The user first name is {a_user.first_name}.")
print(f"The user last name is {a_user.last_name}.")
print(f"The user lives in {a_user.city}.")
a_user.describe_user()
a_user.greet_user()
print()

b_user = User('Rizky', 'Saputra', 'Bandung')

print(f"The user first name is {b_user.first_name}.")
print(f"The user last name is {b_user.last_name}.")
print(f"The user lives in {b_user.city}.")
b_user.describe_user()
b_user.greet_user()
print()