# Total number of cars is 100
cars = 100
# In Each car there is a capicity of 4 people
space_in_a_car = 4.0
# There are total 30 drivers
drivers = 30
# There are total 90 Passengers
passengers = 90
# So total 30 drivers and 100 cars, then 70 cars are not driven
cars_not_driven = cars - drivers
# Cars driven is 30 cars as 30 drivers are there
cars_driven = drivers
# Total 120 Carpool capacity is there - 30 * 4 = 120
carpool_capacity = cars_driven * space_in_a_car
# Average Passengers per car is 90 / 30 -> 3.0
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today")
print("We have",passengers,"to carpool today.")
print("WE need to put about",average_passengers_per_car,"in each car.")