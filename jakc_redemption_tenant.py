from openerp.osv import fields, osv

class rdm_tenant(osv.osv):
    _name = "rdm.tenant"
    _description = "Redemption Tenant"
    _columns = {
        'name': fields.char('Name', size=200, required=True),
        'company': fields.char('Company', size=200),
        'category': fields.many2one('rdm.tenant.category','Category', required=True),
        'grade': fields.many2one('rdm.tenant.grade','Grade', required=True),
        'participant': fields.selection([('1','AYC non participant tenant'),('2','AYC participant tenant')],'Participant Type',required=True),            
        'location': fields.char('Location', size=10),
        'floor': fields.char('Floor', size=10),
        'number': fields.char('Number', size=10),
        'start_date': fields.date('Join Date', required=True),
        'end_date': fields.date('End Date'),   
        'customer_ids': fields.one2many('rdm.customer','tenant_id','Contacts'),
        'message_ids': fields.one2many('rdm.tenant.message','tenant_id','Messages'),        
        'deleted': fields.boolean('Deleted'),
    }
    _default = {
        'participant': lambda *a:'1',
        'deleted': lambda *a: False,  
              
    }
rdm_tenant()

class rdm_tenant_message(osv.osv):
    _name = 'rdm.tenant.message'
    _description = 'Redemption Tenant Message'
    _columns = {
        'tenant_id': fields.many2one('rdm.tenant','Tenant'),
        'customer_id': fields.many2one('rdm.customer','Contact'),
        'subject': fields.char('Subject',size=50,required=True),                
        'message': fields.text('Message',required=True),
        'state': fields.selection([('open','Open'),('done','Close')],'State'),
    }
    _defaults = {
        'state': lambda *a :'open',
    }
    
rdm_tenant_message()