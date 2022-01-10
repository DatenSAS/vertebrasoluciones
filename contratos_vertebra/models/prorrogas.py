from openerp import fields, models, api

class Prorrogas(models.Model):
    _name = 'prorrogas'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description ='Prorrogas'

    name = fields.Char(string="Nombre")
    contrato = fields.Many2one('contratos.principal',string='Contrato', ondelete='restrict')
    fecha_inicio = fields.Date(string='Fecha Inicio')
    fecha_fin = fields.Date(string='Fecha Final')
    responsable = fields.Many2one('res.users', string='Responsable', ondelete='restrict')
    valor = fields.Monetary(string='Valor', currency_field='moneda')

    def _default_currency(self):
        return self.env['res.currency'].search([('name', '=', 'COP')], limit=1).id

    moneda = fields.Many2one('res.currency', string='Moneda', default=_default_currency)
    secuencia = fields.Integer()