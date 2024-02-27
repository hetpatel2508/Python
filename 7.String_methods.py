word="patel het rajeshkumar"

#Slicing techniques
print(word[6:9])    # 6 to 8
print(word[6:])     #6 to length
print(word[:9])     # 0 to 8
print(word[6:18:2]) # 6 to 17 ma 2-2 words ne gap no latter print tase
print("")


#length method
print(len(word))


#capitalize method
print(word.capitalize())    #only first latter capital karse
print(word.upper())         #convert to upper case
print(word.lower())         #convert to lower case


print(word.endswith("rajeshkumar"))  #true if yes , nai to false

print(word.count('h'))      #will return how many time 'h' appear in string

print(word.find('het'))     #will return index of word 'het' starts with

print(word.replace("het","HETT")) #will simply repalce words