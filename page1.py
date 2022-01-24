#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.

print("you have been given madlib #1!")

'''
According to all known laws
of aviation, there is no way a *ANIMAL1*
should be able to *VERB1*. Its *PLURAL NOUN1* are too *ADJECTIVE1* to get
its *ADJECTIVE2* little *NOUN2* off the ground. The *ANIMAL1*, of course, *PRESENT VERB* anyway, because *ANIMAL1*s don't care what *ANIMAL2*s think is impossible.

'''

animal1 = input("enter an animal: ")
verb1 = input("enter a verb: ")
pluralnoun1 = input("enter a plural noun: ")
adjective1 = input("enter an adjective: ")
adjective2 = input("enter another adjective: ")
noun1 = input("enter a noun: ")
presentverb1 = input("enter a verb in the present tense(eg: jumps, cries): ")
animal2= input("enter an animal: ")

story1 = "According to all known laws of aviation, there is no way a "+ animal1 +" should be able to " +verb1+". Its  " + pluralnoun1 + " are too " + adjective1 +  " to get its " + adjective2 + " little " + noun1 + " off the ground. The " + animal1 + ", of course, " + presentverb1 + " anyway, because " + animal1 + "s don't care what " + animal2 +"s think is impossible."

print(story1)

