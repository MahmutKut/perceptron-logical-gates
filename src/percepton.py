# EXAMPLE : FIND THE TRUE WEIGHT VALUE FOR AND TABLE
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


weight1     = 1
weight2     = 1
threshold   = 5
result      = list()
alfa        = 0.5          # learing rate
iteration   = 0

while True:

    for i in range (len(input)):
        if(((input[i][0]*weight1)+(input[i][1]*weight2))>threshold):
            result.append(1)
        else:
            result.append(0)

        if(result[i]!=output[i]):
            error = output[i] - result[i]
            D_weight1 = error * alfa * input[i][0]
            D_weight2 = error * alfa * input[i][1]
            weight1 = weight1 + D_weight1
            weight2 = weight2 + D_weight2
            result.clear()
            break

    iteration = iteration + 1 

    if(result == output):
        print("Weight1 ---> "+str(weight1))
        print("Weight2 ---> "+str(weight2))
        print("Iteration ---> "+str(iteration))
        break

    