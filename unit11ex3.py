"""For this problem,use the dictionary from the beginning of this chapter whose keys are month names and whose 
values are the number of days in the corresponding months.
(a) Ask the user to enter a month name and use the dictionary to tell them how many days are in the month. 
(b) Print out all of the keys in alphabetical order. (c) Print out all of the months with 31 days. 
(d) Print out the (key-value) pairs sorted by the number of days in each month (e) Modify the program from part 
(a) and the dictionary so that the user does not have to know how to spell the month name exactly. That is, 
all they have to do is spell the ﬁrst three letters of the month name correctly."""

days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 
'September':30, 'October':31, 'November':30, 'December':31}

#a
mon = input('Enter the month : ')
if mon in days:
    print ('There are',days[mon],' days in that month')
#b
print(sorted(days.keys()))

x = list(days.items())
x = [i[0] for i in x]
x.sort()
for i in x :
    print(i)

#c 
L = [x[0] for x in days.items() if x[1]==31]
print(L)

for x in days.items():
       if x[1]==31:
           print(x[0]) 
#d
print(sorted(days.items()))


#e

z = input('Enter the month : ')
for a in days.keys() :
    if a[:3] == z[:3]:
        print(a,days[a])



