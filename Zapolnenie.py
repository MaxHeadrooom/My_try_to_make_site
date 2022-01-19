import create_db as new_db
import datetime

acc1 = new_db.Accounts(Login="Login1", Password="Password1", reg_date=datetime.datetime.now(), city="Moscow", street="Chertanovo", house="1")
acc2 = new_db.Accounts(Login="Login2", Password="Password2", reg_date=datetime.datetime.now(), city="Moscow", street="Tverskya", house="5")
acc3 = new_db.Accounts(Login="Login3", Password="Password3", reg_date=datetime.datetime.now(), city="Moscow", street="Chertanovo", house="17")

new_db.database.session.add(acc1)
new_db.database.session.add(acc2)
new_db.database.session.add(acc3)
new_db.database.session.commit()

print(new_db.Accounts.query.all())