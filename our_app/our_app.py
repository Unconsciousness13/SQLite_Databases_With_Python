import database

# # add a record to the database
# database.add_one("Pako", "Iliev" , "pako@pako.es")



# # delete record row id as string
# database.delete_one('5')


# add many records
# stuff = [
#         ('Ceko', 'Sofinq', 'ceko@sifonq.bg'),
#          ('Tigar', 'Pobesnel', 'tigar@besen.bg')
#          ]
         
# database.add_many(stuff)
database.email_lookup("pako@pako.es")

# # show all the records
# database.show_all()


