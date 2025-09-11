"""
Miriam Stern
goal: Create a function to extract hours and minutes from users minutes entry.  called minutes_to_hours_and_minutes()
1. call my function minutes_to_hours_and_minutes
2. in function : minutes_to_hours_and_minutes:
    A. Ask the user "how many minutes they would like to calculate", save as minutes
    B. convert minutes to float, save as minutes 
    C. divide minutes by 60, store this value as hours
    D. if there is a remainder, store as min
    D. tell my user what the conversion is

    
"""

""" this is the conversion that you need to divide minutes by in order to get hours"""
HOUR_CONVERSION = 60.0

""" The purpose of this function is to convert the minutes the user would like to calculate into hours and minutes"""
def minutes_to_hours_and_minutes():
    question = "How many minutes would you like to calculate?" #asking user to input amount of minutes they would like to calculate 
    minutes = int(input(question)) #minutes that user inputed is converted into a float 
    hours = (minutes // HOUR_CONVERSION) # minutes are divided by 60 which converts it into hours
    remaining_minutes = (minutes % HOUR_CONVERSION) # the remaining minutes after being converted into hours
# printing the conversion of the users minutes into hours and minutes
    print('the conversion from ', minutes, 'minutes to hours and minutes is ', hours, 'hours and ', remaining_minutes, 'minutes')
    

    
    
    
minutes_to_hours_and_minutes()
