from openerp.osv import fields, osv

class rdm_tenant(osv.osv):
    _name = "rdm.tenant"
    _description = "Redemption Tenant"
    _columns = {
        'type': fields.many2one('rdm.tenant.type','Type', required=True),
        'grade': fields.many2one('rdm.tenant.grade','Grade', required=True),
        'participant': fields.selection([('1','AYC non participant tenant'),('2','AYC participant tenant')],'Participant Type'),
        'name': fields.char('Name', size=200, required=True),
        'company': fields.char('Company', size=200),
        'location': fields.char('Location', size=10),
        'floor': fields.char('Floor', size=10),
        'number': fields.char('Number', size=10),
        'start_date': fields.date('Join Date'),
        'end_date': fields.date('End Date'),   
        'tenant_pic_ids': fields.one2many('rdm.tenant.pic','tenant_id','Contacts')
    }
rdm_tenant()

class rdm_tenant_pic(osv.osv):
    _name = 'rdm.tenant.pic'
    _description = 'Redemption Tenant PIC'
    _columns = {
        'tenant_id': fields.integer('Tenant ID'),
        'name': fields.char('Name', size=200),        
        'title': fields.many2one('rdm.tenant.title','Title'),
        'birth_place': fields.char('Birth Place', size=100),
        'birth_date': fields.date('Birth Date'),
        'gender': fields.selection([('1','Man'),('2','Woman')],'Gender'),
        'address': fields.text('Address'),
        'province': fields.many2one('rdm.province','Province'),
        'city': fields.many2one('rdm.city','City'),
        'zipcode': fields.char('Zipcode', size=10),
        'phone1': fields.char('Phone 1', size=20),
        'phone2': fields.char('Phone 2', size=20),
        'mobile_phone1': fields.char('Mobile Phone 1', size=20),
        'mobile_phone2': fields.char('Mobile Phone 2', size=20),
        'email': fields.char('Email',size=100),        
        'join_date': fields.date('Join Date'),
        'end_date': fields.date('End Date'),        
    }        
    
rdm_tenant_pic()