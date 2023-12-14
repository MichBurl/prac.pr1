#The playing cards have the following values: Ace (A), King (K), Queen (Q), Jack (J) and 10 (T) have a value of 10 each. 
# The other cards have the value indicated by the card number. 
# Create a function f(player1,player2) that returns true if the first player has cards of the same or higher value, and false otherwise. 
# Example:
#f("AJ972","AQT72") 🡪 False
#f("9532","K8") 🡪 True

def f(player1, player2):
    card_values = {'A': 10, 'K': 10, 'Q': 10, 'J': 10, 'T': 10}

    def total_value(player):
        total = 0
        for card in player:
            if card in card_values:
                total += card_values[card]
            else:
                total += int(card)
        return total

    return total_value(player1) >= total_value(player2)

# Example usage:
result1 = f("AJ972", "AQT72")
result2 = f("9532", "K8")

print(result1)  # Output will be False
print(result2)  # Output will be True
