#%%
word1 ='How'
word2 ='do'
word3 ='ÿou'
word4 = 'like'
word5 = 'python'
word6 = 'so'
word7 = 'far'
print( word1+' ' + ' '+ word2+' '+ word3+ ' '+ word4 +' '+ word5+ ' '+ word6+ ' '+ word7)
# %%
x = 50.125
y = 50.125
print(x+y)
# %%
x = 300.25
y = 200.0
print(x-y)
# %%
x = 200.5
y = 2
print(x/y)
# %%
x = 50.125
y = 2
print(x*y)

# %%
x = 10.01249
y = 2
print(x**2)
# %%
x = 4
y = 6
z = 5
print(x*(y+z))
# %%
x = 4
y = 6
z = 5
print(x*y+z)

# %%
x = 4
y = 6
z = 5
print(x+y*5)
# %%
s = 'hello'
print(s[1])
# %%
s = 'hello'
print(s[4])
# %%
s = 'hello'
print(s[-1])
# %%
list=[0, 0, 0]
print(list)
# %%
list = [0, 0, 0, 0]
print(list[1:])
# %%
list3 = [1,2,[3,4,'goodbye']]
print(list3)
# %%
d = {'simple-key':'hello'}
print(d{4:})

# %%
x= 144
print(x**(1/2))

# %%
S = 'hello'
print(s[::-1])
# %%
list1 = [1,2,[3,4,'hello']]
list1[2][2]
list1[2][2] = 'goodbye'
print(list1)


# %%
list4 = [7,5,4,6,2,8]
sorted(list4)
# %%
sorted_list = list4.sort()
print(sorted_list)
# %%
d = {'simple_key':'hello'}
d['simple_key']
# %%
d = {'k1':{'k2':'hello'}}
d['k1']['k2']
# %%
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d['k1']
# %%
d['k1'][0]
# %%
d['k1'][0]['nest_key']
# %%
d['k1'][0]['nest_key'][1][0]
# %%
person = 'Sammy'

if person == 'Sammy' :
    print('Welcome Sammy!')
else:
    print('Welcome, what's your name?')

# %%
>>>(4< 5) and (5< 6)
# %%
name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello, Mary')
     if password == 'swordfish':
    print('Access granted.')
    else:
        print('Wrong password.')
# %%
spam = 0
if spam < 5:
    print('Hello, world')
    spam = spam + 1

# %%
spam = 0
while spam < 5:
    print('Hello, world.')
# %%
x = 'ronaldo chacha'
print(x)
# %%
while True:
    print('Hello, world')
# %%
if name != 'Joe':
   continue
print('Hello, Joe. What is the password?(It is a fish.)')
password = input()
if password == 'swordfish'
    break
print('Access granted')
# %%

# %%
try:
    print(x)
except:
        print('An exception occurred')
# %%
print(x)
# %
# %%
print('Ronaldo Chacha')
name = input()
print('Habari yako,' + name')
# %%
x = 23
y = 5
print(x%y)
# %%
name = ('Chuck') 
input = 'Welcome buddy'
print(name + input)
# %%
  x = 5
  if x < 10:
      print('smaller') 
      if x > 20:
          print('Bigger')
          print('finis')

# %%
 x = 5
if x == 5:
    print('Equals 5')
# %%
x = 5
if x > 2:
  print('Bigger than 2 ')
  print('Still bigger')
print('Done with 2')
for i in range(5):
   print(i)
if i > 2:
  print('Bigger than 2')
  print('All done')
# %%
if x < 2:
    print('medium')
elif x < 10:
    print('medium')
else:
     print('large')

# %%
x = 20
if x < 2:
    print('medium')
elif x < 10:
    print('medium')
else:
    print('large')
print('All done')
# %%
x = 5
if x < 2:
    print('small')
elif x < 10:
    print('medium')
print('All done')

# %%
 x = 5
 if x < 2:
     print('small')
 elif x < 10:
     print('medium')
 elif x < 20:
     print('big')
 elif x < 40:
     print('larg')
 elif x < 100:
      print('huge')
 else:
     print('Ginormous')


# %%
if x < 2:
    print('below 2')
elif x < 20:
    print('below 20')
elif x < 10:
    print('below 10')
else:
    print('something else')

# %%
i = 1
while i < 20:
    print(i)
    # if i == 15:
    #     break
    i += 2
# %%
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)
# %%
for x in range(2,30,3):
    print(x)
#%%
adj = ['red', 'big','tasty']
fruits = ['apple','banana','cherry']
for x in adj:
    for y in fruits:
        print(x,y)    
# %%
