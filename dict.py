# a = "asia"
# print("Hello World! " + a)

# x = "print"[0] 
# print(x)

# character_job = "pilot"
# character_ride = "plane"
# character_souvenir = "fruits"
# character_pet = "lion"

# print("pirate is the " + character_job + ".")

# print('Roses are red, violets are blue')
# if 10 > 7:
#     print("Ten is greater than seven!")
# if 16 < 42:
#     print("Sixteen is less than forty-two!")
# print("A long time ago in a galaxy far, far away...")

# def greet(name):
#     print("Have a nice day! " + name)

# name = "Hoho-san"
# greet(name)

# class Customers():
#     greeting = "Welcome to the coffee Palace!"
#     pass # to avoid indentationerror
# c_1 = Customers
# c_1.name = "Samirah"
# c_1.beverage = "Iced caffe latte"
# c_1.food = "Cinnamo roll"
# c_1.total = 225

# c_2 = Customers
# c_2.name = "Jerry"
# c_2.beverage = "Caramel macchiato"
# c_2.food = "Glazed doughnut"
# c_2.total = 230

# print(Customers.greeting)
# print(c_1.beverage)
# print(c_2.food)


# #For LOop
# for num in range(3):
#     print("Attempt" , num + 1, (num + 1)* ".")
# for num in range(1, 6):
#     print("Attempt" , num , num * ".")
# for num in range(1, 10 , 2):
#     print("Attempt" , num , num * ".")

# successful = True
# for num in range(3):
#     print("Sugoi")
#     if successful:
#         print("Successful")
#         break       # if no break it will print 3 times

# # Nested for loop
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# for x in "In a String":
#     print(x)

# count = 0
# for x in range(1, 10):
#     if x%2 == 0:
#         count +=1
#         print (x)
# print(f"We have {count } even numbers") # f means formmated string

# class Guest:
#     def __init__(self, first_name, last_name, interest, phone):
#         self.first = first_name
#         self.last = last_name
#         self.interest = interest
#         self.urnum = phone

# person_1 = Guest("Hoho-san", "None", "Anime", 9952665015 )
# person_2 = Guest("Jojo", "Javier", "Anime" , 9078385548)

# print(person_1.interest)

# class Customers:
#     greeting = "Welcome to the coffee Palace!"
#     def __init__(self, name, beverage, Food, Total):
#         self.name = name
#         self.beverage = beverage
#         self.Food = Food
#         self.Total = Total

# customer01 = Customers("Nate", "Espresso", "Pastrami on rye", 220)
# customer02 = Customers("Elaine", "Straberry frappuccino", "Tuna wrap", 270)
# customer03 = Customers("Samirah", "Iced caffe latte", "Cinnamon roll", 225)
# customer04 = Customers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
# customer05 = Customers("Paz", "Iced tea", "Blueberry pancakes", 315)

# print(Customers.greeting)
# print(customer02.name)
# print(customer02.beverage)
# print(customer02.Food)
# print(customer02.Total)
# print(customer04.name)
# print(customer04.beverage)
# print(customer04.Food)
# print(customer04.Total)

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def display(self):
#         print("(parent class/User) Username: ", self.username, "password: ", self.password)

# class Admin (User):
#     def display(self):
#         print("(subclass/Admin) Username: ", self.username, "password: ", self.password)

# a_1 = Admin("Me@123", "12345678")
# u_1 = User("user@123", "87654321")

# a_1.display() # never forget the paranthesis
# u_1.display()

# class Clubmembers:
#     def __init__(self, name , birthday, age, favoriteFood, goal):
#         self.name = name
#         self.birthday = birthday
#         self.age = age
#         self.favoriteFood = favoriteFood
#         self.goal = goal

#     def display(self):
#         print("Name: " , self.name)
#         print("Birthday: ", self.birthday)
#         print("Age: " , self.age)
#         print("Favorite Food: ", self.favoriteFood)
#         print("Goal: ", self.goal)

# class Clubofficer(Clubmembers):
#     def __init__(self, name, birthday, age, favoriteFood, goal, position):
#         self.position = position
#         super().__init__(name, birthday, age, favoriteFood, goal)
#     def display(self):
#         super().display()
#         print("Position: " , self.position)
#         return

