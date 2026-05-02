print("LWE Summary")
print("-----------")

q = 17
secret = [1, -1, 0, 1]
error = [1, 0, -1, 0]

print("modulus q =", q)
print("secret =", secret)
print("error =", error)

print()
print("LWE uses a linear equation with a small amount of noise.")
print("The noise makes it harder to find the secret from the")
print("public information.")
print()
print("This is a small example used only to understand the idea.")
