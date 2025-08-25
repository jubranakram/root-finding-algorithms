from typing import Callable, Optional, Tuple, List

def incremental_search(
    f: Callable[[float], float], 
    lb: float,
    ub: float,
    increment_length: float) -> Tuple[int, List[List[float]]]:
    
    """
    Performs the incremental search method to locate intervals where a function changes sign, indicating the presence of roots.
    Args:
        f (Callable[[float], float]): The function for which roots are to be found.
        lb (float): The lower bound of the search interval.
        ub (float): The upper bound of the search interval.
        increment_length (float): The length of each increment step within the interval.
    Returns:
        Tuple[int, List[List[float]]]: 
            - The number of intervals where a sign change (potential root) was detected.
            - A list containing the intervals [x0, x1] where sign changes occur.
    """
    intervals = []
    number_of_roots = 0
    
    while lb <= ub:
        
        if f(lb) == 0:
            number_of_roots += 1
            intervals.append([lb - increment_length, lb + increment_length])
            
        if f(lb) * f(lb + increment_length) < 0:
            number_of_roots += 1
            intervals.append([lb, lb + increment_length])
            
        lb += increment_length
        
    return number_of_roots, intervals


def bisection(
    f: Callable[[float], float], 
    lb: float,
    ub: float,
    threshold: float = 1e-3,
    max_iterations: int = 100) -> Optional[float]:    
    """
    Finds roots using the bisection method (bracketing methods).
    Args:
        f (Callable[[float], float]): The function for which roots are to be found.
        lb (float): The lower bound of the search interval.
        ub (float): The upper bound of the search interval.
        threshold (float): Stopping criterion based on precision
        max_iterations (int): Maximum number of iterations in the stopping criterion
    Returns:
        Optional[float]: 
            - Roots if present, otherwise None.            
    """
    iteration = 0   
    while lb <= ub:
        iteration += 1
        mid = (lb + ub) / 2
        if -threshold < f(mid) < threshold:
            return mid 
        elif f(lb) * f(mid) < 0:
            ub = mid 
        elif f(ub) * f(mid) < 0:
            lb = mid
            
            
        if iteration > max_iterations:
            break 
        
    return None 

def false_position(
    f: Callable[[float], float], 
    lb: float,
    ub: float,
    threshold: float = 1e-3,
    max_iterations: int = 100) -> Optional[float]:    
    """
    Finds roots using the false position or linear interpolation method (bracketing methods).
    Args:
        f (Callable[[float], float]): The function for which roots are to be found.
        lb (float): The lower bound of the search interval.
        ub (float): The upper bound of the search interval.
        threshold (float): Stopping criterion based on precision
        max_iterations (int): Maximum number of iterations in the stopping criterion
    Returns:
        Optional[float]: 
            - Roots if present, otherwise None.            
    """
    iteration = 0   
    while lb <= ub:
        iteration += 1
        x_r = ub - f(ub) * (lb - ub) / (f(lb) - f(ub))
        if -threshold < f(x_r) < threshold:
            return x_r 
        elif f(lb) * f(x_r) < 0:
            ub = x_r
        elif f(ub) * f(x_r) < 0:
            lb = x_r
            
            
        if iteration > max_iterations:
            break 
        
    return None 

def newton_raphson(
    f: Callable[[float], float], 
    f_der: Callable[[float], float],
    x0: float,
    threshold: float = 1e-3,
    max_iterations: int = 100) -> Optional[float]:    
    """
    Finds roots using the Newton-Raphson method (open methods).
    Args:
        f (Callable[[float], float]): The function for which roots are to be found.
        f_der (Callable[[float], float]): The derivation of function for which roots are to be found.
        x0 (float): The initial guess of root value.
        threshold (float): Stopping criterion based on precision
        max_iterations (int): Maximum number of iterations in the stopping criterion
    Returns:
        Optional[float]: 
            - Roots if present, otherwise None.            
    """
    iteration = 0   
    x = x0
    while True:
        iteration += 1
        x = x - f(x)/f_der(x)
        if -threshold < f(x) < threshold:
            return x 
                
        if iteration > max_iterations:
            break 
        
    return None 

def secant(
    f: Callable[[float], float], 
    x0: float,
    x1: float,
    threshold: float = 1e-3,
    max_iterations: int = 100) -> Optional[float]:    
    """
    Finds roots using the secant method (open methods).
    Args:
        f (Callable[[float], float]): The function for which roots are to be found.
        x0 (float): First initial guess.
        x1 (float): Second initial guess.
        threshold (float): Stopping criterion based on precision
        max_iterations (int): Maximum number of iterations in the stopping criterion
    Returns:
        Optional[float]: 
            - Roots if present, otherwise None.            
    """
    iteration = 0   
    while True:
        iteration += 1
        x = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if -threshold < f(x) < threshold:
            return x   
            
        if iteration > max_iterations:
            break 
        
        x0, x1 = x1, x
        
    return None 

def modified_secant(
    f: Callable[[float], float], 
    x0: float,
    dx: float,
    threshold: float = 1e-3,
    max_iterations: int = 100) -> Optional[float]:    
    """
    Finds roots using the modified secant method (open methods).
    Args:
        f (Callable[[float], float]): The function for which roots are to be found.
        x0 (float): Initial guess.
        dx (float): Perturbation.
        threshold (float): Stopping criterion based on precision
        max_iterations (int): Maximum number of iterations in the stopping criterion
    Returns:
        Optional[float]: 
            - Roots if present, otherwise None.            
    """
    iteration = 0   
    while True:
        iteration += 1
        x = x0 - f(x0) * dx / (f(x0 + dx) - f(x0))
        if -threshold < f(x) < threshold:
            return x   
            
        if iteration > max_iterations:
            break 
        
        
    return None 



            
            
            