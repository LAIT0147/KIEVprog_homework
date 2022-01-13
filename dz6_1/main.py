import module_students
import module_group


kovalskii = module_students.Student('Man', "Ukr", "Bogdan", "Kovalskii", '2000/12/12', 2)
didovec = module_students.Student('Man', "Ukr", "Vlad", "Didovec", '2002/4/19', 2)
tokar = module_students.Student('Man', "Ukr", "Nikita", "Tokar", '2002/9/13', 2)
andrienko = module_students.Student('Man', "Ukr", "Ilia", "Andrienko", '2001/1/25', 2)
kaznadey = module_students.Student('Man', "Ukr", "Egor", "Kaznadey", '2001/4/16', 2)
kud = module_students.Student('Man', "Ukr", "Vlad", "Kud", '2002/1/19', 2)


KI_21 = module_group.Group([kovalskii, didovec, tokar, andrienko, kaznadey])
print("Group KI\n")
for items in KI_21:
    print(items)
print()

KI_21.add(kud)
print("Added new student (kud)\n")
for items in KI_21:
    print(items)

print("Searching for a student\n", KI_21.search("Kud"))

KI_21.remove("Kaznadey")
print("Removing Kaznadey from KI_21")
for items in KI_21:
    print(items)
