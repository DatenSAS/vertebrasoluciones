from openerp import fields, models, api
from odoo import exceptions
from datetime import datetime

class ticket(models.Model):
    _inherit = 'helpdesk.ticket'

    contacto = fields.Many2one('res.partner', string='Contacto',tracking=True, ondelete='restrict')
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
    ticket_cnt = fields.Many2one('helpdesk.ticket', string="Ticket de Continuación",tracking=True, ondelete='restrict')

    cliente_id = fields.Integer(string="Cliente ID")
    punto = fields.Many2one('punto', string='Punto',tracking=True, ondelete='restrict')

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
    tipo_propiedad = fields.Char(related='punto.tipo_propiedad')
    cuenta = fields.Many2one('cuenta', string="Cuenta", ondelete='restrict')
    punto_id = fields.Integer(related='punto.id', string="Punto ID")
    prestador = fields.Char(related='cuenta.prestador_servicio')
    dias_totales = fields.Integer('Días hábiles transcurridos')
    rechazado = fields.Selection(
        [('Gestión Responsabilidad del Cliente', 'Gestión Responsabilidad del Cliente'),
         ('Fuera del Alcance Contratcual', 'Fuera del Alcance Contratcual')
         ],
        'Razón Rechazo',tracking=True
    )

    escalado_a = fields.Many2one('res.partner', string='Escalado a', tracking=True, ondelete='restrict')
    proceso_help = fields.Many2one('proceso', string='Proceso', tracking=True, default=1, ondelete='restrict')
    categoria_help = fields.Many2one('categoria', string='Categoria', tracking=True, ondelete='restrict')
    subcategoria_help = fields.Many2one('subcategoria', string='Sub Categoria', tracking=True, ondelete='restrict')

    proceso_id = fields.Integer(related='proceso_help.id', string="Proceso ID")
    categoria_id = fields.Integer(related='categoria_help.id', string="Categoria ID")

    solucion = fields.Html(string="Solución")
    centro_de_costo = fields.Char(related='punto.centro_costo')
    departamento = fields.Char(related='punto.departamento')
    municipio = fields.Char(related='punto.ciudad')


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
        stages=[14, 16]
        if self._origin.stage_id.id == 1 and self.stage_id.id not in stages:
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
        active = fields.Boolean(string="Active", default=True)

    class categoria(models.Model):
        _name = 'categoria'
        _description = 'Categoria asociada a Reclamaciones'

        name = fields.Char(string='Categoria')
        proceso_id = fields.Many2one('proceso', string='Proceso',tracking=True, ondelete='restrict')
        active = fields.Boolean(string="Active", default=True)

    class subcategoria(models.Model):
        _name = 'subcategoria'
        _description = 'Subcategoria asociada a Reclamaciones'

        name = fields.Char(string='Subcategoria')
        categoria = fields.Many2one('categoria', string='Categoria',tracking=True, ondelete='restrict')
        active = fields.Boolean(string="Active", default=True)
