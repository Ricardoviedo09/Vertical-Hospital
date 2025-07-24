from odoo import fields, models, api
from ast import literal_eval


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    webserver_endpoint = fields.Char(string='Webserver Endpoint')

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()

        self.env['ir.config_parameter'].sudo().set_param(
            'vertical_hospital.webserver_endpoint', self.webserver_endpoint)

        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()

        with_user = self.env['ir.config_parameter'].sudo()

        webserver_endpoint = with_user.get_param('vertical_hospital.webserver_endpoint')

        res.update(webserver_endpoint=webserver_endpoint)

        return res
