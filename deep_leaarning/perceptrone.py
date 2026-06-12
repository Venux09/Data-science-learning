def step(x):
    return 1 if x>= 0 else 0 

def perceptron(x1,x2,x3,x4,w1,w2,w3 , w4 , b):
    z = x1*w1+x2*w2+x3*w3+x4*w4+b 

    return(step(z))

print(perceptron(1,0,1,0,1,1,1,1,-1.5))
print(perceptron(0,1,0,0,1,1,1,1,-1.5))
print(perceptron(0,0,1,0,1,1,1,1,-1.5))
print(perceptron(1,1,1,1,1,1,1,1,-1.5))