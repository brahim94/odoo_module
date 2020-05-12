from odoo import api,fields,models
from odoo.exceptions import Warning,ValidationError,UserError


class extend_contact(models.Model):
    _inherit='res.partner'
    
    
    def print_page(self):
        return self.env.ref('odoo.action_report_page').report_action(self)
    