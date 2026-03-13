# Currency Converter - Terminal Based

exchange_rates = {
    'USD': 1.0,
    'EUR': 0.92,
    'GBP': 0.79,
    'NPR': 133.50,
    'INR': 83.12,
    'JPY': 149.50,
    'AUD': 1.53,
    'CAD': 1.36,
    'CHF': 0.89,
    'CNY': 7.24,
}

def convert(amount, from_currency, to_currency):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in exchange_rates:
        print(f"❌ '{from_currency}' is not supported.")
        return
    if to_currency not in exchange_rates:
        print(f"❌ '{to_currency}' is not supported.")
        return

    # convert to USD first then to target currency
    in_usd = amount / exchange_rates[from_currency]
    result = in_usd * exchange_rates[to_currency]

    print(f"\n✅ {amount} {from_currency} = {result:.2f} {to_currency}\n")

def show_currencies():
    print("\n📋 Supported Currencies:")
    for code in exchange_rates:
        print(f"   {code}")
    print()

def main():
    print("=" * 40)
    print("      💱 CURRENCY CONVERTER")
    print("=" * 40)

    while True:
        print("\nOptions:")
        print("1. Convert currency")
        print("2. Show supported currencies")
        print("3. Exit")

        choice = input("\nEnter choice (1/2/3): ").strip()

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                from_currency = input("From currency (e.g. USD): ").strip()
                to_currency = input("To currency (e.g. NPR): ").strip()
                convert(amount, from_currency, to_currency)
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")

        elif choice == '2':
            show_currencies()

        elif choice == '3':
            print("\n👋 Goodbye!\n")
            break

        else:
            print("❌ Invalid choice. Enter 1, 2 or 3.")

main()