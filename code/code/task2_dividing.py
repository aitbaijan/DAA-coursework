# Function 1: T(n) = T(n/2) + 1
def fun1_dividing(n: int) -> None:
    if n > 1:
        print(f"fun1_div: n = {n}")
        fun1_dividing(n // 2)

# Function 2: T(n) = T(n/2) + n
def fun2_dividing(n: int) -> None:
    if n > 1:
        for i in range(n):
            pass  # O(n) iteration work
        print(f"fun2_div: n = {n}")
        fun2_dividing(n // 2)

# Function 3: T(n) = 2T(n/2) + n
def fun3_dividing(n: int) -> None:
    if n > 1:
        for i in range(n):
            pass  # O(n) iteration work
        print(f"fun3_div: n = {n}")
        fun3_dividing(n // 2)
        fun3_dividing(n // 2)

if __name__ == "__main__":
    print("--- Task 2 Dividing Functions Demo ---")
    fun1_dividing(8)
    fun2_dividing(8)
    fun3_dividing(8)
