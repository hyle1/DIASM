# main.py
from polylib import area_of_triangle

if __name__ == "__main__":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print(f"The area of the triangle is {area_of_triangle(base, height)}")
