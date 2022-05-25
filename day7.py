#Python range() Function

#Using Range Function
print(range(6))
print(range(1,33))
print(range(1,100,2))

#using range on list
print(list(range(6)))
print(list(range(1,6)))
print(list(range(1,100,2)))
print(list(range(1,100,3)))
print(list(range(1,100,4)))

#range func 
a = range(6)
for n in a:
  print(a)

a = range(6)
for n in a:
  print(n)  
#
a = range(16,20)
for n in a:
  print(n)
#  
a = range(16,20)
for n in a:
  print(n)

a = range(1,20,2)
for n in a:
  print(n)


#Join(greet)
#join function iterable.
greet = ' '.join(['Hi','i','am','RObot'])
print(greet)

greet1 = ("Apple","Cherry" , "Mango")
x = ".".join(greet1)
print(x)

d = {
  'name':"Neeti",
  'country':"Bangladesh" 
}
check = "Test"
x = check.join(d)
print(x)

#List UnpACking
a,b,c,d = [1,2,3,4]
print(a)
print(b)
print(c)
print(d)

a,b,c,*murgi = [1,2,3,4,5,6]
print(a)
print(b)
print(c)
print(murgi)


a,b,c,*murgi,d,e = [1,2,3,4,5,6,7,8,9,10]
print(a)
print(b)
print(c)
print(murgi)
print(d)
print(e)


#Dictionary
#Dictionary******unordered,
#list,element of dictionary
#declare dictionary with a list.
d = {'name' : 'Neeti',
     'age' : 24,
     'is gratuated': True,
     'my_cart' : ['food','mood']
    }
print(d)
print(d["name"]) #ACCESS KEY FOR VALUE
print(d['age'])


#declare dictionary with a list.
list = [{'name':'Neeti',
        'age': 24,
        'is_graduation': True,
        'my_cart':['food','mood']}]
print(list)


#multidimentional list
list = [{'name' : 'Neeti',
     'age' : 24,
     'is gratuated': True,
     'my_cart' : ['food','mood']
    },
   {'name' : 'srabonti',
     'age' : 23,
     'is gratuated': True,
     'my_cart' : ['food','mood']
    }     ]
print(list)
print(list[1]['my_cart'][1])
print(list[0]['my_cart'][0])
print(list[1]['age'])



a ={
    123: 'srabonti',
     'age' : 23,
     'is gratuated': True,
     'my_cart' : ['food','mood']
    } 
print(123)
print(a[123])

a ={
    True: 'srabonti',
     'age' : 23,
     'is gratuated': True,
     'my_cart' : ['food','mood']
    } 
print(a[True])
#dictionary Key alws emutable



#update name the last value
a = {'name':'neeti',
    'name': 'srabonti',
     'age' : 23,
     'age' : 30,
     'is gratuated': True,
     'my_cart' : ['food','mood']
    } 
print('name')
print(a['name'])
print(a['age'])

d = { 
   'name' : 'Neeti',
     'age' : None,
     'is gratuated': True,
     'my_cart' : ['food','mood']
    }
print(d.update({'age' : 24}))
print(d)


#Get Function
#N.B: GEt is use for error handling.
value = {
  'name' : 'Neeti',
     'age' : 24,
     'is gratuated': True,
     'my_cart' : ['food','mood']
    }
print(value.get('ok'))
print(value.get('name'))
print(value.get('age',30))

value = {
  'name' : 'Neeti',
     'age' : None,
     'is gratuated': True,
     'my_cart' : ['food','mood']
    }
print(value.get('age',30))


#in func
d ={'name' : 'Neeti',
       'age': 24,
       'is_graduate' :True,
'my_cart' : ['food', 'dress']
       }
#in func
print('my_cart' in d)
#values
print(24 in d.values())
#keys
print('my_cart' in d.keys())
#items
print(d.items)
print(d)
#pop
print(d.pop('name'))
print(d)
#popitem
print(d.popitem())
#update
print(d.update({'age' : 30}))
print(d)


#list mutable
#tuple emutable
#tuple a kisu insert kora jai na

#tuple
#t = (1,2,3)
#t[0] = 4
#print(t) 
#N.B: tuple unpacking kora possible.


#SEt:a distinct number of element,unique.

s = {1,2,3}
print(s)
s = {1,2,3,3}
print(s)
#add func
s = {1,2,3}
s.add(100)
print(s)


x ={1,2,3,4,5,6,7}
y = {8,9,10,11,12,13}
z ={1,5,9}

print(x.union(y))

x ={1,2,3,4,5,6,7}
y = {8,9,10,11,12,13}
z ={1,5,9}
print(x.intersection(z))

x ={1,2,3,4,5,6,7}
y = {8,9,10,11,12,13}
z ={1,5,9}
print(x.intersection_update(y))

x ={1,2,3,4,5,6,7}
y = {8,9,10,11,12,13}
z ={1,5,9}
print(x.isdisjoint(y))

s1= {1,2,3,4,5}
s2= {4,5,6}
print(s1.isdisjoint(s2))


s= {1,2,3,4,5}
n= {4,5,6}
print(s|n)

x= {1,2,3,4,5}
y= {4,5,6}
print(x & y)

s ={1,2,3}
y ={4,5,6,6}
print(s.union(y) )
print(s|y)
print(s.intersection(y)) 
print(s & y)
print(s.intersection_update(y))
print(s.isdisjoint(y))
print(s.difference_update(y))



#If-Else
a = True
b = True

if a:
 print( "a is true")



a = False
b = False
if a:
  print("a is True")
else:
  print("b is False")
print("True")  


#N.B: if always true carry kore,else false carry kore

a = True
b = False
c = False
if a:
  print("a is true")
elif b:
  print("b is false")
else:
  print("a is true")
print("yes")


a = True
b = True
c = False

if a:
 print( "a is true")
elif c:
 print("c is false")
else:
 print("a is true")
print("yes")


a = False
b = True
c = True

if a:
 print( "a is true")
elif c:
 print("c is false")
else:
 print("a is true")
print("yes")


 #Even-Odd 
number = int(input("Enter a number: "))
if (number % 2) == 0:
  print("The number is even")
else:
  print("The number is odd")
  
#or
num = int(input("Enter a number: "))
if (num % 2) > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

    
#negative positive
number = int(input("Enter a number: "))
if number > 0:
    print("This is an positive number.")
else:
    print("This is an Negative number.")
