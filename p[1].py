Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=10
>>> a=b
>>> b=a
>>> a
10
>>> b
10
>>> a=5
>>> b=10
>>> c=5
>>> a=b
>>> b=c
>>> a
10
>>> b
5
>>> a=5
>>> b=10
>>> a,b=b,a
>>> a
10
>>> b
5
>>> a=b+c
>>> b=a+c
>>> a=b
>>> b=a
>>> a
15
>>> b
15
>>> a,b,c=5,10,5
>>> a
5
>>> b
10
>>> c
5
>>> 
