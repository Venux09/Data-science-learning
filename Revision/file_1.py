#buildings an simple perceptron from the scratch 






def step(x):
    return 1 if x >= 0 else 0 

def perceptron(x1,x2,w1,w2,b):
    z = x1*w1 + x2*w2 +b #perceptron formula for the application of the perceptron           

    return step(z) 

print(perceptron(0,0,1,1,-1.5))#values for the perceptron weights and inputs and also the same bias for the every equestion 
print(perceptron(1,1,1,1,-1.5))
print(perceptron(1,0,1,1,-1.5))
print(perceptron(0,1,1,1,-1.5))




