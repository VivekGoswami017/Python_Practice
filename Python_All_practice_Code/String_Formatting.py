# 1.Comma (,) in print()
name = "Python"
age = 21
print("Name:", name)
print("Age:", age)
print("Name:", name, "Age:", age)


# 2. String Concatenation (+)
name = "World !!"
print("Hello " + name)


# 3. % Formatting
name = "Rakesh"
age = 22
price = 799.5

print("Name: %s" % name)
print("Age: %d" % age)
print("Price: %.2f" % price)
print("Name: %s Age: %d" % (name, age))


# 4. .format() Method
name = "Vivek"
age = 22

print("Name: {}".format(name))
print("Name: {} Age: {}".format(name, age))

price = 799.5
print("Price: {:.2f}".format(price))

# 5. f-String
name = "Modi"
age = 85
print(f"Name: {name}")
print(f"Age: {age}")

no=100
no1=50
no2=50
print(f"addition of {no} and {no1} and {no2} is there {no+no1+no2}")