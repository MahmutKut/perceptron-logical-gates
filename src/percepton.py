# EXAMPLE : FIND THE TRUE WEIGHT VALUE
"""
----------- AND TABLE -----------
input[0]    input[1]   |   output
    0           0      |     0
    0           1      |     0
    1           0      |     0
    1           1      |     1    
"""

input       = [(0,0),(0,1),(1,0),(1,1)]
output      = [0,0,0,1]

w0     = 1
w1     = 1
w2     = 1

bias            = -5
learing_rate    = 2

iteration       = 0
result          = list()

#Rule-1:
# bias*w0+x1*w1+x2*w2 > 0 ---> 1
# bias*w0+x1*w1+x2*w2 < 0 ---> 0

#Rule-2:
# if (result != output)   ---> error = output - result

#New weights:
# w1 = w1 + learing_rate * error * x1
# w2 = w2 + learing_rate * error * x2

while True:

    for i in range (len(input)):
        x1  = input[i][0]
        x2  = input[i][1]
        equation = bias*w0+x1*w1+x2*w2

        if(equation>0):
            result.append(1) 
        else:
            result.append(0) 

        if(result[i] == output[i]):
           continue
        else:
            error = output[i] - result[i]
            w1 = w1 + learing_rate * error * x1
            w2 = w2 + learing_rate * error * x2
    if(result == output):
        print("Last w1 ---> "           +str(w1))
        print("Last w2 ---> "           +str(w2))
        print("Total Iteration ---> "   +str(iteration))
        break
    else:
        result.clear()
    iteration = iteration + 1 
  

    