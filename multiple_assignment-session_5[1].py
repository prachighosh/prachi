Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=[2,3,4,"Hi",4]
>>> print(a)
[2, 3, 4, 'Hi', 4]
>>> a[0]
2
>>> a[1]
3
>>> a[2]
4
>>> a[3]
'Hi'
>>> a[4]
4
>>> a[20]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a[20]
IndexError: list index out of range
>>> a[2]
4
>>> a[2]=5
>>> a[2]
5
>>> a
[2, 3, 5, 'Hi', 4]
>>> b=(a,b,c,d)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b=(a,b,c,d)
NameError: name 'b' is not defined
>>> a=5
>>> b=10
>>> c=30
>>> b=(a,b,c)
>>> print(b)
(5, 10, 30)
>>> 
>>> b(2)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    b(2)
TypeError: 'tuple' object is not callable
>>> b[2]
30
>>> b[1]
10
>>> b=(a,b,c)
>>> b[1]=4
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b[1]=4
TypeError: 'tuple' object does not support item assignment
>>> a[1]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a[1]
TypeError: 'int' object is not subscriptable
>>> a=[2,3,4,"Hi",4]
>>> a[2]
4
>>> a[2]=2222
\
>>> a
[2, 3, 2222, 'Hi', 4]
>>> a[3][0]
'H'
>>> a[3][1]
'i'
>>> a="prachi"
>>> a
'prachi'
>>> a[3]
'c'
>>> a[3]=g
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a[3]=g
NameError: name 'g' is not defined
>>> a[3]='g'
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a[3]='g'
TypeError: 'str' object does not support item assignment
>>> a=['hi','hello','prachi']
>>> a
['hi', 'hello', 'prachi']
>>> a[1]="hey"
>>> a
['hi', 'hey', 'prachi']
>>> a[2][1]
'r'
>>> a[2][1]='g'
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a[2][1]='g'
TypeError: 'str' object does not support item assignment
>>> 
