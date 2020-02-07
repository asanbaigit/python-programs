"""
 Recall that if s is a string, then s.find('a') will ﬁnd the location of the ﬁrst a in s. The problem is 
 that it does not ﬁnd the location of every a. Write a function called findall that given a string and a 
 single character, returns a list containing all of the locations of that character in the string. It should
  return an empty list if there are no occurrences of the character in the string. """

def findall (w,l):
    return [i for i in range (len(w)) if w[i] == l]

w = input('Enter a word :')
l = input('Enter a letter :')

print(findall(w,l))