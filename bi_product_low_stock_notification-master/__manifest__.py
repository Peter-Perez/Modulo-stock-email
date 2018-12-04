 # -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
	'name': 'Product Low Stock Notification',
	'version': '11.0.0.1',
	'category': 'Inventory',
	'sequence':140 ,
    "price": 19,
    "currency": 'EUR',
	'summary': 'This apps help to receive low stock notification about product when product stock goes below on certian stock.',
	'description': """To send notification to user while stock is low
		This apps help to receive low stock notification about product when product stock goes below on certian stock
		product low stock notification
		product low stock notify
		product low stock alerts
		product low stock alarm
		email notificaion about low stock products
		configurable low stock for product , send email notification for low stock product
		product stock alerts
		product stock notification
		product stock alarm
		product stock email notification
		low product stock notification
		low stock product notification
		low stock product alert
		alert low stock product
		alert stock low product

		minimum product stock alerts
		minimum product stock notification
		warehouse stock alerts
		warehouse stock notification
		warehouse stock alarms
		warehouse product stock alerts
		warehouse product stock notification
		warehouse product stock alarms

		warehouse low stock alerts
		warehouse low stock notification
		warehouse low stock alarms
		warehouse low product stock alerts
		warehouse low product stock notification
		warehouse low product stock alarms
		warehouse minimum stock alerts
		warehouse minimum stock notification
		warehouse minimum stock alarms
		warehouse minimum product stock alerts
		warehouse minimum product stock notification
		warehouse minimum product stock alarms
	""",
	'author':'Browseinfo',
	'website': 'https://www.browseinfo.in',
	'depends': ['base','sale_management','stock','mail'],
	'data': [
	'view/product_product_view.xml',
	'view/email_templete.xml',
	'view/stock_config_settings_views.xml',
	'data/low_stock_notification_cron.xml',
			
	],
	
	'test': [],
		
	
	'demo': [],
	'css': [],
	'installable': True,
	'auto_install': False,
	'application': False,
    "images":['static/description/Banner.png'],
}


