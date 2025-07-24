from odoo import http
from odoo.http import request, Response
import json


class PatientsController(http.Controller):

    @http.route(['/api/<path:url_param>'], type='http', auth='public', methods=['GET'], csrf=False)
    def consulta_paciente(self, url_param, **kw):
        # Read the endpoint from the system parameter
        expected_endpoint = request.env['ir.config_parameter'].sudo().get_param('vertical_hospital.webserver_endpoint')

        # Remove possible leading or trailing slashes for safe comparison
        normalized_param = '/' + url_param.strip('/')
        normalized_expected = expected_endpoint.strip()

        if not expected_endpoint or not normalized_param.startswith(normalized_expected):
            return Response(
                json.dumps({'error': 'Ruta no válida o no coincide con el endpoint configurado'}),
                status=403,
                content_type='application/json'
            )

        # Extract the sequence from the URL parameter
        sequence = normalized_param.replace(normalized_expected, '', 1).strip('/')
        if not sequence:
            return Response(
                json.dumps({'error': 'Secuencia no especificada'}),
                status=400,
                content_type='application/json'
            )

        patient = request.env['vertical.patients'].sudo().search([('name', '=', sequence)], limit=1)

        if not patient:
            return Response(
                json.dumps({'error': 'Paciente no encontrado'}),
                status=404,
                content_type='application/json'
            )

        return Response(
            json.dumps({
                'seq': patient.name,
                'nombre': f"{patient.patient_name} {patient.patient_last_name}",
                'rnc': patient.rnc,
                'estado': patient.state
            }),
            status=200,
            content_type='application/json'
        )
