from time import sleep
import math
#Establishing dictionary of rates
rates = {"EUR":0.9, "USD":0.77, "JPY": 0.0074}
#Create function to calculate conversion
def convert(amount,currency):
    total = amount / rates.get(currency.upper())
    return round(total, 2)
print("{}\n Currency Converter v1.1 \n{}".format("*"*80, "*"*80))
#while loop to repeat
again = "y"
#input and output/ repeat condition
while again.lower() != "n":
    ConvertAmount = float(input("How much do you want to convert(GBP)? "))
    ConvertCurrency = str(input("EUR \nUSD \nJPY \nWhat currency would you like to convert to?(enter as shown) "))
    print("PROCESSING...")
    sleep(2)
    print("CONVERTED TOTAL: {} \nSTARTING AMOUNT: {} \nRATE:{}".format(convert(ConvertAmount,ConvertCurrency), ConvertAmount, rates.get(ConvertCurrency.upper())))
    again = str(input("Use again?(y/n)"))
