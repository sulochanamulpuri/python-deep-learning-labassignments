list = input("Enter the sentence: ")

longest = 0
for word in list.split():
    if len(word) > longest:
        longest = len(word)
        longest_word = word

print("The longest word is %s" % longest_word)

reverse = list[::-1]
print ("The reverse of a sentence is %s" %reverse)

words = list.split() #Forget ()
len_sentence = len(words)
middle = []
if len_sentence%2==0:
    middle.append(words[(len_sentence//2)-1])
    middle.append(words[len_sentence//2])
else:
    middle.append(words[len_sentence//2])
print("The middle of a sentence is %s"%middle)