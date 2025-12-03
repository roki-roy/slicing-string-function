#..slicing configer:-

country = "Banagladesh" # Banagladesh = string

print(country[0]) # B
print(country[0:7]) # Bangla
print(country[-5:-1]) #ades

"String Function:"

str = "diplomainn"

print(str.endswith("nn")) #True
print(str.endswith("rm")) #False
print(str.capitalize()) # Diploma
print(str.upper()) # DIPLOMA
print(str.replace("diploma","bangladesh")) #("old","new") = bangladesh
print(str.find("l")) # 3
print(str.split()) # ['diplomainn']
print(str.count("n")) # 2