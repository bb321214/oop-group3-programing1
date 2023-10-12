import sys

# print menu
print("-------------------------------------------------")
print("*** Welcome to Gas Station Supplier Program! ***")
print("-------------------------------------------------")
print("Please select the type of purchase:\nG: Gas\nO: Oil")
# enter your option
purchaseType = input(">>> ")

# check option
isOilOption = purchaseType == "o" or purchaseType == "O"
isGasOption = purchaseType == "g" or purchaseType == "G"
# invalid option check
if not isOilOption and not isGasOption:
    print("Invalid input, you should enter g/G or o/O")
    sys.exit()

# order detail variables
product = "demo"
litres = 0.0
price_before = 0.0
price_after = 0.0

if isOilOption:
    # calculate oil price -- zeo to do
    cases = float(input("Enter # of cases of Oil: "))
    litres = cases*12
    original_cost_per_litre = 1.27
    price_before = litres*original_cost_per_litre
    if(cases > 8):
        price_after = price_before*0.9
    else:
        price_after = price_before
else:
    # calculate gas price -- keith to do
    print("")

# calculate gst and total price
provinceAbbr = input("Please enter the 2 letters province abbreviation: ")
provinceAbbr = provinceAbbr.upper()
match provinceAbbr:
    case "AB":
        gst = 0.05
    case "BC":
        gst = 0.05
    case "MB":
        gst = 0.05
    case "NT":
        gst = 0.05
    case "NU":
        gst = 0.05
    case "QC":
        gst = 0.05
    case "SK":
        gst = 0.05
    case "yt":
        gst = 0.05
    case "ON":
        gst = 0.13
    case others:
        gst = 0.15
gst_money = round(price_after * gst, 2)
total_price = price_after + gst_money

print("---------------------------------------------------------------------------------")
print("Product      # Of Litres    Price Before    Price After    GST    Total Price")
print(f"{product}      {litres}         {price_before}            {price_after}           {gst_money}   {total_price}")
print("---------------------------------------------------------------------------------")
print("Thanks for your business, Good Bye")
