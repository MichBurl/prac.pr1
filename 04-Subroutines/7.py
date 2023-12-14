def f(card_number):
    masked = card_number[:2] + '*' * (len(card_number) - 6) + card_number[-4:]
    return masked

print(f("5290312400019022"))