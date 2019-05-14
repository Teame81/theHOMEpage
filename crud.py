from dbModels import db, Puppy,Owner,Toy

#Create

rufus = Puppy('Rufus',3, 'doogie')
fido = Puppy('Fido', 1, 'hamster')

db.session.add_all([rufus,fido])
db.session.commit()

print(Puppy.query.all())


rufus = Puppy.query.filter_by(name='Rufus').first()
print (rufus)
timmie = Owner('Timmie', rufus.id)

toy1 = Toy('Chew toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([timmie,toy1, toy2])
db.session.commit()

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
print(rufus.report_toys())
