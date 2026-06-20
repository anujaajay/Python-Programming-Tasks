stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150
}

total = 0

while True:
    stock = input("Enter stock name (AAPL/TSLA/GOOGL) or 'done': ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        qty = int(input("Enter quantity: "))
        total += stock_prices[stock] * qty
    else:
        print("Stock not found!")

print("Total Investment Value = $", total)

# Save result to file
file = open("portfolio.txt", "w")
file.write("Total Investment Value = $" + str(total))
file.close()
