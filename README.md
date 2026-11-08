# Coursework: Recurrence Relations and Master Theorem

**Subject:** CS 301: Design and Analysis of Algorithms (Fall 2026)  
**Author:** aitbaijan  

---

## Theoretical Background

### 1. Master Theorem for Decreasing Recurrences
For recurrence relations of the form:
$$T(n) = a T(n - b) + f(n)$$
where $a \ge 1$, $b > 0$, and $f(n) = O(n^k)$ with $k \ge 0$:

1. **Case 1 ($a < 1$):** $T(n) = O(f(n))$
2. **Case 2 ($a = 1$):** $T(n) = O(n \cdot f(n)) = O(n^{k+1})$
3. **Case 3 ($a > 1$):** $T(n) = O(a^{n/b} \cdot f(n)) = O(a^{n/b})$

---

### 2. Master Theorem for Dividing Recurrences
For recurrence relations of the form:
$$T(n) = a T(n / b) + f(n)$$
where $a \ge 1$, $b > 1$, compare $f(n)$ with $n^{\log_b a}$:

1. **Case 1:** If $f(n) = O(n^{\log_b a - \epsilon})$ for some $\epsilon > 0$, then $T(n) = \Theta(n^{\log_b a})$.
2. **Case 2:** If $f(n) = \Theta(n^{\log_b a} \log^k n)$ for $k \ge 0$, then $T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$.
3. **Case 3:** If $f(n) = \Omega(n^{\log_b a + \epsilon})$ for some $\epsilon > 0$, and $a f(n/b) \le c f(n)$ for $c < 1$, then $T(n) = \Theta(f(n))$.

---

## Task 1: Decreasing Functions

### Function 1: $T(n) = T(n-1) + 1$

#### 1. Derivation from Code
```java
void fun(int n) {
    if (n > 0) {
        System.out.println(n); // O(1) work outside recursion
        fun(n - 1);           // 1 recursive call with size (n - 1)
    }
}
```
- **Identification:** $a = 1$, $b = 1$, $f(n) = 1 = O(1)$.

#### 2. Step-by-Step Manual Solution (Substitution Method)
$$T(n) = T(n-1) + 1$$
$$T(n) = [T(n-2) + 1] + 1 = T(n-2) + 2$$
$$T(n) = T(n-k) + k$$
Base case is reached when $n - k = 0 \implies k = n$:
$$T(n) = T(0) + n = O(n)$$

#### 3. Recursion Depth & Tree Diagram
- **Recursion Depth:** $n$
- **Recursion Tree:**
```text
(n)           --> Work: 1
 |
(n-1)         --> Work: 1
 |
(n-2)         --> Work: 1
 |
...
 |
(0)           --> Work: 1
Total Work = 1 + 1 + ... + 1 (n times) = n -> O(n)
```

#### 4. Master Theorem Application
- Parameters: $a = 1, b = 1, f(n) = O(1)$ ($k = 0$).
- **Applicable Case:** Case 2 ($a = 1$).
- **Result:** $T(n) = O(n \cdot f(n)) = O(n \cdot 1) = O(n)$.
- **Comparison:** Manual substitution and Master Theorem both yield $O(n)$.

---

### Function 2: $T(n) = T(n-1) + n$

#### 1. Derivation from Code
```java
void fun(int n) {
    if (n > 0) {
        for (int i = 0; i < n; i++) { } // O(n) work per call
        System.out.println(n);
        fun(n - 1);                     // 1 recursive call
    }
}
```
- **Identification:** $a = 1$, $b = 1$, $f(n) = n = O(n)$.

#### 2. Step-by-Step Manual Solution
$$T(n) = T(n-1) + n$$
$$T(n) = T(n-2) + (n-1) + n$$
$$T(n) = T(0) + \sum_{i=1}^{n} i = \frac{n(n+1)}{2} = O(n^2)$$

#### 3. Recursion Depth & Tree Diagram
- **Recursion Depth:** $n$
- **Recursion Tree:**
```text
(n)           --> Work: n
 |
(n-1)         --> Work: n - 1
 |
(n-2)         --> Work: n - 2
 |
...
 |
(1)           --> Work: 1
Total Work = n + (n-1) + ... + 1 = n(n+1)/2 -> O(n^2)
```

#### 4. Master Theorem Application
- Parameters: $a = 1, b = 1, f(n) = n$ ($k = 1$).
- **Applicable Case:** Case 2 ($a = 1$).
- **Result:** $T(n) = O(n \cdot f(n)) = O(n \cdot n) = O(n^2)$.
- **Comparison:** Both manual summation and Master Theorem produce $O(n^2)$.

