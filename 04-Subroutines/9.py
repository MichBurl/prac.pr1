def min_coins_count(amount_to_pay):
    return amount_to_pay // 5 + (amount_to_pay % 5) // 2 + (amount_to_pay % 5) % 2

# Sample usage:
print("f(23) returns:", min_coins_count(23))
print("f(8) returns:", min_coins_count(8))
print("f(2) returns:", min_coins_count(2))
print("f(0) returns:", min_coins_count(0))