# me = Clubofficer("Hoho", "09 - 24 - 2000", 21 , "Takoyaki", "to be a Programmer", "President")
# me.display()
# print(" \n ")
# you = Clubmembers("Hoho", "09 - 24 - 2000", 21 , "Bento", "To be a anime character")
# you.display()



# dictionary = {"name" : "Hoho", "Age" : 21, "gender" : "male"} # dictionary is like warehouse
# print(dictionary)


# flavor = ["vanilla" , "chocolate"  , "starwberry" , "cookies n' cream" , "bubblegum" ] # this is a list
# toppings = ["almonds" , "banana slices" , "chocolate syrup" , "caramel syrup", "white chocolate chips"] 
# # zip to combine to list
# # dict to convert combined list into dictionary
# flavortopping = dict(zip(flavor, toppings))

# print(flavortopping)
# flavortopping["chocolate"] = "blueberries"      # to change the value in dictionary or add one key value pair
# flavortopping.update({"matcha" : "pistachios", "ube" : "mango slices"}) # add two or more key value pair
# print(flavortopping)

# print(flavortopping["ube"]) # to find value using key, should be precise because it may cause keyerror

# check_key = "chocolate"

# if check_key in flavortopping:
#     print("found")
# else:
#     print("no data found")

# print(flavortopping.get("vanilla")) # output its value
# print(flavortopping.get("milk")) # return none cause no "milk " key in the dictionary

# dictionary.pop("name") # to delete key value in the dictionary
# print(dictionary)
# x = dictionary.items()
# y = dictionary.keys()
# z = dictionary.values()
# print(x)
# print(y)
# print(z)

# groceries = {"chicken" : 8, "apple" : 6, "cucumbers" : 3, "milk" : 2, "oranges" : 4}
# groceries.pop("oranges")

# for key, value in groceries.items():
#     print("Key:", key)
#     print("Value:", value)

# for key in groceries.keys():
#     print(key)
# for value in groceries.values():
#     print(value)
# for item in groceries.items(): # if I use value() it will display value like on the previuos one
#     print(item)

# g = {1: {"name": "jojo", "age": 21}, 2: {"name": "hoho","gender" : "male", "nationality": "filipino"}}
# print(g)
# print(g[1])
# print(g[2]["name"])

# g[3] = {} # to add new dictionary or use add two or more key value like on the top

# g[3]["name"] = "asuna" # to add one by one key value in your dictionary, need pa rin nung main dictionary(g)!
# print(g[3])


# # file handling
# # RAWX : R - READ; A - APPEND; W - WRITE; X; CREATE
# a = open("newfile.txt", "x") # if file has been already create then you create again it will cause an error
# from os import read


# a = open("newfile.txt", "w") # it also can create new file
# a.write("Hello World") # look at the file

# a = open("newfile.txt", "r")
# print(a.read())
# a.close()   # always close the file

# a = open("newfile.txt", "a") # it also can create new file
# a.write("\nHello python")
# a = open("newfile.txt", "r")
# print(a.read(5)) # read only first 5 letters in the file

# for x in a: # to read all in the file
#     print(x)

# a.close() 

# import os
# os.remove("myfile.txt") # to delete a file
# if os.path.exist("myfile.txt"):
#     os.remove("myfile.txt")
# else:
#     print("File does not exist!")

#Errors!! fuck bugs
# n = - 5

# if n < 0:
#     raise Exception("No negative numbers allowed!") # raised keyword

# a = "roger"
# assert a == "roger"
# print("------")
# assert a == "ling" # assertion error
# print("------")

# try:
#     print(dfssdsdgsgd)
# except:
#     print("above code has error")

# try:
#     print(dfgadgdsg)
# except NameError:
#     print("You have Name error")
# except IndentationError:
#     print("You have Indention error")
# else:
#     print("end of code")
# finally:
#     print("this code will run even there is a bug on the top")

# import hi
# import hi as nani # as key for alias of the module

# a = nani.customer01

# print(a.name)
# print(a.beverage)
# print(a.Food)
# print(a.Total)
# print(a.greeting)

# a = nani.get_sum(2,4)
# print(a)

# from hi import get_sum # to import single function in a module
# b = get_sum(5, 6) # dont need the .hi

# print(b)

