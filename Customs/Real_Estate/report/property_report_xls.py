from odoo import models
import base64
import io

class PropertyReportXlsx(models.AbstractModel):
    _name = 'report.real_estate.report_properties_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, properties):

        bold = workbook.add_format({'bold': True})
        format1=workbook.add_format({'bold':True ,'align':'center','bg_color':'yellow'})
        '''format2=workbook.add_format({'align':'center','style':'width:40%'})'''



        for obj in properties:
            sheet = workbook.add_worksheet(obj.name)
            row = 3
            col = 3
            sheet.set_column('D:D', 14)
            sheet.set_column('E:E', 15)

            row += 1
            sheet.merge_range(row, col,row,col + 1, 'Property ID', format1)

            row += 1
            if obj.image:
                property_image=io.BytesIO(base64.b64decode(obj.image))
                sheet.insert_image(row, col, "image.png", {'image_data':property_image,'x_scale': 0.15, 'y_scale': 0.15})
                row += 6


            sheet.write(row, col,'Name', bold)
            sheet.write(row, col + 1, obj.name)
            row += 1
            sheet.write(row, col, 'Expected_Price', bold)
            sheet.write(row, col + 1, obj.expected_price)
            row += 1
            sheet.write(row, col, 'Selling_Price', bold)
            sheet.write(row, col + 1, obj.selling_price)
            row += 1
            sheet.write(row, col, 'Best Offer', bold)
            sheet.write(row, col + 1, obj.best_price)
            row += 2
            '''row += 1
            sheet.write(row, col, 'Tag', bold)
            sheet.write(row, col + 1, obj.tag_ids)'''
