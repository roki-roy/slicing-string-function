#...if-else(syntex)

"Student marke and grade calculation:-"

marke = int(input("enter the marke:"))
if(marke >= 100):
    grade = "A+"
elif(marke >= 70 and marke <= 100):
    grade = "A"
elif(marke >= 50 and marke <= 70):
    grade = "B"
elif(marke >= 30 and marke <= 50):
    grade = "C"
else:
    grade = "F"

print(grade)


"Trafig light control:-"

light = input("Enput the coller:")
if(light == "red"):
    condition = "stop"
elif(light == "yellow"):
    condition = "See light"
elif(light == "green"):
    condition = "go now"
else:
    condition = "the systime is broken"

print(condition)