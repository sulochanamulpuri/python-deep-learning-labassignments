list = input("Enter the sentence: ")

longest = 0
for word in list.split():
    if len(word) > longest:
        longest = len(word)
        longest_word = word

print("The longest word is %s" % longest_word)

reversed_string = ' '.join(w[::-1] for w in list.split())
print ("the reversed sentence is %s" %reversed_string)

words = list.split() #Forget ()
len_sentence = len(words)
middle = []
if len_sentence%2==0:
    middle.append(words[(len_sentence//2)-1])
    middle.append(words[len_sentence//2])
else:
    middle.append(words[len_sentence//2])
print("the middle words are %s" % ' '.join(middle))