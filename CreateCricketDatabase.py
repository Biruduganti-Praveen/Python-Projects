import sqlite3
cricket=sqlite3.connect('fantasycricket.db')
objcricket=cricket.cursor()

# Creating a Table for Match
# objcricket.execute('''CREATE TABLE Match1(
#     Player string(20) Primary Key,
#     Scored integer NOT NULL,
#     Faced integer NOT NULL,
#     Fours integer,
#     Sixes integer,
#     Bowled integer,
#     Maiden intger,
#     Given integer,
#     Wkts integer,
#     Catches integer,
#     Stumling integer,
#     RO integer
# )''')

# Creating a Table for Teams
# objcricket.execute('''CREATE TABLE Teams(
#     Players string(20) References Match(PLayer),
#     Name varchar2 NOT NULL,
#     value integer
# )''')
# cricket.commit()
# Creating a Table for Stats
    # objcricket.execute('''CREATE TABLE Stats(
    #     Players string(20) References Match(PLayer),
    #     Matches integer,
    #     Runs integer,
    #     "100s" integer,
    #     "50s" integer,
    #     value integer,
    #     ctg text
    # )''')

objcricket.execute('Select Players,Name,value from Teams')
# print(objcricket.fetchall())
for i in objcricket.fetchall():
    # if i[0] == "Kohli":
        print(i[2])
# cricket.commit()
cricket.close()