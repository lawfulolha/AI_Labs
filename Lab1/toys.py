from kanren import Relation, facts, run, var, eq

toy = Relation()

facts(toy,  ("Ball", 10, "from 2 to 90"),
            ("Watergun", 60, "from 5 to 12"),
            ("Spinner", 90, "from 4 to 8"),
            ("Tea Set", 120, "from 2 to 7"),
            ("Barbie Doll", 140, "from 4 to 12"),
            ("Tennis Set", 90, "from 6 to 15"),
            ("Skateboard", 110, "from 8 to 16"),
            ("Makeup Set", 210, "from 5 to 10"),
            ("SWAT Set", 150, "from 4 to 9"),
            ("M16 Assault Rifle", 410, "from 21 to 90")
)

x, y, z = var(), var(), var()

price = 0
count = 0
for a in run(0, [x, y, z], toy(x, y, z)):
    price += a[y]
    count += 1

print("Cost: ", price, "Average price: ", price/count)