# & (Binary AND)  Operator copies a bit to the result if it exists in both operands

a1 = 7
b1 = 5
print(a1 & b1)  # it basically performs AND operatin on each bit  (7=111 and 5=101)

# | (Binary OR)	It copies a bit if it exists in either operand.
print(a1 | b1)  # it basically performs OR operation on each bit.

# ^ (Binary XOR)	It copies the bit if it is set in one operand but not both.
print(a1 ^ b1)  # it basically performs XOR operation on each bit.

# ~ Binary Ones Complement	It is unary and has the effect of 'flipping' bits.
c1 = ~a1
c2 = ~b1
print(c1)
print(c2)

# << (Binary Left Shift)	The left operands value is moved left by the number of bits specified by the right operand.
a2 = 60
print(a2 << 2)  # 60= 0011 1100  and a2<<2 =240 =1111 0000

# >> Binary Right Shift	The left operands value is moved right by the number of bits specified by the right operand.
print(a2 >> 2)  #a2>>2=15=0000 1111
