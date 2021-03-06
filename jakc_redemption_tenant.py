from openerp.osv import fields, osv
import logging

_logger = logging.getLogger(__name__)

AVAILABLE_STATES = [
    ('draft','New'),    
    ('active','Active'),
    ('disable', 'Disable'),
    ('terminate', 'Terminate'),
]

AVAILABLE_PARTICIPANT = [
    ('1','AYC non participant tenant'),
    ('2','AYC participant tenant')
]

class rdm_tenant(osv.osv):
    _name = "rdm.tenant"
    _description = "Redemption Tenant"

    def trans_reset(self, cr, uid, ids, context=None):
        _logger.info("Reset for ID : " + str(ids))
        self.write(cr,uid,ids,{'state':'active'},context=context)
        return True
    
    def trans_disable(self, cr, uid, ids, context=None):
        _logger.info("Disable for ID : " + str(ids))
        self.write(cr,uid,ids,{'state':'disable'},context=context)
        return True

    def trans_enable(self, cr, uid, ids, context=None):
        _logger.info("Enable for ID : " + str(ids))
        self.write(cr,uid,ids,{'state':'active'},context=context)
        return True
        
    def trans_terminate(self, cr, uid, ids, context=None):
        _logger.info("Terminate for ID : " + str(ids))
        self.write(cr,uid,ids,{'state':'terminate'},context=context)
        return True
    
    def _get_trans(self, cr, uid, trans_id , context=None):
        return self.browse(cr, uid, trans_id, context=context);
            
    _columns = {
        'name': fields.char('Name', size=200, required=True),
        'company': fields.char('Company', size=200),
        'category': fields.many2one('rdm.tenant.category','Category', required=True),
        'grade': fields.many2one('rdm.tenant.grade','Grade', required=True),
        'participant': fields.selection(AVAILABLE_PARTICIPANT,'Participant Type',required=True),            
        'location': fields.char('Location', size=10),
        'floor': fields.char('Floor', size=10),
        'number': fields.char('Number', size=10),
        'start_date': fields.date('Join Date', required=True),
        'end_date': fields.date('End Date'),   
        'customer_ids': fields.one2many('rdm.customer','tenant_id','Contacts'),
        'message_ids': fields.one2many('rdm.tenant.message','tenant_id','Messages'),        
        'state': fields.selection(AVAILABLE_STATES,'Status',size=16,readonly=True),
    }
    _default = {
        'participant': lambda *a:'1',
        'state': lambda *a: 'draft',            
    }
    
    def create(self, cr ,uid, values, context=None):
        values.update({'state':'active'})
        trans_id = super(rdm_tenant,self).create(cr, uid, values, context=context)
        return trans_id
    
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