import csv
from collections import defaultdict

# File name
FILENAME = "orders.csv"

# Data containers
total_revenue = 0
order_count = 0
customer_spending = defaultdict(float)

# Read CSV
with open(FILENAME, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        customer = row['Customer']
        amount = float(row['Amount'])
        total_revenue += amount
        order_count += 1
        customer_spending[customer] += amount

# Sort top customers
top_customers = sorted(customer_spending.items(), key=lambda x: x[1], reverse=True)[:3]

# Report
print("===== ORDER SUMMARY REPORT =====")
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Number of Orders: {order_count}")
print(f"Number of Unique Customers: {len(customer_spending)}")
print("\nTop 3 Customers by Spending:")
for i, (customer, amount) in enumerate(top_customers, start=1):
    print(f"{i}. {customer} - ${amount:.2f}")
