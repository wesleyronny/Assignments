#%%
str =  'print only the words that start with s in this sentence'
for word in str.split():
    if word[0] =='s':
        print(word)

# %%
#use range() to print even numbers from 0 to 10
for x in range(1,10):
    if x%2 == 0:
        print(x)

# %%
#create a list of numbers between 1 and 50 that are divisible by 3
for num in range(1,51): 
    if num%3 == 0:
       print(num)
# %%
#go through the string below and if length is even print 'even'
str = 'Print every word in this sentence that has an even number of'
for word in str.split():
    if len(word)%2 == 0:
        print(word + ' has an even length ')
# %%
#write a program that prints intergers from 1 to 100.For multiples of 3 print'Fizz' instead of number,for multiples of 3 print 'Buzz'.For numbers divisible by both 3 and 5 print 'FizzBuzz'
for num in range(1,100):
    if num % 5 == 0 and num % 3 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
# %%
#use list comprehension to create a list of first letters of every word in the string below:
str = 'Create a list of the first letters of every word in this string'
for word in str.split():
    print(word[0])

# %%
