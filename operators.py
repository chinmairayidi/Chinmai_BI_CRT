a = 10
b = 5
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("📌 Arithmetic Operators:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)

print("\n📌 Assignment Operators:")
a += 1
print("a += 1 =>", a)
a -= 2
print("a -= 2 =>", a)
a *= 3
print("a *= 3 =>", a)
a /= 2
print("a /= 2 =>", a)
a %= 3
print("a %= 3 =>", a)
a //= 1
print("a //= 1 =>", a)
a **= 2
print("a **= 2 =>", a)

print("\n📌 Comparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\n📌 Logical Operators:")
print("a > 5 and b > 1:", a > 5 and b > 1)
print("a > 5 or b < 1:", a > 5 or b < 1)
print("not(a > 5):", not(a > 5))

print("\n📌 Bitwise Operators:")
print("a & b:", int(a) & b)
print("a | b:", int(a) | b)
print("a ^ b:", int(a) ^ b)
print("~a:", ~int(a))
print("a << 1:", int(a) << 1)
print("a >> 1:", int(a) >> 1)

print("\n📌 Identity Operators:")
print("x is y:", x is y)
print("x is z:", x is z)
print("x is not y:", x is not y)

print("\n📌 Membership Operators:")
print("2 in x:", 2 in x)
print("4 not in x:", 4 not in x)
