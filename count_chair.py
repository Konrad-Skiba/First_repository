str1 = "ala ma kota"
char_dict = dict()

for char in str1:
    count = str1.count(char)
    char_dict[char] = count

print('Result:',char_dict)

print(char_dict)