"""
Write a class called Wordplay. It should have a ﬁeld that holds a list of words. The user of the class should 
pass the list of words they want to use to the class. There should be the following methods:
• words_with_length(length) — returns a list of all the words of length length 
• starts_with(s) — returns a list of all the words that start with s 
• ends_with(s) — returns a list of all the words that end with s 
• palindromes() — returns a list of all the palindromes in the list 
• only(L) — returns a list of the words that contain only those letters in L 
• avoids(L) — returns a list of the words that contain none of the letters in L """

class Wordplay:
    def __init__(self,words=[]):
        self.words = words
    
    def __str__(self):
        return ','.join(self.words)
    
    def starts_with_s (self):
        return [word for word in self.words if word[0]=='s']

    def words_with_length(self,length):
        return [word for word in self.words if len(word) == length]

    def ends_with_s(self):
        return [word for word in self.words if word[-1]=='s']
    
    def palindromes(self):
        return [word for word in self.words if word == word[::-1]]
    
    def only_L (self,L):
        List_only_L = []
        for i in range (len(self.words)):
            for j in range (len(L)):
                if L[j] in self.words[i]:
                    if self.words[i] not in List_only_L:
                        List_only_L.append(self.words[i])
        return List_only_L
    
    def avoids_L (self,L1):
        List_avoids_L = []
        for i in range (len(self.words)):
            flag = True
            for j in range (len(L1)):
                if L1[j] in self.words[i]:
                    flag = False
            if flag:
                List_avoids_L.append(self.words[i])       
        return List_avoids_L

p = Wordplay(['s123','456s','python','silver','silk','abccba','hello','cola','upside','java'])
print(p)

print(p.starts_with_s())

print(p.words_with_length(4))

print(p.ends_with_s())
print(p.palindromes())

L = ['o','d','i']
print(p.only_L(L))

L1 = ['o','s']
print(p.avoids_L(L1))
