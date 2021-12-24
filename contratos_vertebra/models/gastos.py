from openerp import fields, models, api

class Gastos(models.Model):
    _name = 'gastos'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description ='Gastos'

    name = fields.Char()
    contrato = fields.Many2one('contratos.principal',string='Contrato')
    fecha = fields.Date(string='Fecha de Gasto')
    tercero = fields.Many2one('res.partner',string='Tercero')
    motivo = fields.Selection(
        [('Transporte', 'Transporte'), ('Alimentación', 'Alimentación'),
         ('Hospedaje', 'Hospedaje'),('Compra de Insumos y Materiales', 'Compra de Insumos y Materiales'),
         ('Personal', 'Personal'),('Sanción','Sanciones')],
         'Motivo del Gasto')
    secuencia = fields.Integer()
    valor = fields.Monetary(string='Valor', currency_field='moneda')

    def _default_currency(self):
        return self.env['res.currency'].search([('name', '=', 'COP')], limit=1).id

    moneda = fields.Many2one('res.currency', string='Moneda', default=_default_currency)