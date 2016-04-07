"""
General purpose CSV utility functions
"""

import csv


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
