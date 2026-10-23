import math

def calculate_hypotenuse():
    try:
        
        side_a = float(input("Enter the length of side A (in metres): "))
        side_b = float(input("Enter the length of side B (in metres): "))
        
        if side_a <= 0 or side_b <= 0:
            print("Error: A side that is zero or negative must be rejected.")
            return

        hypotenuse = math.sqrt(side_a**2 + side_b**2)
        
        print(f"The length of the hypotenuse is: {hypotenuse:.2f} metres")
        
    except ValueError:
        print("Error: Please enter valid numerical values.")

calculate_hypotenuse()
