# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Profilelist(models.Model):

    _name = 'profile.list'
    
    name = fields.Char('Nom de profile')
    descp = fields.Char('Description')
    

class ResUsers(models.Model):

    _inherit = "res.users"

    profile_inht = fields.One2many('res.users', 'profile', string='Profile')


class SaleOrderLine(models.Model):

    _inherit = 'sale.order'

    profile_in = fields.One2many('res.users', 'profile', string='Profile')
    

