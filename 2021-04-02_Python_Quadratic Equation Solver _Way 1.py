#Quadratic Equation Solver in Python
#python- Computer Programming Tuttor- April 2, 2021

print("Enter the Coefficients of equation : ax^2 + bx +c =0")

a = float(input("Value of a = "))
b = float(input("Value of b = "))
c = float(input("Value of c = "))
if a==0:
    print("Invalid, It is  Not a quadratic equation")
    if b==0:
        print("there is no x")
    else:
        x1= -b/c
        print("x1 = " + str(x1))
else:
    if b**2 -4*a*c<0:
        print("No Real Roots")
    else:
        x1= (-b+(b**2-4*a*c)**0.5)/(2*a)
        x2= (-b-(b**2-4*a*c)**0.5)/(2*a)
        #print("x1= " + str(x1))
        #print("x2= " + str(x2))
        print("x1= " + str("%.4f"%x1))
        print("x2= " + str("%.3f"%x2))

        

        
        



#"%.2f"%
        
