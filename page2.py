#Use of this page is optional. If you use code here, make sure either import page2 or from page2 import * appear on your main.py page.

print("you have been given madlib #2!")

'''
"good " + timeofday1 + name + "! you look postively " + adjective1 + " today. today's meal will have" + number1 + "courses. we will be serving " + food1 + " with a side of " + food2 + " and a " + food3 + " sauce. for the dessert, we will be serving " + food4 + " with " + food5 + ". enjoy your meal, " + name + "."
'''

timeofday1 = input("enter a time of day (morning, evening, afternoon): ")
name = input("what's your name? ")
adjective1 = input("enter an adjective: ")
number1 = input("enter a number: ")
food1 = input("enter a food: ")
food2 = input("enter another food: ")
food3 = input("enter yet another food: ")
food4 = input("enter a fourth food: ")
food5 = input("enter your final food: ")

story2 = "good " + timeofday1 + " " + name + "! you look postively " + adjective1 + " today. today's meal will have " + number1 + " courses. we will be serving " + food1 + " with a side of " + food2 + " and a " + food3 + " sauce. for the dessert, we will be serving " + food4 + " with " + food5 + ". enjoy your meal, " + name + "."

print(story2)