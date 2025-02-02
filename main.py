from integration.Romberg_method import main as romberg
from integration.Trapezoidal_method import main as trap
from root.bisection_method import main as bisection
from root.newtonRapson import main as newt_raph
from interpolation.lagrange_interpolation import main as lagrange
from interpolation.neville_method import main as neville
import math

if __name__ == '__main__':
    # excersize 2
    f = lambda x: (math.sin(x**2 + 5*x + 6)) / (2 * math.exp(-x))
    print("\nExcersize 2:\n")
    result = romberg(f,0,1,5)
    print(f"The romberg method solution (Group 2): {8000*result}")
    result = trap(f,0,1,5)
    print(f"The trapezodial method solution (Group 2): {8000*result}")
    # excersize 3
    f = lambda x: (math.cos(x**2 + 5*x + 6)) / (2 * math.exp(-x))
    print("\nExcersize 3:\n")
    result = bisection(f, -1.5,2)
    print(f"The bistection solution (Group 2): {2500*result}")
    df = lambda x: (-math.sin(x**2 + 5*x + 6) * (2*x + 5) + math.cos(x**2 + 5*x + 6)) / (2 * math.exp(-x))
    result = newt_raph(f,df,-1.5,1e-6,100)
    print(f"The newton-raphson solution (Group 2): {2500*result}")
     # excersize 8
    f = lambda x: (math.sin(x**3 + 5*x**2 - 6)) / (2 * math.exp(-2*x))
    print("\nExcersize 8:\n")
    result = romberg(f,0,1,5)
    print(f"The romberg method solution (Group 2): {1300*result}")
    result = trap(f,0,1,5)
    print(f"The trapezodial method solution (Group 2): {1300*result}")   
    # excersize 34
    x_data = [0.2 , 0.35, 0.45, 0.6,0.75,0.85,0.9]
    y_data = [13.7241,13.9776,14.0625,13.9776,13.7241,13.3056,12.7281]
    x_interpolation = 0.65
    print("\nExcersize 34:")
    result = lagrange(x_data,y_data,x_interpolation)
    print(f"The lagrange interpolation method solution (Group 2): {700*result}")
    result = neville(x_data,y_data,x_interpolation)
    print(f"The neville method solution (Group 2): {700*result}")
    # excersize 35
    x_data = [0.35 , 0.4, 0.55, 0.65,0.7,0.85,0.9]
    y_data = [-213.5991,-204.4416,-194.9375,-185.0256,-174.6711,-163.8656,-152.6271]
    x_interpolation = 0.75
    print("\nExcersize 35:")
    result = lagrange(x_data,y_data,x_interpolation)
    print(f"The lagrange interpolation method solution (Group 2): {200*result}")
    result = neville(x_data,y_data,x_interpolation)
    print(f"The neville method solution (Group 2): {200*result}")   