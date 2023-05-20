# PYTHON Variables
# ------------------
# Variables are containers for storing data values.

# For Testing variables

# number --> int
# decimal number --> float
# word --> string
# multiple words --> list (or) array
# true/false --> boolean


# We can declare varibles directly with data types
##################################################

# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0 

###################################################

# Variable declaration methods
# ------------------------------

# camel case variable declaration
# myVariableNameOfThisTimeIs = 5

# Pascal case variable declaration
# MyVariableNameOfThisTimeIs = 5

# Snake case variable declaration
# my_variable_name_of_this_time_is = 5

#####################################################

x = 5
y = 10.001250
z = "Tarun"
a = True

# 'x' value and data type
print(type(x))
print(x)

# 'y' value and data type
print(type(y))
print(y)

# 'z' value and data type
print(type(z))
print(z)

# 'a' value and data type
print(type(a))
print(a)

#####################################################
# Assigning multiple variables
# ----------------------------

Name, Number, Boolean, Decimal_Number = "Tarun", 7, False, 12.356
print(type(Name))
print(Name)

print(type(Number))
print(Number)

print(type(Boolean))
print(Boolean)

print(type(Decimal_Number))
print(Decimal_Number)


############################################
# One value to multiple variables
# -------------------------------

a = b = c = d = "Alphabates"
print(a)
print(b)
print(c)
print(d)


##################################################
# Unpacking (Extracting the values to variables )
# -----------------------------------------------

colours = [ "Black", "White", "Gray", "Yellow", "Blue", "Green" ]

p = q = r = s = colours

print(colours)
print(p)
print(q)
print(r)
print(s)


##################################
# Output variables
##################################




def print_Values(tableno, orderno, items, persons):
    body = {}
    if tableno == "1" :
        tablename = "guest"
    else:
        tablename = "customers"
     
    a = f"tablename is {tablename}"
    b = f"orderno is {orderno}"
    c = f"items is {items}"
    d = f"No of persons is {persons}"

    body = {
        "tablename" : a,
        "orderno" : b,
        "items": c,
        "persons" : d
    }
    return body
callfunction = print_Values("2", "5", "6", "7")
print(callfunction)
callfunction2 = print_Values("1", "5", "5", "5")
print(callfunction2)