---

### Function 3: $T(n) = T(n-1) + \log n$

#### 1. Derivation from Code
```java
void fun(int n) {
    if (n > 0) {
        for (int i = 1; i < n; i = i * 2) { // O(log n) loop work
            System.out.println(n);
        }
        fun(n - 1);                         // 1 recursive call
    }
}
```
- **Identification:** $a = 1$, $b = 1$, $f(n) = \log n$.

#### 2. Step-by-Step Manual Solution
$$T(n) = T(n-1) + \log n$$
$$T(n) = T(0) + \sum_{i=1}^{n} \log i = \log(n!) = O(n \log n)$$

#### 3. Recursion Depth & Tree Diagram
- **Recursion Depth:** $n$
- **Recursion Tree:**
```text
(n)           --> Work: log(n)
 |
(n-1)         --> Work: log(n-1)
 |
...
 |
(1)           --> Work: log(1)
Total Work = log(n) + log(n-1) + ... + log(1) = log(n!) -> O(n log n)
```

#### 4. Master Theorem Application
- Parameters: $a = 1, b = 1, f(n) = \log n$.
- **Applicable Case:** Case 2 ($a = 1$).
- **Result:** $T(n) = O(n \cdot f(n)) = O(n \log n)$.
- **Comparison:** Both methods give $O(n \log n)$.

---

### Function 4: $T(n) = 2T(n-1) + 1$

#### 1. Derivation from Code
```java
void fun(int n) {
    if (n > 0) {
        System.out.println(n); // O(1)
        fun(n - 1);           // Recursive call 1
        fun(n - 1);           // Recursive call 2
    }
}
```
- **Identification:** $a = 2$, $b = 1$, $f(n) = 1$.

#### 2. Step-by-Step Manual Solution
$$T(n) = 2 T(n-1) + 1$$
$$T(n) = 2[2 T(n-2) + 1] + 1 = 4 T(n-2) + 2 + 1$$
$$T(n) = 2^k T(n-k) + \sum_{i=0}^{k-1} 2^i$$
At $k = n$:
$$T(n) = 2^n T(0) + (2^n - 1) = O(2^n)$$

#### 3. Recursion Depth & Tree Diagram
- **Recursion Depth:** $n$
- **Recursion Tree:**
```text
          (n)               --> Work: 1
        /     \
    (n-1)     (n-1)         --> Work: 2 * 1 = 2
    /   \     /   \
  (n-2)(n-2)(n-2)(n-2)      --> Work: 4 * 1 = 4
Total Work = 1 + 2 + 4 + ... + 2^(n-1) = 2^n - 1 -> O(2^n)
```

#### 4. Master Theorem Application
- Parameters: $a = 2, b = 1, f(n) = 1$.
- **Applicable Case:** Case 3 ($a > 1$).
- **Result:** $T(n) = O(a^{n/b} \cdot f(n)) = O(2^n \cdot 1) = O(2^n)$.
- **Comparison:** Both tree expansion and Master Theorem give $O(2^n)$.

---

### Summary Table of Task 1

| Function | Recurrence | $a$ | $b$ | $f(n)$ | Master Theorem Case | Asymptotic Time Complexity |
|---|---|---|---|---|---|---|
| **Fun 1** | $T(n) = T(n-1) + 1$ | 1 | 1 | $O(1)$ | Case 2 ($a=1$) | $O(n)$ |
| **Fun 2** | $T(n) = T(n-1) + n$ | 1 | 1 | $O(n)$ | Case 2 ($a=1$) | $O(n^2)$ |
| **Fun 3** | $T(n) = T(n-1) + \log n$ | 1 | 1 | $O(\log n)$ | Case 2 ($a=1$) | $O(n \log n)$ |
| **Fun 4** | $T(n) = 2T(n-1) + 1$ | 2 | 1 | $O(1)$ | Case 3 ($a>1$) | $O(2^n)$ |

---

## Task 2: Dividing Functions

### Function 1: $T(n) = T(n/2) + 1$

#### 1. Derivation from Code
```java
void fun(int n) {
    if (n > 1) {
        System.out.println(n); // O(1) work
        fun(n / 2);           // 1 call with size n/2
    }
}
```
- **Identification:** $a = 1$, $b = 2$, $f(n) = 1$.

#### 2. Recursion Tree Analysis
- **Number of calls at level $i$:** $1$
- **Input size at level $i$:** $n / 2^i$
- **Work performed at level $i$:** $1$
- **Height of Tree:** $\log_2 n$
- **Total Work:** $\sum_{i=0}^{\log_2 n} 1 = \log_2 n + 1 = \Theta(\log n)$