# help("modules") # to show bunch of list of modules
# help("random") 
# print(dir("random")) # dir return list of valid attributes

# from random import randint
# import datetime

# print(int(randint(1, 20)))

# c = datetime.datetime.now()
# d = datetime.datetime(2000, 9, 24)
# print(c)
# print(d)
# print(c.strftime("%B"))


# import statistics

# # # statistics method:
# # # statistics.median()  statistics.variance()      statistics.stdev() => sample population
# # # statistics.mode()    statistics.pvariance()     statistics.pstdev() => total population
# # # statistics.mean()    

# grade = [11,2,3,4,55,56,3,2,46,65,35,7,34,22,55,9]
# variance = round(statistics.pvariance(grade),2)
# mean_grade = statistics.mean(grade)
# median_grade = statistics.median(grade)
# mode_grade = statistics.mode(grade)
# print("Variance: ", variance)
# print("Mean: ", mean_grade)
# print("Median: ", median_grade)
# print("Mode: ", mode_grade)


# import numpy as np
# from scipy import stats as sp

# sample_data = [103,151,176, 188, 146, 184, 175, 112, 115, 163]

# mean = np.mean(sample_data)
# median = np.median (sample_data)
# mode = sp.mode(sample_data)

# var = round(np.var (sample_data, ddof=1),2)
# sdev = round(np.std (sample_data, ddof=1),2)
# Range = np.ptp(sample_data)

# print('Mean:',mean)
# print('Median: ', mode)
# print('Mode: ',median)
# print('Variance:', var)
# print('Standard deviation: ', sdev)
# print('Range: ', Range)

# import pandas as pd

# sample_data = [103,151,176, 188, 146, 184, 175, 112, 115, 163]

# ser = pd.Series(sample_data)
# print(ser)
# sum_stat = ser.describe()
# print(sum_stat)

# from os import pardir
# import pandas as pd

# df = pd.read_csv("population_by_country_2020.csv")

# firstrows = df.head(10)
# lastrows = df.tail(10)
# print(df)
# print(firstrows)
# print(lastrows)

# sel_country = df[df["Country"] == "Philippines"]
# print(sel_country)

# sea = df[df["Country"].isin(["Philippines", "Thailand", "Indonesia", "Myanmar", "Laos", "Vietnam", "Brunei", "Singapore"])]
# # print(sea)

# stat = sea["Population (2020)"].describe()
# rstat = round(stat, 2)

# print(rstat)

# sort_sea = sea.sort_values(by="Population (2020)", ascending=False)
# print(sort_sea)

# import matplotlib.pyplot as plt 
# import statistics as stat


# f_usage = [5, 4, 3, 5, 8, 2, 5, 2, 5, 8, 10, 8, 7, 9, 10,5, 7, 5, 7, 5, 4, 3, 5, 8, 4]

# fig = plt.figure (figsize =(16, 9))

# plt.hist(f_usage, bins = 8 , edgecolor= "black")
# plt.xlabel('Hours')
# plt.ylabel('Frequency')
# plt.title('Friends Social Media Usage', size=14)
# plt.plot([stat.mean(f_usage), stat.mean(f_usage)], [0, 9], linestyle="--", color="r")
# plt.plot([stat.median (f_usage), stat.median (f_usage)], [0, 10], linestyle="--", color="y")
# plt.plot([stat.pstdev (f_usage), stat.pstdev (f_usage)], [0, 9], linestyle="--", color="g")
# plt.plot([stat.mode (f_usage), stat.mode (f_usage)], [0, 9], linestyle="--", color="m")
# plt.plot([stat.variance (f_usage), stat.variance (f_usage)],

# [0, 9], linestyle="--", color="c")

# plt.text(8,8, 'mean', color="r")
# plt.text(8,7.5, 'median', color="y")
# plt.text(8,7, 'mode', color="m")
# plt.text(8,6.5, 'stdev', color="g")
# plt.text(8,6, 'variance', color="c")
# plt.show()

# import matplotlib.pyplot as plt

# country = east_asia['Country'] 
# population = east_asia[ 'Population (2020)']

# fig = plt.figure (figsize = (16, 10))

# plt.barh(country, population)

# plt.title ('2020 Population by Country (East Asia)')

# plt.show()