# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning,ValidationError,UserError


class Profilelist(models.Model):

    _name = 'profile.list'

    dcp = fields.Char('Description')
    namee = fields.Char('Nom de profile')
    
    

class ResUser(models.Model):

    _inherit = "res.users"

    profile = fields.Many2one('res.profile', string='Profile')



class SaleOrderLine(models.Model):

    _inherit = "sale.order"

    profile_in = fields.Many2one('res.profile', string='Profile')
    type_ven =  fields.Selection([ ('type1', 'Projet'),('type2', 'Vente directe'),],'Type vente', default='type2')
    compta_analy = fields.Char('Compte analytique')



#class my_project(models.Model):
       
    #_inherits = {'project.project':'project_id'}
   
    #project_id = fields.Many2one('project.project', 'Project', ondelete="cascade", required=True)



