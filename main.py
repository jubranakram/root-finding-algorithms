from utils import *

if __name__ == '__main__':
    
    f = lambda x: x**2 - 7*x + 10
    f_der = lambda x: 2*x - 7
    
    # Incremental Search to find the number of roots and the corresponding intervals
    # ------------------------------------------------------------------------------
    roots_info = incremental_search(f, -4, 8, 0.8)
    print(f"Number of roots: {roots_info[0]}")
    
    # Roots obtained from using the Bisection method
    for idx in range(roots_info[0]):
        lb = roots_info[1][idx][0]
        ub = roots_info[1][idx][1]
        print(f"Bisection method: root in the interval {idx}: {bisection(f, lb, ub):.3f}")
        
    # Roots obtained from using the False position or linear interpolation method
    for idx in range(roots_info[0]):
        lb = roots_info[1][idx][0]
        ub = roots_info[1][idx][1]
        print(f"False position method: root in the interval {idx}: {false_position(f, lb, ub):.3f}")
        
    # Roots obtained from using the Newton-Raphson method
    for idx in range(roots_info[0]):
        x0 = ( roots_info[1][idx][0] + roots_info[1][idx][1] ) / 2
        print(f"Newton-Raphson method: root in the interval {idx}: {newton_raphson(f, f_der, x0):.3f}")
        
    # Roots obtained from using the secant method
    for idx in range(roots_info[0]):
        x0 = roots_info[1][idx][0]
        x1 = roots_info[1][idx][1]
        print(f"Secant method: root in the interval {idx}: {secant(f, x0, x1):.3f}")
        
    # Roots obtained from using the modified secant method
    for idx in range(roots_info[0]):
        x0 = roots_info[1][idx][0]
        dx = 0.1
        print(f"Modified secant method: root in the interval {idx}: {secant(f, x0, dx):.3f}")