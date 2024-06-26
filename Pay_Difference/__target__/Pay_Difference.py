# Compilation mode, support OS specific.
# nuitka-project-if: {OS} in ("Windows", "Linux", "Darwin", "FreeBSD"):
#    nuitka-project: --onefile
# nuitka-project-if: {OS} not in ("Windows", "Linux", "Darwin", "FreeBSD"):
#    nuitka-project: --standalone

"""
Program name: Salary Calc
Author: JMcDonald
date: 06/06/23
note: This program is to calculate Pay, Both Hourly and Salary in USD
"""

def thanks():
        print(uname +", Thank you for using my calculator!")
print("Pay Calculator with Difference Calculation By Josh McDonald")
uname=input("What is your name? ")
def ask_user():
        answer = input(uname +", Are you Salary? (y/n) ")
        try:
                if answer.lower() == 'y':
                        return True
                elif answer.lower() =='n':
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
                if answerx.lower() == 'y':
                        return True
                elif answerx.lower() =='n':
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
                if answery.lower() == 'y':
                        return True
                elif answery.lower() =='n':
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
                if answerz.lower() == 'y':
                        return True
                elif answerz.lower() =='n':
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
def worked():
    try:
        currentx=float(input("How many hours do you expect to work per week? "))
        return currentx
    except ValueError:
        print("Please enter a valid number")
        return worked()
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
def tax():
    try:
        taxr=float(input("What is your local tax rate percentage? "))
        return (taxr / 100) 
    except ValueError:
        print("Please enter a valid number")
        return tax()
def taxaskl():
    taxaskq = input(uname +", Would you like to input your current local tax rate? (y/n) ")
    try:
        if taxaskq.lower() == 'y':
            return tax()
        elif taxaskq.lower() =='n':
            return False
        else:
            print(f"Invalid response")
            return taxaskl()
    except Exception as error:
            print(f"Please answer y or n")
            print(error)
            return taxaskl()

def taxaskf():
    taxaskfq = input(uname +", Would you like to Deduct Federal Taxes? (y/n) ")
    try:
        if taxaskfq.lower() == 'y':
            return taxf()
        elif taxaskfq.lower() =='n':
            return False
        else:
            print(f"Invalid response")
            return taxaskf()
    except Exception as error:
            print(f"Please answer y or n")
            print(error)
            return taxaskf()
def taxf():
    try:
        taxfr=float(input("What is your Federal tax rate percentage?(The average is 7.65%) ") or "7.65")
        return (taxfr / 100)
    except ValueError:
        print("Please enter a valid number")
        return taxf()
def garnish():
    garnishq = input(uname +",Would you like to include any Garnishments? (eg: Child Support or Alimony) (y/n) ")
    try:
        if garnishq.lower() == 'y':
            return tax()
        elif garnishq.lower() =='n':
            return False
        else:
            print(f"Invalid response")
            return garnish()
    except Exception as error:
            print(f"Please answer y or n")
            print(error)
            return garnish()
def garnishment():
    try:
        garnishr=float(input("What is the Monthly amount? "))
        return (garnishr / 4 )
    except ValueError:
        print("Please enter a valid number")
        return garnishment()


