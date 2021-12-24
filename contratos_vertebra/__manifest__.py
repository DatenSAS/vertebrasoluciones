# -*- coding: utf-8 -*-
{
    'name': 'Contratos - Vertebra',
	'version': '15.0.1.0',
    "category": "Contratos",
    "website": "https://www.daten.com.co/",
    'description': u"""
Manejo de Contratos Soluciones Vertebra
    """,
    'author': u'Carlos Alberto Villarreal',
    'depends': ['base','mail'],
    'data' : ['views/contratos.xml',
              'views/prorrogas.xml',
              'views/etapas.xml',
              'views/facturacion.xml',
              'views/gastos.xml'
              'security/ir.model.access.csv'
        ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
