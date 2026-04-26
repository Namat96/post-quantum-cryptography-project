print("Week 11 - Noise Effect Experiment")
print("----------------------------------")

q = 17
message = 1

for noise in range(0, 7):
    value = (message + noise) % q
    print("noise =", noise, "stored value =", value)

print()
print("In real lattice schemes, noise is carefully controlled.")
print("Too much noise can make correct recovery difficult.")
print("This is only a simple learning experiment.")
