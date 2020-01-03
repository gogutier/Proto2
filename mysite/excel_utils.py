import io
import xlsxwriter

def WriteToExcel(weather_data, town=None):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})

    #worksheet = workbook.add_worksheet()
    #worksheet.write(0, 0, 'Hello, world!')

    title = workbook.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter'
    })
    header = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })

    cell_center = workbook.add_format({
        #'bg_color': '#000000',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 0
    })

    cell = workbook.add_format({
        #'bg_color': '#000000',
        'color': 'black',
        #'align': 'center',
        'valign': 'top',
        'border': 0
    })

    worksheet_s = workbook.add_worksheet("Summary")


    worksheet_s.write(0, 0, "Pallet", header)
    worksheet_s.write(0, 1, "ID"    , header)
    worksheet_s.write(0, 2, "Calle", header)
    # the rest of the headers from the HTML file

    # Here we will adding the code to add data
    '''
    for idx, data in enumerate(weather_data):
        row = 1 + idx
        #worksheet_s.write_number(row, 0, idx + 1, cell_center)
        worksheet_s.write_string(row, 0, data.pallet, cell)
        worksheet_s.write_string(row, 1, data.ORDERID, cell)
        worksheet_s.write_string(row, 2, data.calle, cell)
    #worksheet_s.write(row, 2, data.date.strftime('%d/%m/%Y'), cell_center)
    # the rest of the data
    '''

    row=0
    print(weather_data)
    for data in weather_data:
        for pallet in weather_data[data]['palletsencontrados'][0]:
            row = 1 + row
            #worksheet_s.write_number(row, 0, idx + 1, cell_center)
            worksheet_s.write_string(row, 0, pallet, cell)
            worksheet_s.write_string(row, 1, data, cell)
            worksheet_s.write_string(row, 2, "Encontrado OK", cell)

        for pallet in weather_data[data]['palletsnoencontrados'][0]:
            row = 1 + row
            #worksheet_s.write_number(row, 0, idx + 1, cell_center)
            worksheet_s.write_string(row, 0, pallet, cell)
            worksheet_s.write_string(row, 1, data, cell)
            worksheet_s.write_string(row, 2, "No encontrado", cell)        


    workbook.close()

    output.seek(0)




    xlsx_data = output.getvalue()
    # xlsx_data contains the Excel file
    return xlsx_data