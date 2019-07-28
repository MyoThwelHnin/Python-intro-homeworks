# Create a function that return the largest number in the list


def get_largest_number(mylist):
    largest_num = 0

for number in mylist:
    if largest_num < number:
        largest_num = number

return largest_num

result = get_largest_number([12,9,7,14,0])
print(result)
   





