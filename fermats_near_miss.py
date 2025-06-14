#!/usr/bin/env python3
"""
Title: Fermat's Last Theorem Near Miss Finder
Filename: fermats_near_miss.py
External files necessary: None
External files created: None
Programmers: Mario Opoku Adusei
Email address: MarioJOpokuAdusei@lewisu.edu
Course: SU25-CPSC-60500-001
Date: June 14, 2025

Program Description:
    This program searches for "near misses" of Fermat's Last Theorem, which states
    that there are no positive integers x, y, and z such that x^n + y^n = z^n for n > 2.
    The program prompts the user for values of n (the power) and k (the upper limit for x and y),
    then systematically searches for combinations where x^n + y^n is close to z^n for some integer z.
    For each x,y combination, it finds integers z and z+1 that "bracket" (x^n + y^n),
    calculates the "miss" as the smallest of [(x^n + y^n) - z^n] or [(z+1)^n - (x^n + y^n)],
    and tracks the smallest relative miss found.

Resources Used:
    - Python documentation for math and time modules
    - Fermat's Last Theorem description: https://www.youtube.com/watch?v=ReOQ300AcSU
"""
import math  # Used for mathematical operations
import time  # Used for tracking execution time


def calculate_z_value(sum_value, n):
    """
    Calculate the z value that brackets the sum_value.
    
    Parameters:
        sum_value: The value of x^n + y^n
        n: The power used in the equation
    
    Returns:
        z: An integer such that z^n < sum_value < (z+1)^n
    """
    # Calculate the nth root of sum_value to get an approximate z
    z_float = sum_value ** (1/n)  # Floating point approximation of the nth root
    z = int(z_float)  # Convert to integer (floor of z_float)
    
    # Ensure z^n < sum_value < (z+1)^n
    if z**n >= sum_value:
        z -= 1  # Adjust z downward if necessary to ensure proper bracketing
    
    return z


def calculate_miss(x, y, z, n):
    """
    Calculate the absolute and relative miss for a given x, y, z, n combination.
    
    Parameters:
        x, y: The base numbers in the equation x^n + y^n
        z: The bracketing integer
        n: The power used in the equation
    
    Returns:
        A tuple containing:
        - absolute_miss: The absolute difference between x^n + y^n and the closest of z^n or (z+1)^n
        - relative_miss: The absolute miss divided by (x^n + y^n)
        - is_lower_z: Boolean indicating whether z^n (True) or (z+1)^n (False) is closer
    """
    sum_value = x**n + y**n  # Calculate the sum x^n + y^n
    lower_miss = sum_value - z**n  # Difference between sum and z^n
    upper_miss = (z+1)**n - sum_value  # Difference between (z+1)^n and sum
    
    # Determine which is the smaller miss
    if lower_miss <= upper_miss:
        return lower_miss, lower_miss / sum_value, True
    else:
        return upper_miss, upper_miss / sum_value, False


