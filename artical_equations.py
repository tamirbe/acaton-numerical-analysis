import math

def calculate_metrics(L):
    # Equation (1)
    D1 = 4.86 + 0.018 * L
    
    # Equation (2)
    D2 = L / 3000
    
    # Equation (3) constants for Fortran
    A0, A1, A2 = 0.0047, 0.0023, 0.000043
    D3 = A0 + A1 * math.log2(L) + A2 * (math.log2(L) ** 2)
    
    # Equation (4)
    D4 = 4.2 + 0.0015 * (L ** (4/3))
    
    # Equation (5)
    D5 = 0.069 + 0.00156 * L + 0.00000047 * (L ** 2)
    
    return {
        "Equation 1 (D1)": D1,
        "Equation 2 (D2)": D2,
        "Equation 3 (D3)": D3,
        "Equation 4 (D4)": D4,
        "Equation 5 (D5)": D5
    }

def main(L=None):
    results = calculate_metrics(L)
    for eq, value in results.items():
        print(f"{eq}: {value:.4f}")

if __name__ == '__main__':
    main()