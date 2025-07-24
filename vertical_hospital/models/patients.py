# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class VerticalPatient(models.Model):
    _name = 'vertical.patients'
    _order = 'id desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    company_id = fields.Many2one('res.company', store=True, copy=False,
                                 string="Company",
                                 default=lambda self: self.env.user.company_id.id)

    name = fields.Char(default=lambda self: _('New'), required=True, copy=False)
    state = fields.Selection([('draft', 'Draft'), ('high', 'High'), ('low', 'Low')], default='draft', tracking=True)
    patient_name = fields.Char(string='Patient Name', required=True)
    patient_last_name = fields.Char(string='Last Name', required=True)
    rnc = fields.Char(string="RNC", size=9, required=True, tracking=True)
    discharge_datetime = fields.Datetime(string='Discharge Date')
    update_datetime = fields.Datetime(string='Update Date', required=True, default=fields.Datetime.now, tracking=True)
    treatments_performed = fields.Many2many('vertical.treatments', string='Treatments Performed')


    @api.onchange('rnc')
    def _check_rnc_digits(self):
        for record in self:
            if record.rnc and not record.rnc.isdigit():
                raise ValidationError(_("The RNC must contain only numbers."))

    def get_state_display(self):
        return dict(self._fields['state']._description_selection(self.env)).get(self.state)

    @api.model
    def create(self, values):
        if not values.get('name', False) or values['name'] == _('New'):
            values['name'] = self.env['ir.sequence'].next_by_code('patients.sequence') or _('New')

        record = super(VerticalPatient, self).create(values)

        return record

    def write(self, vals):
        vals['update_datetime'] = fields.Datetime.now()
        return super().write(vals)