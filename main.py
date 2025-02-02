from integration.Romberg_method import main as romberg
from integration.Trapezoidal_method import main as trap
from root.bisection_method import main as bisection
from root.newtonRapson import main as newt_raph

if __name__ == '__main__':
    romberg()
    trap()
    bisection()
    newt_raph()
