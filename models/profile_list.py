# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Profilelist(models.Model):

    _name = 'profile.list'

    dcp = fields.Char('Description')
    namee = fields.Char('Nom de profile')
    
    

class ResUser(models.Model):

    _inherit = "res.users"

    profile = fields.Many2many('res.profile', 'Profile', string='Profile')



class SaleOrderLine(models.Model):

    _inherit = "sale.order"

    profile_in = fields.Many2many('res.profile', 'profile', string='Profile')



