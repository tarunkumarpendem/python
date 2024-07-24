############
# Model -1 #
############

x = "Tarun"
y = 26
z = 52.736

print(x); print(y); print(z)


############
# Model -2 #
############

x = str("Tarun")
y = int(26)
z = float(52.736)

print(x)
print(y)
print(z)


############
# Model -3 #
############

x = str("Tarun")
y = int(26)
z = float(52.736)

print(f"The person's Name is {x}")
print(f"The person's Age is {y}")
print(f"The person's Weight is {z}")

print(type(x))
print(type(y))
print(type(z))


############
# Model -4 #
############

x = y = z = "Pink"

print(x)
print(x)
print(y)
print(type(x))


############
# Model -5 #
############

x,y,z = "Pink" , "Black" , "Brown"

print(x)
print(y)
print(z)
print(type(x))


############
# Model -5 #
############

cars = [ "VOLVO", "JAGWAR", "Rolls Royce" ]

x,y,z = cars

print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))


############
# Model -6 #
############

x = "I'm Tarun and I'm a DevOps Engineer"

print(x)
print(type(x))


############
# Model -7 #
############

j = "I'm Tarun"
q = "and"
k = "I'm a"
a = "DevOps Engineer"

print(j,q,k,a)

print(type(j))
print(type(q))
print(type(k))
print(type(a))


############
# Model -7 #
############

j = "I'm Tarun "
q = "and "
k = "I'm a "
a = "DevOps Engineer "
b = "I'm Learning Python"

print(j + q + k+ a+ b)


############
# Model -8 #
############

j = "I'm Tarun "
q = 5

# ❌
# print(j+q)

# ✅
print(j,q)