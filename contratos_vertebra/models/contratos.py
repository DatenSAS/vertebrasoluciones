# -*- coding: utf-8 -*-
from openerp import fields, models, api

class Contratos_Principal(models.Model):
    _name = 'contratos.principal'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description ='Contratos Principales'

    name = fields.Char()
    objeto = fields.Text(string = 'Objeto')
    fecha_inicio =fields.Date(string = 'Fecha de Inicio')
    fecha_final = fields.Date(string='Fecha Final')
    etapas = fields.Many2one('etapas', string='Etapas', group_expand='_read_group_stage_ids', default = 1)

    @api.model
    def _read_group_stage_ids(self,stages,domain,order):
        stage_ids = self.env['etapas'].search([])
        return stage_ids


    kanban_state = fields.Selection(
        [('normal', 'En Progreso'), ('done', 'Hecho'),
         ('blocked','Bloqueada')]
    )
    cliente = fields.Many2one('res.partner', string='Cliente')
    responsable = fields.Many2one('res.users',string='Responsable')
    valor_inicial =fields.Monetary(string='Valor Inicial', currency_field='moneda')
    valor_total = fields.Monetary(string='Valor Total', currency_field='moneda')
    valor_facturado = fields.Monetary(string='Valor Facturado', currency_field='moneda')
    gastos = fields.Monetary(string='Gastos', currency_field='moneda')

    def _default_currency(self):
        return self.env['res.currency'].search([('name', '=', 'COP')], limit=1).id

    moneda = fields.Many2one('res.currency', string='Moneda', default=_default_currency)
    alcance = fields.Html(string='Alcance')
    pct_facturado = fields.Float(string='Pct Facturado')
    contrato = fields.Boolean(string='Contrato')
    polizas = fields.Boolean(string='Pólizas')
    oferta_tecnica = fields.Boolean(string='Oferta Técnica')
    anexos = fields.Boolean(string='Anexos al Contrato')
    matriz = fields.Boolean(string='Matriz Contractual')
    presupuesto = fields.Boolean(string='Presupuesto General Inicial')
    informe = fields.Boolean(string='Informe de Materializacaión')

    prioridad = fields.Boolean()
    color = fields.Integer(default = 1)


class Etapas (models.Model):
    _name = 'etapas'
    _description ='Etapas'

    name = fields.Char()
    secuencia =fields.Integer()



