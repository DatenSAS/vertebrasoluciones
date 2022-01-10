# -*- coding: utf-8 -*-
from openerp import fields, models, api

class grupo(models.Model):
    _name = 'grupo'
    _description ='Zonificación de Departamentos'

    name = fields.Char(string='Grupo')
    cliente = cliente = fields.Many2one('res.partner', string='Cliente')
    se_id = fields.Char(string='Id Smart Eco')

class punto(models.Model):
    _name = 'punto'
    _description ='Punto - Sucursal'

    name = fields.Char(string='Punto')
    se_id = fields.Char(string='Id Smart Eco')
    cliente = fields.Many2one('res.partner', string='Cliente', ondelete='restrict')
    grupo = fields.Many2one('grupo', string='Grupo', ondelete='restrict')
    departamento = fields.Char(string='Departamento')
    ciudad = fields.Char(string='Ciudad')
    direccion = fields.Char(string='Dirección')
    centro_costo = fields.Char(string='Centro de Costo')
    tipo_punto = fields.Char(string='Tipo de Punto')
    estado = fields.Boolean(string='Estado del Punto')
    tipo_propiedad = fields.Char(string="Tipo de Propiedad")

class cuenta(models.Model):
    _name = 'cuenta'
    _description ='Cuenta'

    name = fields.Char(string='Número')
    se_id = fields.Char(string='Id Smart Eco')
    cliente = fields.Many2one('res.partner', string='Cliente', ondelete='restrict')
    punto = fields.Many2one('punto', string='Punto', ondelete='restrict')
    servicio = fields.Char(string='Servicio')
    prestador_servicio = fields.Char(string='Prestador del Servicio')