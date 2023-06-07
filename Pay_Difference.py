"""
Program name: Salary Calc
Author: JMcDonald
date: 06/06/23
note: This program is to calculate Pay
"""
from os import system, name
from time import sleep
from colorama import Fore
from colorama import Style
def thanks():
        print(uname +", Thank you for using my calculator!")
def clear():
        if name == 'nt':
                _ = system('cls')
        else:
                _ = system('clear')
clear()
print("Simple Gross Pay Difference Calculator")
uname=input("What is your name? ")
def ask_user():
        answer = input(uname +", Are you Salary? (y/n) ")
        try:
                if answer[0] == 'y':
                        return True
                elif answer[0] =='n':
                        return False
                else:
                        print(f"Invalid response")
                        return ask_user()
        except Exception as error:
                print(f"Please answer y or n")
                print(error)
                return ask_user()
def update():
        answerx = input(uname +", Do you want to input a projected wage? (y/n) ")
        try:
                if answerx[0] == 'y':
                        return True
                elif answerx[0] =='n':
                        return False
                else:
                        print(f"Invalid response")
                        return update()
        except Exception as error:
                print(f"Please answer y or n")
                print(error)
                return update()
def calc():
        answery = input(uname +", Are you interested in finding out how much you could make per week with overtime? (y/n) ")
        try:
                if answery[0] == 'y':
                        return True
                elif answery[0] =='n':
                        return False
                else:
                        print(f"Invalid response")
                        return calc()
        except Exception as error:
                print(f"Please answer y or n")
                print(error)
                return calc()
def ans():
        answerz = input(uname + ", do you want to perform another calculation? (y/n) ")
        try:
                if answerz[0] == 'y':
                        return True
                elif answerz[0] =='n':
                        return False
                else:
                        print(f"Invalid response")
                        return ans()
        except Exception as error:
                print(f"Please answer y or n")
                print(error)
                return ans()
def currentsal():
    try:
        currentsalx=float(input("How much do you currently make per year? $")) #using float for partial hour
        return currentsalx
    except ValueError:
        print("Please enter a valid number")
        return currentsal()
def newsal():
    try:
        newsalx=float(input("What is the new salary? $"))
        return newsalx
    except ValueError:
        print("Please enter a valid number")
        return newsal()
def currentwa():
    try:
        currentx=float(input("What is your current wage? $"))
        return currentx
    except ValueError:
        print("Please enter a valid number")
        return currentwa()
def newwa():
    try:
        newx=float(input("What is your projected wage? $"))
        return newx
    except ValueError:
        print("Please enter a valid number")
        return newwa()
def hou():
    try:
        hoursx=float(input("How many hours do you project work? Up to 40? ")) #using float for partial hour entry
        return hoursx
    except ValueError:
        print("Please enter a valid number")
        return hou()
def otx():
    try:
        oty=float(input("How many hours do you project to work over 40? "))
        return oty
    except ValueError:
        print("Please enter a valid number")
        return otx()
while True: #loop start
    salary=ask_user()
    if salary==True:
        #inputs from user
        currentsalary=currentsal() 
        newsalary=newsal()
        #rate=float(input("What is your hourly rate? "))#using float for partial dollar entry
        #otRate=rate*1.54
        grossdifference=(newsalary - currentsalary)
        weekly=(newsalary/52)
        weeklydif=round((grossdifference/52),2)
        biweekly=(newsalary/26)
        biweeklydiff=round((grossdifference/26),2)
        difference=((newsalary / 2080)-(currentsalary / 2080)) #calculations
        differencerounded=(round(difference,2))
        print(f"Your Hourly pay difference is $",differencerounded) #output to user
        print(f"Your Estimated Weekly Pay {Fore.RED}Difference{Style.RESET_ALL} is $",weeklydif)
        print(f"Your Estimated Weekly Pay is $",weekly)
        print(f"Your Estimate Bi-Weekly Pay {Fore.RED}Difference{Style.RESET_ALL} is $",biweeklydiff)
        print(f"Your Estimated Bi Weekly Pay is $",biweekly)
        print(f"Your Esitmated Gross pay {Fore.RED}Difference{Style.RESET_ALL} is $",grossdifference)
        print(f"Your Estimated Net Pay is $",(newsalary*.75),"based off of 25% for Taxes and Insurance")
        ansy=ans()
        if(ansy==True): #check answer for continuation or exit      
                continue
        else:
                thanks()
                break   
    else:
                #input from user
                currentwage=currentwa()
                updatex=update()
                if updatex == True:
                        newwage=newwa()
                        #calculations
                        grosswage=((newwage * 2080) - (currentwage * 2080))
                        wagediff=(newwage - currentwage)
                        wagediffround=(round(wagediff,2))
                        #output to user
                        print("Your new Bi-Weekly Wage is $",newwage * 80)
                        print("Your new Gross Annual wage is $",newwage * 2080)
                        print("Your pay difference is $",wagediffround)
                        calcx=calc()
                        if calcx == True:
                                #rate=float(input("What is your hourly rate? "))#using float for partial dollar entry
                                hours=hou()
                                ot=otx()
                                otRate=newwage*1.5
                                pay=((newwage * hours)+(ot * otRate)) #calculations
                                print("Your projected pay is $",pay, "for",hours+ot, "hours") #output to user
                                print("Your projected Bi-Weekly pay is $",(pay * 2))
                                print("Your projected Bi-Weekly Net is $",((pay * 2) * .75),"based off of 25% for Taxes and Insurance")
                                print("Your projected Bi-Weekly Net is $",((pay * 2) * .75),"based off of 25% for Taxes and Insurance")
                        else:()
                else:
                        print("Your Estimated Bi-Weekly pay is $",(currentwage * 80))
                        print("Your projected Bi-Weekly Net is $",((currentwage * 80) * .75),"based off of 25% for Taxes and Insurance")
                        print("Your Estimated Annual Gross is $",currentwage * 2080)   
                        print("Your Estimated Annual Net is $",((currentwage * 2080) * .75),"based off of 25% for Taxes and Insurance")
                        calcx=calc()
                        if calcx == True:
                                #rate=float(input("What is your hourly rate? "))#using float for partial dollar entry
                                hours=hou()
                                ot=otx()
                                otRate=currentwage*1.5
                                pay=((currentwage * hours)+(ot * otRate)) #calculations
                                print("Your projected pay is $",pay, "for",hours+ot, "hours") #output to user
                                print("Your projected Bi-Weekly pay is $",(pay * 2))
                                print("Your projected Bi-Weekly Net is $",((pay * 2) * .75),"based off of 25% for Taxes and Insurance")
                                print("Your projected Annual Gross is $",(pay * 52), "based off of working all 52 weeks")
                                print("Your projected Annual Net is $",((pay * 52) * .75),"based off of 25% for Taxes and Insurance and working all 52 weeks")
                        else:() 
                ansx=ans()
                if ansx == True: #check answer for continuation or exit
                        continue
                else:
                        thanks()
                        break