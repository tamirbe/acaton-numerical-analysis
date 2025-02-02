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
    result = romberg(f,0,1,5)
    print(f"The romberg method solution (Group 2): {8000*result}")
    result = trap(f,0,1,5)
    print(f"The trapezodial method solution (Group 2): {8000*result}")
    # excersize 3
    f = lambda x: (math.cos(x**2 + 5*x + 6)) / (2 * math.exp(-x))
    result = bisection(f, -1.5,2)
    print(f"The bistection solution (Group 2): {2500*result}")
    df = lambda x: (-math.sin(x**2 + 5*x + 6) * (2*x + 5) + math.cos(x**2 + 5*x + 6)) / (2 * math.exp(-x))
    result = newt_raph(f,df,-1.5,1e-6,100)
    print(f"The newton-raphson solution (Group 2): {2500*result}")

