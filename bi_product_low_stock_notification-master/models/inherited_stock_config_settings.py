# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api, _
from ast import literal_eval


class ResConfigSettings(models.TransientModel):
	_inherit = ['res.config.settings']


	notification_base = fields.Selection([('on_hand','On hand quantity'),('fore_cast','Forecast')],related='company_id.notification_base',string='Notification Based On')
	notification_products = fields.Selection([('for_all','Global for all product'),('fore_product',' Individual for all products')],related='company_id.notification_products',string='Min Quantity Based On')
	min_quantity = fields.Float(string = 'Quantity Limit',related='company_id.min_quantity')
	notification_user_id = fields.Many2one('res.users',related='company_id.notification_user_id',string = 'Notify User')
	email_user = fields.Char( string="Email From",related='company_id.email') 
	low_stock_products_ids = fields.One2many('low.stock.transient','stock_product_id',store=True)



	def action_list_products_(self):
		products_list=[]
		
		res = self.env['res.config.settings'].search([],order="id desc", limit=1)
		if res.id :
			products_dlt = [(2,dlt.id,0)for dlt in res.low_stock_products_ids]
			
		
			res.low_stock_products_ids = products_dlt

			if res.notification_base == 'on_hand':
				if res.notification_products == 'for_all':
					result = self.env['product.product'].search([('qty_available','<',res.min_quantity)])
					
					
					for product in result:
						
						products_list.append([0,0,{'name':product.name,
												'limit_quantity':res.min_quantity,
												'stock_quantity':product.qty_available}])
		
				
				if res.notification_products == 'fore_product':
					
					result = self.env['product.product'].search([])
					

					for product in result:
						if product.qty_available < product.min_quantity:
							products_list.append([0,0,{'name':product.name,
														'limit_quantity':product.min_quantity,
													'stock_quantity':product.qty_available}])


			if res.notification_base=='fore_cast':
				if res.notification_products=='for_all':
					result = self.env['product.product'].search([('virtual_available','<',res.min_quantity)])
					for product in result:
						products_list.append([0,0,{'name':product.name,
												'stock_quantity':product.virtual_available}])
				if res.notification_products == 'fore_product':
					result = self.env['product.product'].search([])

					for product in result:
						if product.virtual_available < product.min_quantity:
							products_list.append([0,0,{'name':product.name,
														'limit_quantity':product.min_quantity,
													'stock_quantity':product.virtual_available}])

				

			
			res.low_stock_products_ids = products_list

				
			return 
		else :
			return




	
	
		
	def action_low_stock_send(self):
		self.action_list_products_()
		
		res = self.env['res.config.settings'].search([],order="id desc", limit=1)
		
		if res.id :
		
		
			
			template_id = self.env.ref('bi_product_low_stock_notification.low_stock_email_template')
			
			send = template_id.send_mail(res.id, force_send=True)
		
			return True

		
		
		return True
	


class low_stock_product(models.TransientModel):
	_name='low.stock.transient'


	name=fields.Char(string='Product name')
	stock_quantity=fields.Float(string='Quantity')
	limit_quantity=fields.Float(string='Quantity limit')
	stock_product_id=fields.Many2one('res.config.settings')

