if 1 == int:
    print("integer")
else:
    print("float")

'''
Lab 1.02 - Using the Interpreter
Part 1
Using the interpreter, type in the expressions below. Copy and paste the output into the output column. If the
result is unexpected, note that in the third column.
Section 1
    Input                   Output                          Did it do something unexpected?
a   5 + 2 * 2                 9                                        no
b   2/3                       .66 rep.                                 no
c   2.0 * 1.5                  3.0                                     no
d   (2 + 3) * 10               50                                      no
e   5.0 // 2                   2.0
f   5.0 % 2                    1.0

Section 2
    Input                   Output                          Did it do something unexpected?
a   a                NameError: name 'a' is not defined
b   'a'                       'a'  

Section 3
    Input                   Output                          Did it do something unexpected?
a   'a + b'                   'a + b'
b   'a' + 'b'                 'ab'

Section 4
    Input                   Output                          Did it do something unexpected?
a   'a' * 'b'                you can't multiply strings
b   'a' * 2                  'aa'                                     I didn't know you could do that

Part 2
Before going to the IDE
1. For each item, predict the data type of the result and enter into the "String/Integer/Float" column.
2. Next, predict the value of the result for each item and enter into it into the "Prediction of Result"
column.

    Expression                  String/Integer/Float        Prediction of Result                Interpreter Result
a   10 * 2                      integer                     20                                  20
b   .5 * 2                      integer                     1.0                                 1.0 / float
c   10/2                        integer                     5                                   5.0 / float
d   10%2                        integer                     0                                   0   / float
e   2 ** 3                      integer                     8                                   8
f   (2+5)*3                     integer                     21                                  21
g   2 + 5 * 3                   integer                     17                                  17
h   'ab' + '12' + '3'           string                      'ab123'                             'ab123'
i   x                           float                       error                               error
j   "ab" + "cd"                 string                      'abcd'                              'abcd'
k   'abc' * 2                   string                      'abcabc'                            'abcabc'
l   '1'*2 + '2' * 3             string                      '11222'                             '11222'
m   1 * 2 + '3' * 2             error                       error                                error
n   'A' ** 2                    error?                      might turn it lowercase or error     error                         
o   'bc' % 2                    error                       error                                error
p   'bc' / 2                    error                       error or 'b''c'                      error

Now go to the IDE
Use the interpreter to evaluate the expressions, write down results in the "Interpreter Result" column.
'''