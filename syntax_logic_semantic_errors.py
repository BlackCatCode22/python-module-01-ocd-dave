#    >>> primt 'Hello world!'
#    File "<stdin>", line 1
#        primt 'Hello world!'
#              ^^^^^^^^^^^^^^
#    SyntaxError: invalid syntax

#    >>> primt ('Hello world')
#    Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
#    NameError: name 'primt' is not defined. Did you mean: 'print'?

#    >>> I hate you Python!
#    File "<stdin>", line 1
#        I hate you Python!
#          ^^^^
#    SyntaxError: invalid syntax
#    >>> if you come out of there, I would teach you a lesson
#    File "<stdin>", line 1
#        if you come out of there, I would teach you a lesson
#               ^^^^
#    SyntaxError: invalid syntax
#    >>>


print 'Hello world!'
File "<stdin>", line 1
print('Hello world!')
      ^^^^^^^^^^^^^^
SyntaxError: invalid syntax

print('Hello world')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'primt' is not defined. Did you mean: 'print'?

>>> I hate you Python!
File "<stdin>", line 1
    I hate you Python!
      ^^^^
SyntaxError: invalid syntax
>>> if you come out of there, I would teach you a lesson
File "<stdin>", line 1
    if you come out of there, I would teach you a lesson
           ^^^^
SyntaxError: invalid syntax
>>>