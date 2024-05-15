# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime, timedelta
from odoo.exceptions import UserError

class ResPartnerBank(models.Model):

    _inherit = 'res.partner.bank'

    is_bank_for_payroll = fields.Boolean(string="Compte paie")
