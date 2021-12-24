# -*- coding: utf-8 -*-
from openerp import fields, models, api

class Facturacion(models.Model):
    _name = 'facturacion'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description ='Facturación Contratos'

    name = fields.Char(string="Nombre")
    contrato = fields.Many2one('contratos.principal', string='Contrato')
    fecha_emision = fields.Date(string='Fecha de Emision')
    fecha_vencimiento = fields.Date(string='Fecha de Vencimiento')
    concepto = fields.Text(string='Concepto')
    etapas = fields.Many2one('etapas.facturacion', string='Etapas', group_expand='_read_group_stage_ids', default=1)

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        stage_ids = self.env['etapas.facturacion'].search([])
        return stage_ids

    kanban_state = fields.Selection(
        [('normal', 'En Progreso'), ('done', 'Hecho'),
         ('blocked', 'Bloqueada')]
    )
    responsable = fields.Many2one('res.users', string='Responsable')
    valor = fields.Monetary(string='Valor', currency_field='moneda')

    def _default_currency(self):
        return self.env['res.currency'].search([('name', '=', 'COP')], limit=1).id

    moneda = fields.Many2one('res.currency', string='Moneda', default=_default_currency)

    prioridad = fields.Boolean()
    color = fields.Integer(default=1)


class Etapas_Facturacion(models.Model):
    _name = 'etapas.facturacion'
    _description = 'Etapas para Facturación'

    name = fields.Char()
    secuencia = fields.Integer()
