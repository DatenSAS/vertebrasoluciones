from openerp import fields, models, api
from odoo import exceptions
from datetime import datetime

class ticket(models.Model):
    _inherit = 'helpdesk.ticket'

    contacto = fields.Many2one('res.partner', string='Contacto',tracking=True)
    origen = fields.Selection(
         [('Ecoeficiencia', 'Ecoeficiencia'), ('Pagos', 'Pagos'),
          ('Cliente', 'Cliente'),('M&T', 'M&T'),
          ],
         'Origen Solicitante',tracking=True
     )

    area = fields.Selection(
         [('Ecoeficiencia', 'Ecoeficiencia'), ('M&T', 'M&T'), ('Pagos', 'Pagos')],
         'Área de Encargo',tracking=True
     )

    tipo = fields.Selection(
         [('Información Propietario', 'Información Propietario'), ('Facturas o Soporte de Pago', 'Facturas o Soporte de Pago'),
          ('Registro Fotográfico', 'Registro Fotográfico')],
         'Tipo Documento',tracking=True
     )

    fecha_solicitud = fields.Date(string="Fecha de Solicitud Información Adicional",tracking=True)
    fecha_recepcion = fields.Date(string="Fecha de Recepción Información Adicional",tracking=True)
    fecha_escalamiento = fields.Date(string="Fecha de Escalamiento",tracking=True)
    fecha_escalamiento_nr = fields.Date(string="Fecha de Escalamiento sin Radicado",tracking=True)
    radicado = fields.Char(string="Radicado",tracking=True)
    fecha_recepcion_rad = fields.Date(string="Fecha de Recepción Radicado",tracking=True)
    fecha_recepcion_res = fields.Date(string="Fecha de Recepción Respuesta",tracking=True)
    dias = fields.Integer(string="Días respuesta del prestador",tracking=True)
    cierre = fields.Selection(
         [('No Concluido', 'No Concluido'), ('Exitoso', 'Exitoso'), ('No Exitoso','No Exitoso')],
         'Tipo de Cierre',tracking=True
     )

    justificacion = fields.Selection(
         [('No se recibió información completa', 'No se recibió información completa'),
          ('Respuesta no concluyente del prestador', 'Respuesta no concluyente del prestador'),
          ('Sin respuesta del prestador', 'Sin respuesta del prestador'),
          ('Falta de Información adicional en el tiempo previsto','Falta de Información adicional en el tiempo previsto')],
         'Justificación',tracking=True
     )
    ticket_cnt = fields.Many2one('helpdesk.ticket', string="Ticket de Continuación",tracking=True)

    cliente_id = fields.Integer(related='partner_id.id', string="Cliente ID")
    punto = fields.Many2one('punto', string='Punto',tracking=True)
    info_adicional = fields.Boolean(string="¿Requiere Información Adicional?",tracking=True)
    escalar_prestador = fields.Boolean(string="¿Requiere Escalar a Prestador?",tracking=True)
    sin_radicado = fields.Boolean(string="¿Sin Radicado?",tracking=True)
    recuperado=fields.Monetary(string="Monto Recuperado", currency_field='moneda')

    def _default_currency(self):
          return self.env['res.currency'].search([('name', '=', 'COP')], limit=1).id

    moneda=fields.Many2one('res.currency', string='Moneda', default=_default_currency)

    servicio = fields.Selection(
        [('Energía', 'Energía'), ('Acueducto y Alcantarillado', 'Acueducto y Alcantarillado'),
         ('Aseo','Aseo'),('Alumbrado Público','Alumbrado Público'),('Gas','Gas')],
        'Servicio',tracking=True
    )

    medio = fields.Selection(
        [('Llamada', 'Llamada'),
         ('Correo', 'Correo'),
         ('WhatsApp', 'WhatsApp')],
        'Medio de Escalamiento',tracking=True
    )

    grupo = fields.Char(related='punto.grupo.name')
    cuenta = fields.Many2one('cuenta', string="Cuenta")
    punto_id = fields.Integer(related='punto.id', string="Punto ID")
    prestador = fields.Char(related='cuenta.prestador_servicio')
    dias_totales = fields.Integer('Días hábiles transcurridos')
    rechazado = fields.Selection(
        [('Gestión Responsabilidad del Cliente', 'Gestión Responsabilidad del Cliente'),
         ('Fuera del Alcance Contratcual', 'Fuera del Alcance Contratcual')
         ],
        'Razón Rechazo',tracking=True
    )

    escalado_a = fields.Many2one('res.partner', string='Escalado a', tracking=True)
    proceso_help = fields.Many2one('proceso', string='Proceso', tracking=True)
    categoria_help = fields.Many2one('categoria', string='Categoria', tracking=True)
    subcategoria_help = fields.Many2one('subcategoria', string='Sub Categoria', tracking=True)

    proceso_id = fields.Integer(related='proceso_help.id', string="Proceso ID")
    categoria_id = fields.Integer(related='categoria_help.id', string="Categoria ID")

    solucion = fields.Html(string="Solución")


    @api.onchange('fecha_solicitud','fecha_recepcion')
    def calculo_de_dias(self):


        if self.fecha_solicitud and self.fecha_recepcion:

            sol = self.fecha_solicitud.strftime('%Y-%m-%d')
            rec = self.fecha_recepcion.strftime('%Y-%m-%d')
            leaves = self.env['resource.calendar.leaves'].search([])

            if rec < sol:
                raise exceptions.UserError('La fecha de recepción no puede estar antes que la fecha de solicitud')
            else:
                nh = 0
                for leave in leaves:
                    start_date = leave.date_from.strftime('%Y-%m-%d')
                    if start_date >= sol and start_date <=rec:
                        nh += 1

            d1 = datetime.strptime(sol, '%Y-%m-%d')
            d2 = datetime.strptime(rec, '%Y-%m-%d')
            daysDiff = (d2 - d1).days

            self.dias_totales = daysDiff - nh

    @api.onchange('fecha_escalamiento', 'fecha_recepcion_res')
    def calculo_de_dias_pres(self):

        if self.fecha_escalamiento and self.fecha_recepcion_res:
            sol = self.fecha_escalamiento.strftime('%Y-%m-%d')
            rec = self.fecha_recepcion_res.strftime('%Y-%m-%d')
            leaves = self.env['resource.calendar.leaves'].search([])

            if rec < sol:
                raise exceptions.UserError('La fecha de recepción no puede estar antes que la fecha de solicitud')
            else:
                nh = 0
                for leave in leaves:
                    start_date = leave.date_from.strftime('%Y-%m-%d')
                    if start_date >= sol and start_date <= rec:
                        nh += 1

            d1 = datetime.strptime(sol, '%Y-%m-%d')
            d2 = datetime.strptime(rec, '%Y-%m-%d')
            daysDiff = (d2 - d1).days

            self.dias = daysDiff - nh

    @api.onchange('stage_id')
    def desde_nuevo(self):
        if self._origin.stage_id.id == 1 and self.satge_id.id != 16:
             if not self.user_id:
                 raise exceptions.UserError('Falta asignar el Ticket')
             if not self.categoria_help:
                 raise exceptions.UserError('Falta asignar Categoria ')
             if not self.subcategoria_help:
                 raise exceptions.UserError('Falta asignar Subcategoria')
             if not self.partner_id:
                 raise exceptions.UserError('Falta asignar Cliente')
             if not self.punto:
                 raise exceptions.UserError('Falta asignar Punto')
             if not self.medio:
                 raise exceptions.UserError('Falta asignar Medio de Escalamiento')
             if not self.description:
                 raise exceptions.UserError('Falta agregar la descipción del ticket')
             if not self.proceso_help:
                 raise exceptions.UserError('Falta diligenciar el proceso')

    class procesos (models.Model):
        _name = 'proceso'
        _description = 'Proceso asociado a Reclamaciones'

        name = fields.Char(string='Proceso')

    class categoria(models.Model):
        _name = 'categoria'
        _description = 'Categoria asociada a Reclamaciones'

        name = fields.Char(string='Categoria')
        proceso_id = fields.Many2one('proceso', string='Proceso',tracking=True)

    class subcategoria(models.Model):
        _name = 'subcategoria'
        _description = 'Subcategoria asociada a Reclamaciones'

        name = fields.Char(string='Subcategoria')
        categoria = fields.Many2one('categoria', string='Categoria',tracking=True)