while True: #loop start
    salary=ask_user()
    if salary==True:
        #inputs from user
        currentsalary=currentsal()
        newsalary=newsal()
        taxaskr=taxaskl()
        taxaskfr=taxaskf()
        garnishrs=garnish()
        #rate=float(input("What is your hourly rate? "))#using float for partial dollar entry
        #otRate=rate*1.50
        grossdifference=(newsalary - currentsalary)
        weekly=round((newsalary/52),2)
        weekly=round((newsalary/52),2)
        weeklydif=round((grossdifference/52),2)
        biweekly=round((newsalary/26),2)
        biweekly=round((newsalary/26),2)
        biweeklydiff=round((grossdifference/26),2)
        difference=((newsalary / 2080)-(currentsalary / 2080)) #calculations
        differencerounded=(round(difference,2))
        def sal_print():
                print(f"Your Current Hourly rate is$",round((currentsalary / 2080),2))
                print(f"Your Hourly pay difference is $",differencerounded) #output to user
                print(f"Your Estimated Weekly Pay Difference is $",weeklydif)
                print(f"Your Estimated Weekly Pay is $",weekly)
                print(f"Your Estimated Bi-Weekly Pay Difference is $",biweeklydiff)
                print(f"Your Estimated Bi Weekly Pay is $",biweekly)
                print(f"Your Estimated Gross pay Difference is $",grossdifference)
                print(f"Your Estimated Net Pay is $",(newsalary*(1 - (taxaskr + taxaskfr)) - garnishrs * 52))
        sal_print()
        ansy=ans()
        if(ansy==True): #check answer for continuation or exit      
                continue
        else:
                thanks()
                break   
    else:
                #input from user
                currentwage=currentwa()
                houworked=worked()
                taxaskr=taxaskl()
                taxaskfr=taxaskf()
                garnishrs=garnish()
                updatex=update()
                if updatex == True:
                        newwage=newwa()
                        #calculations
                        grosswage=(((newwage * houworked) * 52) - ((currentwage * houworked) * 52))
                        grosswage=(((newwage * houworked) * 52) - ((currentwage * houworked) * 52))
                        wagediff=(newwage - currentwage)
                        wagediffround=(round(wagediff,2))
                        groround=(newwage * 2080)
                        biweround=(newwage * 80)
                        groround=(newwage * 2080)
                        biweround=(newwage * 80)
                        #output to user
                        def sal_print():
                                print("Your pay difference is $",wagediffround)
                                print("Your new Bi-Weekly Income is $",(round(biweround,2)))
                                print("Your new Gross Annual Income is $",(round(groround,2)))
                        calcx=calc()
                        if calcx == True:
                                hours=houworked
                                ot=otx()
                                otRate=newwage*1.5
                                pay=round(((newwage * hours)+(ot * otRate)),2) #calculations
                                binet=((pay * 2)*(1 - (taxaskr + taxaskfr)-(garnishrs * 2)))
                                netan=((pay * 52) * (1 - (taxaskr + taxaskfr)-(garnishrs * 52)))
                                def sal_print():                                
                                        print("Your projected pay is $",pay,"for",hours+ot,"hours") #output to user
                                        print("Your projected Bi-Weekly pay is $",(pay * 2))
                                        print("Your projected Bi-Weekly Net is $",(round(binet,2)))
                                        print("Your projected Annual Gross is $",(pay * 52), "based off of working all 52 weeks")
                                        print("Your projected Annual Net is $",(round(netan,2)))
                        else:()
                else:
                        anround=(((currentwage * houworked)*52) * (1 - (taxaskr + taxaskfr)) - (garnishrs * 52))
                        bipayround=((currentwage * houworked)*2)
                        netround=(bipayround *(1 - (taxaskr + taxaskfr))- (garnishrs *2))
                        angro= ((currentwage * houworked)* 52)
                        def sal_print(): 
                                print("Your projected pay is $",(currentwage * houworked),"for",houworked,"hours") #output to user
                                print("Your Estimated Bi-Weekly pay is $",(round(bipayround,2)))
                                print("Your projected Bi-Weekly Net is $",(round(netround,2)))
                                print("Your Estimated Annual Gross is $",(round(angro,2)))   
                                print("Your Estimated Annual Net is $",(round(anround,2)))
                        calcx=calc()
                        if calcx == True:
                                hours=houworked
                                ot=otx()
                                otRate=currentwage*1.5
                                pay=((currentwage * hours)+(ot * otRate)) #calculations
                                netan=((pay * 52) * (1 - (taxaskr + taxaskfr))-(garnishrs * 52))
                                binet=((pay * 2) * (1 - (taxaskr + taxaskfr))- (garnishrs *2))
                                def sal_print():                              
                                        print("Your projected pay is $",pay, "for",hours+ot, "hours") #output to user
                                        print("Your projected Bi-Weekly pay is $",(pay * 2))
                                        print("Your projected Bi-Weekly Net is $",(round(binet,2)))
                                        print("Your projected Annual Gross is $",(pay * 52), "based off of working all 52 weeks")
                                        print("Your projected Annual Net is $",(round(netan,2)))
                        else:()
                # sal_printed=sal_print()
                sal_print()
                ansx=ans()
                if ansx == True: #check answer for continuation or exit
                        continue
                else:
                        thanks()
                        break