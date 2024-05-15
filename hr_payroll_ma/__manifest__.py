# -*- encoding: utf-8 -*-
{
    "name": "Gestion de la paie marocaine sous Odoo ",
    'version': '17.0.1.0',
    "author": "R&B Consulting",
    "website": "www.rb-consulting.com",
    "category": "HR",
    "depends": ["base",
                "hr",
                "hr_contract",
                "hr_holidays",
                "account",
                "account_fiscal_period"],
    "description": """
    Gestion de la paie
    Le but de ce module est la gestion de la paie marocaine:
    Gestion des employés.
    Gestion des contrats.
    Configuration des differents paramètres (barème IR,Barème de la prime d'ancienneté,cotisations CNSS,CIMR,Mutuelle,Autres cotisations ...)
    Configuration des rubriques de paie(primes,indemnités,avantages,déductions du net à payer).
    Configuration des rubriques soumise au cotisations,à l'IR,à la prime d'ancienneté ou encore au congés non payés 
    Configuration des comptes de credit et de débit des élements du salaire.
    Gestion des salaires(Calcul automatique de la prime d'ancienneté,heures supplémentaire,cotisations salariales et patronales,IGR...)
    Gestion des congés(Calcul automatique des congés non payés à partir du module hr_holidays)
    Comptabilisation de la paie(géneration d'une seule écritures comptable pour tout les employés chaque période)
    Reporting(Impression des bulletins de paie,journale de paie par période,Ordres de virement par période)
     """,
    "init_xml": [],
    "demo_xml": [],
    'data': [
        # Data

        "import_wizard/hours_import.xml",
        "import_wizard/import_rub.xml",
        "views/config.xml",
        "views/hr_view.xml",
        "views/hr_payroll_ma_view.xml",
        "views/hr_payroll_ma_sequence.xml",
        "views/hr_payroll_ma_data.xml",
        "views/hr_payroll_ma_wizard.xml",
        "views/hr_payroll_variable.xml",
        "views/hr_payroll_loan.xml",
        "views/res_partner_views.xml",
        "security/hr_payroll_ma_security.xml",
        "security/hr_cotisation_security.xml",
        "security/ir.model.access.csv",
        "report/reports_view.xml",
        "report/bulletin_paie.xml",
       

        ],
    'installable' : True,
    'active' : False,
    'license': 'LGPL-3',
}