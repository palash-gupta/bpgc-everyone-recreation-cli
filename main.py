import sqlite3

db = sqlite3.connect("students.db")

cursor = db.cursor()

print("Enter name, ID, hostel, room queries (leave blank if you want to see all)")

ordermap = {"n": '"Name"', "i": '"Student ID"', "r": '"Room No."', "h": '"Hostel / Room or PS"'}

while True:
    name = "%".join(input("Enter name query: ").split(' '))
    idq = input("Enter ID query (branch/year): ")
    hostel = input("Enter Hostel/PS/Graduate query: ")
    room = input("Enter room number query: ")
    order = input("Order By (n for name, i for id, h for hostel, r for room, leave blank for default): ")

    query = f"""SELECT "Name", "Student ID", "Hostel / Room or PS", "Room No." FROM students"""
    #"Name" LIKE "%{name}%" AND "Student ID" LIKE "%{idq}%" AND "Hostel / Room or PS" LIKE "%{hostel}%" AND "Room No." LIKE "%{room}%";"""

    selectors = []

    if not name == "":
        selectors.append(f'''"Name" LIKE "%{name}%"''')
    if not idq == "":
        selectors.append(f'''"Student ID" LIKE "%{idq}%"''')
    if not hostel == "":
        selectors.append(f'''"Hostel / Room or PS" LIKE "%{hostel}%"''')
    if not room == "":
        selectors.append(f'''"Room No." LIKE "%{room}%"''')

    if len(selectors) != 0:
        query += " WHERE " + " AND ".join(selectors)

    if not order == "":
        query += f"ORDER BY {ordermap[order]}"

    query += ";"

    cursor.execute(query)
    out = cursor.fetchall()
    
    print(f"\n{len(out)} rows found.")
    print("\n" + "-" * 123)

    for i in out:
        for j in i:
            print(j, end=((30 - len(str(j)))*" " + "|" ))
        print("\n" + "-" * 123)


