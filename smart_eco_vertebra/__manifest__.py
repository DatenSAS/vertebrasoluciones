# -*- coding: utf-8 -*-
{
    'name': 'SmartEco - Vertebra',
	'version': '15.0.1.0',
    "category": "Integración",
    "website": "https://www.daten.com.co/",
    'description': u"""
Integración con plataforma Smart Eco
    """,
    'author': u'Carlos Alberto Villarreal',
    'depends': ['contacts','project'],
    'data' : ['views/smart_eco.xml',
              'views/inherited_res_partner.xml',
              'views/inherited_project_task.xml',
              'views/inherited_project_project.xml',
              'views/inherited_helpdesk_ticket.xml',
              'views/contratos_mt.xml',
              'security/security.xml',
              'security/ir.model.access.csv'
        ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
