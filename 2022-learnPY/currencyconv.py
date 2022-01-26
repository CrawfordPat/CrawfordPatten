def currency_conv(currency, amount, date):
    """Convert amount of currency on date from USD to currency.
    Example input:
        2012-2-28 35.30 EUR
    
    Example output:
        2012-2-28 $35.50 USD = 26.19 EUR"""
    # Convert amount to float
    amount = float(amount)
    # Convert date to datetime object
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    # Get the exchange rate for the date
    rate = get_exchange_rate(date, currency)
    # Convert the amount to the currency
    amount = amount * rate
    # Return the result
    return date.strftime("%Y-%m-%d") + " $" + str(amount) + " USD = " + str(amount / rate) + " " + currency