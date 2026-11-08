import math

# Function 1: T(n) = T(n-1) + 1
def fun1_decreasing(n: int) -> None:
    if n > 0:
        print(f"fun1: n = {n}")
        fun1_decreasing(n - 1)

# Function 2: T(n) = T(n-1) + n
def fun2_decreasing(n: int) -> None:
    if n > 0:
        for i in range(n):
            pass  # O(n) iteration work
        print(f"fun2: n = {n}")
        fun2_decreasing(n - 1)

# Function 3: T(n) = T(n-1) + log n
def fun3_decreasing(n: int) -> None:
    if n > 0:
        i = 1
        while i < n:
            i *= 2  # O(log n) work
        print(f"fun3: n = {n}")
        fun3_decreasing(n - 1)

# Function 4: T(n) = 2T(n-1) + 1
def fun4_decreasing(n: int) -> None:
    if n > 0:
        print(f"fun4: n = {n}")
        fun4_decreasing(n - 1)
        fun4_decreasing(n - 1)

if __name__ == "__main__":
    print("--- Task 1 Decreasing Functions Demo ---")
    fun1_decreasing(3)
    fun2_decreasing(3)
    fun3_decreasing(3)
    fun4_decreasing(3)