#### 3. Master Theorem Application
- $n^{\log_b a} = n^{\log_2 1} = n^0 = 1$.
- Compare $f(n) = 1$ with $n^{\log_b a} = 1$: $f(n) = \Theta(n^{\log_b a})$.
- **Applicable Case:** Case 2 ($k = 0$).
- **Result:** $T(n) = \Theta(n^{\log_b a} \log n) = \Theta(\log n)$.
- **Comparison:** Recursion tree analysis and Master Theorem match: $\Theta(\log n)$.

---

### Function 2: $T(n) = T(n/2) + n$

#### 1. Derivation from Code
```java
void fun(int n) {
    if (n > 1) {
        for (int i = 0; i < n; i++) { } // O(n) loop
        System.out.println(n);
        fun(n / 2);                     // 1 call with size n/2
    }
}
```
- **Identification:** $a = 1$, $b = 2$, $f(n) = n$.

#### 2. Recursion Tree Analysis
- **Number of calls at level $i$:** $1$
- **Input size at level $i$:** $n / 2^i$
- **Work performed at level $i$:** $n / 2^i$
- **Height of Tree:** $\log_2 n$
- **Total Work:** $\sum_{i=0}^{\log_2 n} \frac{n}{2^i} = n \left(1 + \frac{1}{2} + \frac{1}{4} + \dots\right) = 2n = \Theta(n)$

#### 3. Master Theorem Application
- $n^{\log_b a} = n^0 = 1$.
- Compare $f(n) = n$ with $n^{\log_b a} = 1$: $f(n) = \Omega(n^{0 + 1})$ ($\epsilon = 1$).
- **Regularity Check:** $a f(n/b) \le c f(n) \implies 1 \cdot (n/2) \le c \cdot n \implies c = 1/2 < 1$.
- **Applicable Case:** Case 3.
- **Result:** $T(n) = \Theta(f(n)) = \Theta(n)$.
- **Comparison:** Both recursion tree and Master Theorem give $\Theta(n)$.

---

### Function 3: $T(n) = 2T(n/2) + n$

#### 1. Derivation from Code
```java
void fun(int n) {
    if (n > 1) {
        for (int i = 0; i < n; i++) { } // O(n) loop
        System.out.println(n);
        fun(n / 2);                     // Call 1
        fun(n / 2);                     // Call 2
    }
}
```
- **Identification:** $a = 2$, $b = 2$, $f(n) = n$.

#### 2. Recursion Tree Analysis
- **Number of calls at level $i$:** $2^i$
- **Input size at level $i$:** $n / 2^i$
- **Work performed at level $i$:** $2^i \times (n / 2^i) = n$
- **Height of Tree:** $\log_2 n$
- **Total Work:** $\sum_{i=0}^{\log_2 n} n = n (\log_2 n + 1) = \Theta(n \log n)$

#### 3. Master Theorem Application
- $n^{\log_b a} = n^{\log_2 2} = n^1 = n$.
- Compare $f(n) = n$ with $n^{\log_b a} = n$: $f(n) = \Theta(n^{\log_b a})$.
- **Applicable Case:** Case 2 ($k = 0$).
- **Result:** $T(n) = \Theta(n^{\log_b a} \log n) = \Theta(n \log n)$.
- **Comparison:** Both recursion tree and Master Theorem give $\Theta(n \log n)$.

---

### Summary Table of Task 2

| Function | Recurrence | $a$ | $b$ | $f(n)$ | $n^{\log_b a}$ | Master Theorem Case | Asymptotic Time Complexity |
|---|---|---|---|---|---|---|---|
| **Fun 1** | $T(n) = T(n/2) + 1$ | 1 | 2 | $1$ | $1$ | Case 2 | $\Theta(\log n)$ |
| **Fun 2** | $T(n) = T(n/2) + n$ | 1 | 2 | $n$ | $1$ | Case 3 | $\Theta(n)$ |
| **Fun 3** | $T(n) = 2T(n/2) + n$ | 2 | 2 | $n$ | $n$ | Case 2 | $\Theta(n \log n)$ |

---

## References & Resources Used
1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press. Chapter 4: Divide-and-Conquer.
2. GeeksforGeeks. *Master Theorem for Subtract and Conquer Recurrences*.
3. GeeksforGeeks. *Master Theorem for Divide and Conquer Recurrences*.
4. Khan Academy. *Algorithms: Analysis of Recursive Algorithms*.
