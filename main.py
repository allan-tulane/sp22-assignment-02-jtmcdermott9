"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
			
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
    ### TODO
  xvec = x.binary_vec
	yvec = y.binary_vec
	if x.decimal_val <= 1 and y.decimal_val <= 1:
		return BinaryNumber(x.decimal_val * y.decimal_val)

	else:
		xvec, yvec = pad(xvec, yvec)

		xL,xR = split_number(xvec)
		yL, yR = split_number(yvec)

		left = bit_shift(_quadratic_multiply(xL, yL), len(xvec))
		midleft = subquadratic_multiply(xL, yR)
		midright = subquadratic_multiply(xR, xL)
		right = subquadratic_multiply(xR, yR)
		middle = (xL.decimal_val + xR.decimal_val) * (yL.decimal_val + yR.decimal_val) - left.decimal_val - right.decimal_val
		#middle = BinaryNumber(
		middle = bit_shift(middle, len(xvec)//2)

		return BinaryNumber(left.decimal_val + 
           middle.decimal_val + right.decimal_val)



		
	
    ###

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2

def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000

    
    

