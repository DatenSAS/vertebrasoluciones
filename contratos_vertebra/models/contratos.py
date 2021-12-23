# -*- coding: utf-8 -*-
from openerp import fields, models, api

class Contratos_Principal(models.Model):
    _name = 'contratos.principal'
    _description ='Contratos Principales'

    name = fields.Char()
    objeto = fields.Text(string = 'Objeto')
    fecha_inicio =fields.Date(string = 'Fecha de Inicio')
    fecha_final = fields.Date(string='Fecha Final')
    etapas = fields.Many2one('etapas', string="Etapas")

class Etapas (models.Model):
    _name = 'etapas'
    _description ='Etapas'

    name = fields.Char()
    secuencia =fields.Integer()



