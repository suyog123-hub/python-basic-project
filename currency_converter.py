exchange_rates = {
    'USD': 1.0,
    'EUR': 0.92,
    'GBP': 0.79,
    'NPR': 148.50,
    'INR': 83.12,
    'JPY': 149.50,
    'AUD': 1.53,
    'CAD': 1.38,
}
while(True):
    print("Available currencies:", list(exchange_rates.keys()))

    amount = float(input("Enter amount: "))
    from_cur = input("From currency: ").upper()
    to_cur = input("To currency: ").upper()

    if from_cur in exchange_rates and to_cur in exchange_rates:
        result = (amount / exchange_rates[from_cur]) * exchange_rates[to_cur]
        print(f"{amount} {from_cur} = {result:.2f} {to_cur}")
    else:
        print("Invalid currency")
