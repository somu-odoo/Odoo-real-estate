import xmlrpc.client; 

db = "odoo15"
user = "admin"
passw = "admin"

common = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/common')
uid = common.authenticate(db, user, passw, {})
if uid: print("[+] Connection Successfull !!!")

models = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/object')

ids = models.execute_kw(db, uid, passw, 'estate.estate', 'search_read', [[(1, '=', 1)]])
print(ids)