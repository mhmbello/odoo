# -*- encoding: utf-8 -*-

from odoo import api, fields, models, _

class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    bulletin_id = fields.Many2one(comodel_name="hr.payroll_ma.bulletin", string="Bulletin")