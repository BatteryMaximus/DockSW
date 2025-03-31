from db_functions import setupPG


db, cursor = setupPG()
SQL = "INSERT INTO packs DEFAULT VALUES returning id;"

cursor.execute(SQL, )

new_id = cursor.fetchone()[0]
db.commit()

print("Inserted row ID: ", new_id)

cursor.close()
db.close()
