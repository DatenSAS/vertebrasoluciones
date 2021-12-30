# -*- coding: utf-8 -*-
from openerp import fields, models, api
from odoo import exceptions

class project_task(models.Model):
    _inherit = 'project.task'

    cliente_id = fields.Integer(related='partner_id.id')
    punto = fields.Many2one('punto',string='Punto',tracking=True)
    contrato = fields.Many2one('contratos', string='Contrato', tracking=True)
    url = fields.Char(string='URL',tracking=True)
    adjunto = fields.Binary(string='Adjunto',tracking=True)
    nombre_adjunto = fields.Char(string='Nombre Adjunto')
    tipo = fields.Selection(
        [('M&T', 'M&T'), ('Ecoeficiencia', 'Ecoeficiencia')],
        'Tipo',
        related='project_id.tipo'
    )
    cuenta = fields.Many2one('cuenta', string='Cuenta',tracking=True)
    grupo = fields.Char(related='punto.grupo.name')
    ciudad = fields.Char(related='punto.ciudad')
    servicio = fields.Char(related='cuenta.servicio')
    comercializador = fields.Char(related='cuenta.prestador_servicio', string='Comercializador Actual')
    contrato_firmado = fields.Boolean(string='Contrato Firmado',tracking=True)
    comercializador_nuevo = fields.Many2one('res.partner', string='Comercializador Nuevo',tracking=True)
    fecha_visita = fields.Date(string='Fecha de Visita',tracking=True)
    fecha_cambio = fields.Date(string='Fecha de Cambio',tracking=True)
    registro_xm_date = fields.Date(string = "Registro XM",tracking=True)
    cuenta_nueva = fields.Many2one('cuenta', string='Cuenta Nueva',tracking=True)
    paz_salvo = fields.Boolean(string='Paz y Salvo',tracking=True)
    fecha_inicio = fields.Date(string='Fecha Inicio',tracking=True)
    fecha_final = fields.Date(string='Fecha Final',tracking=True)
    inicio_periodo = fields.Date(string='Inicio Periodo',tracking=True)
    final_periodo = fields.Date(string='Final Periodo',tracking=True)
    inicio = fields.Date(string='Inicio',tracking=True)
    final = fields.Date(string='Final',tracking=True)
    mes_primer = fields.Selection(
        [('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'),
         ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'),
         ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')],
        'Mes Primer Pago'
    )
    prestador_aseo_check = fields.Boolean(string='Prestador Aseo',tracking=True)
    prestador_ap_check = fields.Boolean(string='Prestador AP',tracking=True)

    prestador_aseo = fields.Many2one('res.partner', string='Empresa Aseo',tracking=True)
    prestador_ap = fields.Many2one('res.partner', string='Empresa AP',tracking=True)
    continuidad_serv = fields.Selection(
        [('Proceso Pendiente', 'Proceso Pendiente'), ('Cobros OK', 'Cobros OK'),
         ('Cobros con Reclamación', 'Cobros con Reclamación'),
         ('Cobro AP con Reclamación', 'Cobro AP con Reclamación'),
         ('Cobro Aseo con Reclamación', 'Cobro Aseo con Reclamación')],
        'Continuidad Otros Servicios', tracking=True
    )
    portal_web = fields.Boolean(string='Portal Web',tracking=True)
    portal_vt = fields.Boolean(string='Portal VT',tracking=True)
    resultado = fields.Selection(
        [('Proceso Pendiente', 'Proceso Pendiente'), ('Empalme OK', 'Empalme OK'),
         ('Empalme con Reclamación', 'Empalme con Reclamación')],
        'Resultado',tracking=True
    )
    razon = fields.Selection(
        [('Margen de Ahorro Minimo', 'Margen de Ahorro Mínimo'),
         ('No hay Mercado Comercialización', 'No hay Mercado Comercialización'),
         ('No hay Autorización por Parte del Propietario', 'No hay Autorización por Parte del Propietario'),
         ('Requiere Firma Pagaré o Firmas', 'Requiere Firma Pagaré o Firmas'),
         ('No hay Autorización por Parte del Centro Comercial', 'No hay Autorización por Parte del Centro Comercial'),
         ('Desconocimiento del Procedimiento', 'Desconocimiento del Procedimiento'),
         ('Negación Paz y Salvo', 'Negación Paz y Salvo'),
         ('Requiere Inversiones Adecuación Sistema de Medida', 'Requiere Inversiones Adecuación Sistema de Medida'),
         ('Traslado de Oficina', 'Traslado de Oficina'),
         ('Almacenaje', 'Almacenaje'),
         ('Consumo Menor Mínimo Viable', 'Consumo Menor Mínimo Viable'),
         ('Consumo Cero', 'Consumo Cero'),
         ('Medida Centralizada / Blindobarras', 'Medida Centralizada / Blindobarras')],
        'Razón No Viabilidad',tracking=True
    )

    empleados = fields.Integer(string = "Cantidad de Empleados de Planta",tracking=True)
    pisos = fields.Char(string = "Número de Pisos",tracking=True)
    area = fields.Float(string = "Área en m2",tracking=True)
    dias_lab = fields.Integer(string = "Días laborados a la semana",tracking=True)
    horario_st = fields.Float(string="Horario de trabajo", tracking=True)
    horario_end = fields.Float(tracking=True)
    turnos = fields.Char(string = "Número de turnos al día",tracking=True)
    distribuidor_energia = fields.Many2one('res.partner',string="Distribuidor")
    tension = fields.Float(string="Nivel de tensión (V)",tracking=True)
    cuentas = fields.Integer(string="Número de cuentas de energía",tracking=True)
    potencia = fields.Float(string="Potencia Instalada (kW)",tracking=True)
    consumo = fields.Float(string="Consumo Energía Mensual (kW/mes)",tracking=True)
    medidor_energia = fields.Char(string = "Número medidor de Energía",tracking=True)
    medidor_acueducto = fields.Char(string="Número medidor de Acueducto",tracking=True)
    cont_nombre = fields.Char(string="Nombre y Apellido",tracking=True)
    cont_cargo = fields.Char(string="Cargo",tracking=True)
    cont_cel = fields.Char(string="Teléfono Celular",tracking=True)
    cont_email = fields.Char(string="Correo Electrónico",tracking=True)
    dir_predio = fields.Boolean (string="Foto Dirección del Predio",tracking=True)
    panoramica = fields.Boolean(string="Foto Panoramica del predio completo fachada",tracking=True)
    medidores_energia = fields.Boolean(string="Foto medidor(es) de energía",tracking=True)
    caja_energia = fields.Boolean(string="Foto Panorámica de caja donde se aloja el medidor de energía",tracking=True)
    medidores_agua = fields.Boolean(string="Foto medidor(es) de agua",tracking=True)
    caja_agua = fields.Boolean(string="Foto Panorámica de caja donde se aloja el medidor de agua",tracking=True)
    total = fields.Boolean(string="Fotos totalizador y tableros generales del lugar",tracking=True)
    sitio = fields.Boolean(string="Foto lugar donde se podria instalar el equipo de medida",tracking=True)
    breaker = fields.Boolean(string="Foto con marcación de breaker totalizador",tracking=True)
    nivel = fields.Boolean(string="Foto con nivel de señal celular",tracking=True)
    cts = fields.Boolean(string="Foto de conductores donde se deben instalar los CTS de medida",tracking=True)
    observaciones = fields.Text(string="Observaciones",tracking=True)
    es_viable = fields.Boolean(string="Es viable la instalación",tracking=True)
    fecha_hora_ins = fields.Datetime(string="Fecha y Hora",tracking=True)
    ubicacion = fields.Char(string="Ubicación",tracking=True)
    sch_week_st = fields.Float(string ="Horarios L-V", tracking=True)
    sch_week_end = fields.Float(tracking=True)
    sch_weekend_st = fields.Float(string ="Horarios S,D,F", tracking=True)
    sch_weekend_end = fields.Float(tracking=True)
    nivel_ten = fields.Float(string="Nivel de tensión (L - L)", tracking=True)
    tipo_ins = fields.Selection(
        [('Trifásica', 'Trifásica'),('Bifásica', 'Bifásica'), ('Monofásica', 'Monofásica')],
        'Tipo de Instalación',tracking=True
    )
    equipo = fields.Many2one('stock.production.lot', string="Número de Equipo")
    nivel_cel = fields.Selection(
        [('Mala', 'Mala'), ('Buena', 'Buena'), ('Excelente', 'Excelente')],
        'Nivel de Señal', tracking=True
    )
    sim_card = fields.Many2one('stock.production.lot', string="SIM")
    operador = fields.Selection(
        [('Claro', 'Claro'),('Movistar', 'Movistar'), ('Tigo', 'Tigo')],
        'Operador',tracking=True
    )
    observaciones_ins = fields.Text(string="Observaciones",tracking=True)
    tec_vis = fields.Many2one('res.partner', string="Inspector",tracking=True)
    tec_ins = fields.Many2one('res.partner', string="Técnico Instalador",tracking=True)

    medidas = fields.Binary(string='Registro Medidas')
    nombre_medidas = fields.Char(string='Nombre Medidas')

    fecha_recepcion_doc = fields.Date(string='Fecha de Recepción del documento',tracking=True)
    task_ticket = fields.Many2one('helpdesk.ticket', string="Ticket Generado",tracking=True)
    task_ticket_ap = fields.Many2one('helpdesk.ticket', string="Ticket Generado AP", tracking=True)
    task_ticket_aseo = fields.Many2one('helpdesk.ticket', string="Ticket Generado Aseo", tracking=True)

    cancelado = fields.Selection(
        [('Solicitud de Cliente', 'Solicitud de Cliente'),('Cierre de Punto', 'Cierre de Punto'),
         ('Sin Autorización de Ingreso', 'Sin Autorización de Ingreso'),('Otros','Otros')],
        'Justificación',tracking=True
    )

    modalidad = fields.Selection(
        [('Comodato', 'Comodato'), ('Cambio de Medidor', 'Cambio de Medidor')],
        'Modalidad', tracking=True
    )

#   Control flujo 'Cambio de Comercializador'

    @api.onchange('stage_id')
    def contrato_done(self):
        stages = [23, 24, 25]
        if self._origin.stage_id.id == 22 and self.stage_id.id in stages and self.contrato_firmado == False and self.tipo == "M&T":
            raise exceptions.UserError('No existe contrato firmado.')

    @api.onchange('stage_id')
    def mx_cuenta_nueva_done(self):
        stages = [24, 25]
        if self._origin.stage_id.id == 23 and self.stage_id.id in stages and (not self.registro_xm_date or not self.cuenta_nueva) and self.tipo == "M&T":
            raise exceptions.UserError('Falta diligenciar el Registro XM o la Cuenta Nueva')

    @api.onchange('stage_id')
    def verificacion_done(self):

        stages = [25]

        if self._origin.stage_id.id == 24 and self.stage_id.id in stages and self.tipo == "M&T":
            if not self.paz_salvo:
                raise exceptions.UserError('Falta Paz y Salvo')
            if not self.fecha_inicio:
                raise exceptions.UserError('Falta Fecha Inicio Última Factura Comercializador Anterior')
            if not self.fecha_final:
                raise exceptions.UserError('Falta Fecha Final Última Factura Comercializador Anterior')
            if not self.inicio_periodo:
                raise exceptions.UserError('Falta Inicio Periodo Factura Cierre')
            if not self.final_periodo:
                raise exceptions.UserError('Falta Final Periodo Factura Cierre')
            if not self.inicio:
                raise exceptions.UserError('Falta Inicio Primera Factura Comercializador Nuevo')
            if not self.final:
                raise exceptions.UserError('Falta Final Primera Factura Comercializador Nuevo')
            if not self.mes_primer:
                raise exceptions.UserError('Falta Primer Mes Primera Factura Comercializador Nuevo')
            if not self.resultado:
                raise exceptions.UserError('Falta Resultado Primera Factura Comercializador Nuevo')
            if self.prestador_ap_check and not self.prestador_ap:
                raise exceptions.UserError('Falta Prestador AP')
            if self.prestador_aseo_check and not self.prestador_aseo:
                raise exceptions.UserError('Falta Prestador Aseo')
            if not self.portal_web:
                raise exceptions.UserError('Falta Portal Web')
            if not self.portal_vt:
                raise exceptions.UserError('Falta Portal VT')
            if not self.continuidad_serv:
                raise exceptions.UserError('Falta Continuidad Otros')
            if self.resultado != 'Empalme OK':
                raise exceptions.UserError('El campo "Resultado" debe ser "Empalme Ok" para pasar a la etapa de Cerrado')
            if self.continuidad_serv != 'Cobros OK':
                raise exceptions.UserError('El campo "Continuidad Otros Servicios" debe ser "Cobros Ok" para pasar a la etapa de Cerrado')

    @api.onchange('stage_id')
    def stage_no_viable(self):
        stages = [20,21,22]
        if self._origin.stage_id.id in stages and self.contrato_firmado != False and self.stage_id.id == 26:
            raise exceptions.UserError('Solo se permite cuentas con contratos no firmados desde estas etapas')
        if self._origin.stage_id.id == 25 and self.stage_id.id == 26:
            raise exceptions.UserError('No se permite este cambio de etapa')
        if self._origin.stage_id.id == 24 and self.stage_id.id == 26:
            raise exceptions.UserError('No se permite este cambio de etapa')

#   Control flujo 'Visita e Instalaciones Ecoeficiencia

    @api.onchange('stage_id')
    def a_cancelado(self):
        stages=[27,28,30,31]
        if self._origin.stage_id.id in stages and self.stage_id.id == 44:
            raise exceptions.UserError('No es posible este cambio de etapa')

    @api.onchange('stage_id')
    def desde_pendiente(self):
        stages=[28,29]
        if self._origin.stage_id.id == 27 and self.stage_id.id in stages:
            if not self.partner_id :
                raise exceptions.UserError('Falta diligenciar el cliente')
            if not self.punto:
                raise exceptions.UserError('Falta diligenciar el punto')
            if not self.user_ids:
                raise exceptions.UserError('Falta asignar esta tarea')

    @api.onchange('stage_id')
    def a_cerrado(self):
        stages = [27,28,29,30]
        if self._origin.stage_id.id in stages and self.stage_id.id == 31:
            if self.project_id.tipo == 'Ecoeficiencia - Visita':
                if not self.url:
                    raise exceptions.UserError('Falta diligenciar la URL')
                if not self.adjunto:
                    raise exceptions.UserError('Falta diligenciar el Adjunto')
            if self.project_id.tipo == 'Ecoeficiencia - Instalaciones':
                if not self.tec_ins:
                    raise exceptions.UserError('Falta diligenciar el Técnico Instalador')
                if not self.fecha_hora_ins:
                    raise exceptions.UserError('Falta diligenciar Fecha y Hora de Instalación')
                if not self.ubicacion:
                    raise exceptions.UserError('Falta diligenciar la Ubicación')
                if not self.sch_week_st or not self.sch_week_end:
                    raise exceptions.UserError('Falta diligenciar Horarios Entre Semana')
                if not self.nivel_ten:
                    raise exceptions.UserError('Falta diligenciar Niveles de Tensión')
                if not self.equipo:
                    raise exceptions.UserError('Falta diligenciar Número de Equipo')
                if not self.sim_card:
                    raise exceptions.UserError('Falta diligenciar Número de SIM')
                if not self.operador:
                    raise exceptions.UserError('Falta diligenciar Operador')
                if not self.medidas:
                    raise exceptions.UserError('Falta diligenciar Archivo Adjunto de Medidas')

# Generación de tickets para el cambio de comercializador

    def generar_ticket(self):
        ticket = self.env['helpdesk.ticket'].create({
                'kanban_state':'normal',
                'name':self.name + '-' + 'Reclamación',
                'team_id': 1,
                'partner_id': self.partner_id.id,
                'punto':self.punto.id,
                'description':'Este ticket fue generado desde el proceso de Cambio de Comercializador como resultado de un empalme con Reclamación'
                })
        self.task_ticket = ticket.id

    def generar_ticket_ap(self):
        ticket = self.env['helpdesk.ticket'].create({
                'kanban_state':'normal',
                'name':self.name + '-' + 'Reclamación',
                'team_id': 1,
                'partner_id': self.partner_id.id,
                'punto':self.punto.id,
                'description':'Este ticket fue generado desde el proceso de Cambio de Comercializador como resultado de una Reclamación de Alumbrado Público'
                })
        self.task_ticket_ap = ticket.id

    def generar_ticket_aseo(self):
        ticket = self.env['helpdesk.ticket'].create({
                'kanban_state':'normal',
                'name':self.name + '-' + 'Reclamación',
                'team_id': 1,
                'partner_id': self.partner_id.id,
                'punto':self.punto.id,
                'description':'Este ticket fue generado desde el proceso de Cambio de Comercializador como resultado de una Reclamación de Aseo'
                })
        self.task_ticket_aseo = ticket.id


    # Check de formato de visita que permite seleccionar como viable la instalación

    @api.onchange('es_viable')
    def viabilidad (self):

        check = True

        if not self.tec_vis or not self.pisos or not self.horario_st or not self.horario_end or not self.turnos or not self.distribuidor_energia \
        or not self.medidor_energia or not self.medidor_acueducto or not self.dir_predio or not self.panoramica or \
        not self.medidores_energia or not self.medidores_agua or not self.caja_agua or not self.caja_energia or not \
        self.total or not self.sitio or not self.nivel or not self.cts or not self.empleados or not self.pisos or not self.area or not self.dias_lab \
        or not self.turnos or not self.tension or not self.cuentas or not self.potencia or not self.consumo or not self.medidor_energia or not self.medidor_acueducto:
            check = False

        if self.es_viable and not check:
            raise exceptions.UserError('Falta Diligenciar Completamente el Formato de Visita. No se Admiten Campos en Cero')

    # Sacar una tarea del flujo de ecoeficiencia de la etapa de cancelado solo es posible por un rol supervisor

    @api.onchange('stage_id')
    def desde_cancelada(self):

        usuario = self.env['res.user'].search(self._uid)
        grupos = usuario.groups_ids
        check = False

        for grupo in grupos:
            if grupo == 17:
                check = True

        if self._origin.stage_id.id == 44 and not check:
            raise exceptions.UserError('Este cambio de etapa solo puede realizarse por un rol Supervisor')






