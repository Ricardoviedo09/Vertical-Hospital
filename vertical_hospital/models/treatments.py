# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class VerticalTreatments(models.Model):
    _name = 'vertical.treatments'
    _order = 'id desc'

    name = fields.Char(required=True)
    code = fields.Char(string='Code', required=True)
    treating_doctor = fields.Char(string='Treating Doctor', required=True)


    @api.constrains('code')
    def validate_without_026(self):
        if "026" in self.code:
            raise ValidationError(_("The text cannot contain the sequence '026'."))
