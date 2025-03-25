# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Question 2: Extended Euclidean Algorithm
print("Question 2: Extended Euclidean Algorithm")
test_cases = [(428, 23), (125, 23), (125634, 2356)]
for a, b in test_cases:
    d, s, t = extended_gcd(a, b)
    print(f"as + bt = d => {a}({s}) + {b}({t}) = {d}")
print()