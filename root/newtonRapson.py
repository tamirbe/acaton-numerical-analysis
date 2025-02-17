def newton_raphson(f, df, p0, TOL, N=50):
    print("{:<10} {:<15} {:<15} ".format("Iteration", "po", "p1"))
    for i in range(N):
        if df(p0) == 0:
            print( "Derivative is zero at p0, method cannot continue.")
            return

        p = p0 - f(p0) / df(p0)

        if abs(p - p0) < TOL:
            return p  # Procedure completed successfully
        print("{:<10} {:<15.9f} {:<15.9f} ".format(i, p0, p))
        p0 = p
    return p

def main(f=None, df=None, p0=None, TOL=None, N=None):
    f = lambda x: x**3 - 3*x**2
    df = lambda x: 3*x**2 - 6*x
    p0 = -5
    TOL = 1e-6
    N = 100
    roots = newton_raphson(f, df,p0,TOL,N)
    print("\nThe equation f(x) has an approximate root at x = {:<15.9f} ".format(roots))
    return roots

if __name__ == '__main__':
    main()
