# -*- coding: utf-8 -*-
from openerp import fields, models, api

class contacto(models.Model):
    _inherit = 'res.partner'

    se_id = fields.Char(string='Id Smart Eco')
    servicio = fields.Char(string='Servicio')