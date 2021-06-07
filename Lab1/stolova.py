from kanren import Relation, facts, run, var, eq


first = Relation()
second = Relation()
third = Relation()

facts(first, ("Soup", "Borshtch"))
facts(second, ("Beef", "Chicken", "Fish"))
facts(third, ("Kompot", "Tea" ))
 
meal = Relation()

facts(meal, ("Soup", "Fish", "Kompot"),
            ("Borshtch", "Fish", "Kompot"),
            ("Soup", "Chicken", "Kompot"),
            ("Borshtch", "Chicken", "Kompot"),
            ("Soup", "Beef", "Kompot"),
            ("Borshtch", "Beef", "Kompot"),
            ("Soup", "Fish", "Tea"),
            ("Borshtch", "Fish", "Tea"),
            ("Soup", "Chicken", "Tea"),
            ("Borshtch", "Chicken", "Tea"),
            ("Soup", "Beef", "Tea"),
            ("Borshtch", "Beef", "Tea"))

count = 0
x, y, z = var(), var(), var()

names = []
for a in run(0, [x, y, z], meal(x, y, z)):
    if a[1] == "Beef" and a[2] == "Tea":
        print(a)
        count += 1
print("Count: ", count)