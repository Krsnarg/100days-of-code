letter = "Hey my name is{} and I am from {}"
country = "India"
name = "Harry"

print(letter.format(name, country))

letter = "Hey my name is{1} and I am from {0}"
country = "India"
name = "Harry"
print(f"Hey my name is {name} and I am from {country}")

txt = "For only {Price: .2f}dollars!"
print(txt.format(price = 49.09999999))

price = 49.099999
txt = f"For only {Price:.2f}dollars!"
#print(txt.format())
print(txt)

print(f"{2 * 30}")

print(letter.format(name, country))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
