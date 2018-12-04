# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api, _


class ProductProduct(models.Model):
	_inherit = ['product.product']

	min_quantity = fields.Float(string='Minimum Quantity')
