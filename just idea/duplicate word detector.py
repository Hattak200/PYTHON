text = input("enter your text: ")
list =  text.split()
count = 0
for i in range(len(list)):
    count += 1
print("The number of words in the text is:", count)
not_repeat = []
for word in list:
    c = 0
    if word not in not_repeat:
        for i in range(0 , count):
            if word == list[i]:
                c += 1
                if c > 1:
                    print("The word", word, "is repeated", c, "times")
                    not_repeat.append(word)

   

     
