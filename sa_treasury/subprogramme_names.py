from datapackage_pipelines.wrapper import process


def modify_datapackage(datapackage, parameters, stats):
    return datapackage


def process_row(row, row_index,
                resource_descriptor, resource_index,
                parameters, stats):
    if row['subprogramme'] == 'Community sport':
        row['subprogramme'] = 'Community Sport'
    return row


process(modify_datapackage=modify_datapackage,
        process_row=process_row)
