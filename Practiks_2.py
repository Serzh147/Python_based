
# def truncate(text, length):
#     result = f"{text[0:length]}..."
#     return print(result)
# text = 'Becose we are wery important people! Sad mr. Putin'
# truncate(text, 24)

# def get_hidden_card(card_number, lenght):
#    return(print(f"{'*'*lenght}{card_number[12::]}"))
#
# card_number = str(1253263545858811)
# get_hidden_card(card_number,4)

numbers = []
for value in range(1,11):
   cube = value**3
   numbers.append(cube)
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print()
print('Второй способ:')
print()
cube = [value**3 for value in range(1,11)]
print(cube)



