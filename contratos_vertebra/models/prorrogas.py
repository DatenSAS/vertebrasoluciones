from openerp import fields, models, api

class Prorrogas(models.Model):
    _name = 'prorrogas'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description ='Prorrogas'

    name = fields.Char(string="Nombre")
    contrato = fields.Many2one('contratos.principal',string='Contrato')