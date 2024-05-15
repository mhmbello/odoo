# -*- encoding: utf-8 -*-
{
    'name': 'Etats legaux Maroc',
    'version': '1.0',
    'category': 'HR',
    'complexity': "normal",
    'description': """
    Etats legaux Maroc : Journal de paie, Bulletin de paie, Bordereau de virement, Etat CNSS, Bordereau paiement CNSS
""",
    'author': 'R&B Consulting',
    'website': 'http://www.rb-consulting.com',
    'images': [],
    'depends': ['hr_payroll_ma',
                ],
    'data': [
             'custom_bulletin_form_view.xml',
             'custom_payroll_parametres_view.xml',
             'report/reports_view.xml',
             'report/bulletin.xml',
             'report/journal_paie.xml',
             'report/bordereau_virement.xml',
             'report/etat_cnss.xml',
             'report/etat_igr.xml',
             'report/bordereau_paiement_cnss.xml',
             'wizard/wizard_export_journal_paie_view.xml',
             'wizard/wizard_export_bulletin_paie_view.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

