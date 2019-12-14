# Write a program that asks the user for a number of seconds and prints
# out how many minutes and seconds that is. For instance, 200 seconds is 3
# minutes and 20 seconds.
# [Hint: Use the // operator to get minutes and the % operator to get seconds.]


answer = int(input('enter the seconds '))

print (answer,'- time in seconds')
print ('That is ', answer//60,' minutes and ',answer%60,' seconds' )

