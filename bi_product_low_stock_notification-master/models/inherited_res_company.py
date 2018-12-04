# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models

class Company(models.Model):
	_inherit = 'res.company'



	notification_base = fields.Selection([('on_hand','On hand quantity'),('fore_cast','Forecast')],string='Notification Based On',default='on_hand')
	notification_products = fields.Selection([('for_all','Global for all product'),('fore_product',' Individual for all products')],string='Min Quantity Based On',default='for_all')
	min_quantity = fields.Float(string = 'Quantity Limit')
	notification_user_id = fields.Many2one('res.users',string = 'Notify User')