def find_near_misses(n, k):
    """
    Find near misses for Fermat's Last Theorem with the given parameters.
    
    Parameters:
        n: The power to use in the equation (2 < n < 12)
        k: The upper limit for x and y values (k > 10)
    
    This function systematically checks all combinations of x and y within the range,
    tracks the smallest relative miss found, and displays results.
    """
    best_relative_miss = float('inf')  # Initialize with infinity to ensure first result is captured
    best_result = None  # Will store the tuple (x, y, z, abs_miss, rel_miss) of the best result
    
    # Count the total number of combinations to check for progress reporting
    total_combinations = (k - 9) * (k - 9)
    combinations_checked = 0  # Counter for tracking progress
    
    print(f"\nSearching for near misses with n={n} and k={k}...")
    print("This may take some time depending on the values of n and k.")
    print("New best results will be displayed as they are found.\n")
    
    start_time = time.time()  # Record start time for performance tracking
    
    # Loop through all possible x, y combinations within the specified range
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            combinations_checked += 1
            
            # Calculate x^n + y^n
            sum_value = x**n + y**n
            
            # Find the z value that brackets the sum
            z = calculate_z_value(sum_value, n)
            
            # Calculate the miss
            abs_miss, rel_miss, is_lower_z = calculate_miss(x, y, z, n)
            
            # Check if this is a new best result (smaller relative miss)
            if rel_miss < best_relative_miss:
                best_relative_miss = rel_miss  # Update the best relative miss
                best_z = z if is_lower_z else z + 1  # Store the z value that's closer
                best_result = (x, y, best_z, abs_miss, rel_miss)  # Store the complete result
                
                # Print the new best result for the user to see progress
                print(f"New best result found!")
                print(f"  x = {x}, y = {y}, z = {best_z}")
                print(f"  {x}^{n} + {y}^{n} {'<' if is_lower_z else '>'} {best_z}^{n}")
                print(f"  Absolute miss: {abs_miss}")
                print(f"  Relative miss: {rel_miss:.10%}")
                print(f"  Progress: {combinations_checked}/{total_combinations} combinations checked ({combinations_checked/total_combinations:.2%})")
                print()
            
            # Periodically show progress to keep the user informed during long runs
            if combinations_checked % 10000 == 0:
                elapsed_time = time.time() - start_time
                print(f"Progress: {combinations_checked}/{total_combinations} combinations checked ({combinations_checked/total_combinations:.2%})")
                print(f"Elapsed time: {elapsed_time:.2f} seconds")
                print(f"Current best relative miss: {best_relative_miss:.10%}")
                print()
    
    elapsed_time = time.time() - start_time  # Calculate total execution time
    
    # Print final results with clear formatting
    print("\n" + "="*50)
    print("SEARCH COMPLETE")
    print("="*50)
    if best_result:
        x, y, z, abs_miss, rel_miss = best_result
        print(f"Best near miss found:")
        print(f"  x = {x}, y = {y}, z = {z}")
        print(f"  {x}^{n} + {y}^{n} {'≈'} {z}^{n}")
        print(f"  {x}^{n} + {y}^{n} = {x**n + y**n}")
        print(f"  {z}^{n} = {z**n}")
        print(f"  Absolute miss: {abs_miss}")
        print(f"  Relative miss: {rel_miss:.10%}")
    else:
        print("No valid near misses found.")
    
    print(f"\nTotal time: {elapsed_time:.2f} seconds")
    print(f"Total combinations checked: {combinations_checked}")


def main():
    """
    Main function to run the program.
    
    Handles user input, validation, and calls the search function.
    """
    print("="*50)
    print("Fermat's Last Theorem Near Miss Finder")
    print("="*50)
    print("This program searches for 'near misses' of Fermat's Last Theorem,")
    print("which states that there are no positive integers x, y, and z such")
    print("that x^n + y^n = z^n for any n > 2.")
    print("\nThe program will search for values where x^n + y^n is close to z^n.")
    
    # Get user input for n with validation to ensure it's within the required range
    while True:
        try:
            n = int(input("\nEnter n (power to use, 2 < n < 12): "))
            if 2 < n < 12:
                break  # Valid input, exit the loop
            else:
                print("Error: n must be between 3 and 11 inclusive.")
        except ValueError:
            print("Error: Please enter a valid integer.")
    
    # Get user input for k with validation to ensure it's greater than 10
    while True:
        try:
            k = int(input("Enter k (upper limit for x and y, k > 10): "))
            if k > 10:
                break  # Valid input, exit the loop
            else:
                print("Error: k must be greater than 10.")
        except ValueError:
            print("Error: Please enter a valid integer.")
    
    # Find near misses using the validated parameters
    find_near_misses(n, k)
    
    # Keep the console open so the user can review the results
    input("\nPress Enter to exit...")


# Program entry point
if __name__ == "__main__":
    main()
