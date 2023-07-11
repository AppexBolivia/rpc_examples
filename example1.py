# odoo rpc example

import xmlrpc.client

# Login to Odoo server
url = 'http://localhost:8069'
db = 'v15'
username = 'admin'
password = 'admin'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
print("Logged in as %s (uid: %d)" % (username, uid))

# Read the sessions
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# get account.move that are not invoices
domain = [('move_type', '=', 'entry')]
fields = ['name', 'date', 'ref', 'journal_id', 'line_ids']
move_ids = models.execute_kw(db, uid, password, 'account.move', 'search_read', [domain], {'fields': fields})
for move in move_ids:
    print(move)


# employee_ids = models.execute_kw(db, uid, password, 'hr.employee', 'search_read', [[]], {'fields': ['id', 'name']})
# for employee_id in employee_ids:
#     #employee = models.execute_kw(db, uid, password, 'hr.employee', 'read', [employee_id], {'fields': ['id', 'name']})
#     print(employee_id)
