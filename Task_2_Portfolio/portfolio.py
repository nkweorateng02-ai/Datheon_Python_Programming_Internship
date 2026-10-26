import csv

portfolio = {} # Empty Dictionary structure

num = int(input("Enter number of stocks: "))# Stores stocks quantity

for i in range(num):# In this loop I will collect data from the user
    ticker = input("\nEnter stock ticker symbol: ").upper()
    buy_price = float(input(f"Enter buy price for {ticker}: $"))
    quantity = int(input(f"Enter number of shares for {ticker}: "))
    current_price = float(input(f"Enter current price for {ticker}: $"))

    portfolio[ticker] = [quantity, buy_price, current_price]# Stores data in a dictionary

# Step 3: Calculate and show
print("\n--- Stock Portfolio Perfomance Tracker ---")
total_invested = 0
total_now = 0

for ticker in portfolio:
    quantity, buy, current = portfolio[ticker]
    
    invested = quantity * buy# Calculates the money invested
    now = quantity * current# Current market value
    gain = now - invested# Gain/Loss
    percent = (gain / invested) * 100# Convert to percentage

    total_invested += invested # Stores invested amount and avoids overriding
    total_now += now# Prevents overriding and stores current market value

    print(f"{ticker}: {quantity} quantity | Gain: ${gain:.2f} ({percent:.1f}%)")# Print data

print(f"\nTotal Invested: ${total_invested}")
print(f"Total Now: ${total_now}")
print(f"Total Profit: ${total_now - total_invested:.2f}")

# Step 4: Save to CSV file
with open("portfolio_summary.csv", "w", newline="") as file:# Create a new file "Portfolio summary"
    writer = csv.writer(file)
    writer.writerow(["Ticker", "Quantity", "Buy Price", "Current Price", "Gain/Loss"])

    for ticker in portfolio:
        quantity, buy, current = portfolio[ticker]
        gain = (quantity * current) - (quantity * buy)
        writer.writerow([ticker, quantity, buy, current, gain])#writes everything to the

print("\nDone! File saved as portfolio_summary.csv")
