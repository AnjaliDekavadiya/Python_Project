{
	'name': 'Testing_Estate',
	'depends': ['base','mail','report_xlsx'],
	'data': ['data/res.country.state.csv',
			 'data/ir.model.access.csv',
			 'data/number.xml',
			 'wizard/create_offer_view.xml',
			 'views/estate_property_views.xml',
			 'views/property_type_views.xml',
			 'views/user.xml',
			 'report/properties_detail_template.xml',
			 'report/report.xml'],

	'sequence':-100,
	'application':'True',
	'installable':True
}