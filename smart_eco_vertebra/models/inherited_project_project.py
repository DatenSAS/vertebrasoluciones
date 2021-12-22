# -*- coding: utf-8 -*-
from openerp import fields, models, api

class project_project(models.Model):
    _inherit = 'project.project'

    tipo = fields.Selection(
        [('M&T', 'M&T'), ('Ecoeficiencia - Visita', 'Ecoeficiencia - Visita'),
         ('Ecoeficiencia - Instalaciones', 'Ecoeficiencia - Instalaciones'),
         ('Ecoeficiencia - Sensibilizaciones', 'Ecoeficiencia - Sensibilizaciones')],
        'Tipo'
    )
