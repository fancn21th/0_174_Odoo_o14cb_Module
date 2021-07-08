# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Teachers(models.Model):
    _name = 'keen.teachers'

    name = fields.Char()
