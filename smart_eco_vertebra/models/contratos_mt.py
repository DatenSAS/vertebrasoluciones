# -*- coding: utf-8 -*-
from openerp import fields, models, api

class contratos(models.Model):
    _name = 'contratos'
    _description ='Contratos asociados al flujo de mercados y tarifas'

    name = fields.Char(string='Contrato')
    cliente = fields.Many2one('res.partner', string='Cliente')
    activo = fields.Boolean(string="¿Activo?")