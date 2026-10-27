# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 200,
    "MSFT": 420
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

n = int(input("How many different stocks do you want to buy? "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Stock:", stock_name)
        print("Price:", stock_prices[stock_name])
        print("Investment:", investment)
    else:
        print("Stock not available!")

print("\nTotal Investment =", total_investment)

# Save result in a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write("Total Investment = " + str(total_investment))

print("Result saved in portfolio.txt")