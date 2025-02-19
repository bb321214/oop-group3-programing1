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
    print("")
else:
    # calculate gas price -- keith to do
    print("")

# calculate gst and total price
provinceAbbr = input("Please enter the 2 letters province abbreviation: ")
provinceAbbr.upper()
match provinceAbbr:
    case "AB":
        gst = 0.5
    case "BC":
        gst = 0.5
    case "MB":
        gst = 0.5
    case "NT":
        gst = 0.5
    case "NU":
        gst = 0.5
    case "QC":
        gst = 0.5
    case "SK":
        gst = 0.5
    case "yt":
        gst = 0.5
    case "ON":
        gst = 0.13
    case others:
        gst = 0.15
gst_money = price_after * gst
total_price = price_after + gst_money

print("---------------------------------------------------------------------------------")
print("Product      # Of Litres    Price Before    Price After    GST    Total Price")
print(f"{product}      {litres}         {price_before}            {price_after}           {gst_money}   {total_price}")
print("---------------------------------------------------------------------------------")
print("Thanks for your business, Good Bye")
