"""
General purpose CSV utility functions
"""

import csv


def write_csv_data(out_file, flds, out_data):
    """
    Write dictionary data out to a CSV file

    :param out_file: output file name
    :param flds: column header names
    :param out_data: dictionary data to write out to CSV file
    :return: None
    """

    with open(out_file, 'wb') as out_file:
        writer = csv.DictWriter(out_file, fieldnames=flds)
        headers = dict((n, n) for n in flds)
        writer.writerow(headers)
        for row in out_data:
            writer.writerow(row)


def csv2dict(in_file, key_fld):
    """
    Read in a CSV file build a data dictionary using the key_fid as the key for the rest of the data
    :param in_file: CSV file
    :param key_fld: key field (string)
    :return: data dictionary with each row of data accessible by the key_fld
    """

    out_dict = {}

    with open(in_file, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if key_fld in row.keys():
                out_dict[row[key_fld]] = row
            else:
                raise ValueError("Key Field: {0} not found in data".format(key_fld))

    return out_dict
