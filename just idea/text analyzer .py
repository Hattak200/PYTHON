text = str(input('welcome to the text analyzer! \n please enter the text you want to analyze:'))
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_count = 0
space_count = 0
notvowels_count = 0
for letter in text.lower():
    if letter in vowels :
        vowels_count += 1
    elif letter == ' ' :
        space_count += 1
    else:
        notvowels_count += 1
print('the number of vowels in the text is:', vowels_count)
print('the number of spaces in the text is:', space_count)
print('the number of non-vowel characters in the text is:', notvowels_count)






