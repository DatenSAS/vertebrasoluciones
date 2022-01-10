# -*- coding: utf-8 -*-
from openerp import fields, models, api
from odoo import exceptions

class Contratos_Principal(models.Model):
    _name = 'contratos.principal'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description ='Contratos Principales'

    name = fields.Char(string="Nombre")
    objeto = fields.Text(string = 'Objeto')
    fecha_inicio =fields.Date(string = 'Fecha de Inicio')
    fecha_final = fields.Date(string='Fecha Final')
    etapas = fields.Many2one('etapas', string='Etapas', group_expand='_read_group_stage_ids', default = 1, ondelete='restrict')
    active = fields.Boolean(string="Active", default=True)

    @api.model
    def _read_group_stage_ids(self,stages,domain,order):
        stage_ids = self.env['etapas'].search([])
        return stage_ids


    kanban_state = fields.Selection(
        [('normal', 'En Progreso'), ('done', 'Hecho'),
         ('blocked','Bloqueada')]
    )
    cliente = fields.Many2one('res.partner', string='Cliente', ondelete='restrict')
    responsable = fields.Many2one('res.users',string='Responsable', ondelete='restrict')
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
    informe = fields.Boolean(string='Informe de Materialización')

    prioridad = fields.Boolean()
    color = fields.Integer(default = 1)

    def actualizar_datos(self):
        contratos = self.env['contratos.principal'].search([])
        for contrato in contratos:
             prorrogas = self.env['prorrogas'].search([('contrato', '=', contrato.id)])
             valor_pro = 0
             for prorroga in prorrogas:
                 valor_pro = valor_pro + prorroga['valor']
             contrato['valor_total'] = valor_pro + contrato['valor_inicial']

             facturas = self.env['facturacion'].search([('contrato', '=', contrato.id)])
             valor_fac = 0
             for factura in facturas:
                 if factura.etapas.id == 2 or factura.etapas.id == 3:
                     valor_fac = valor_fac + factura['valor']
             contrato['valor_facturado'] = valor_fac
             if contrato['valor_inicial']:
                 contrato['pct_facturado'] = valor_fac / contrato['valor_inicial']

             gastos = self.env['gastos'].search([('contrato', '=', contrato.id)])
             valor_gas = 0
             for gasto in gastos:
                 valor_gas = valor_gas + gasto['valor']
             contrato['gastos'] = valor_gas

    @api.onchange('etapas')
    def a_suspendido(self):
        if self._origin.etapas.id == 3 and self.etapas.id==3:
            raise exceptions.UserError('No se permite este cambio de etapa')

    @api.onchange('etapas')
    def check(self):
        if self._origin.etapas.id == 1:
            if not self.contrato:
                raise exceptions.UserError('Falta Verificar Contrato')
            if not self.polizas:
                raise exceptions.UserError('Falta Verificar Pólizas')
            if not self.oferta_tecnica:
                raise exceptions.UserError('Falta Verificar Oferta Técnica')
            if not self.matriz:
                raise exceptions.UserError('Falta Verificar Matriz')
            if not self.presupuesto:
                raise exceptions.UserError('Falta Verificar Presupuesto')
            if not self.informe:
                raise exceptions.UserError('Falta Verificar Informe')

class Etapas (models.Model):
    _name = 'etapas'
    _description ='Etapas'

    name = fields.Char()
    secuencia =fields.Integer()



