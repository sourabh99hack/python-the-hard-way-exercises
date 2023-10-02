my_name = 'Sourabh nahatkar'
my_age = 25 # not a lie
my_height = 75 # Inches
my_height_cm = 75 * 2.54 # height in cm
my_weight = 60 # KG's
my_weight_lbs = 60 * 2.2 #Pound
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall and in CM it is {my_height_cm} cm.")
print(f"He's {my_weight_lbs} KG's heavy.")
print("Actually that's not too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His Teeth are usually {my_teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = my_age + my_height + my_weight_lbs
print(f"If I add {my_age}, {my_height} and {my_weight_lbs} I get {total}")