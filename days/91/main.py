from currency import Currency

curr = Currency(1000, 'USD')
print(curr)

curr2 = Currency(250, 'EUR')
print(curr2)

new_currency = curr.convert_to('EUR')
print(new_currency)

new_curr = curr2.convert_to('USD')
print(new_curr)

sum_curr = curr + curr2
print(sum_curr)

sum_curr2 = curr + 5.5
print(sum_curr2)
