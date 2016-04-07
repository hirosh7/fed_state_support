"""
Process raw state government finance data retrieved from http://www.census.gov/govs/state/
State Government Finances provides a comprehensive summary of annual survey findings for state
governments. The tables and data files present the following details:

Revenue, by source of revenue
Expenditure, by object and function of expenditure
Indebtedness, by long-term or short-term debt, and
Asset, by purpose and type of asset

This data will be refined into a new CSV file which can be used by Tableau for data visualization
"""

from utilities import csvtools


def _row2dictitem(in_row):
    """
    Process a state revenue data row The standard format is as follows:

    Field Name	    Position	Start Position	Length	Characteristic
    ------------------------------------------------------------------
    Government ID 	     1-14	     1	            14	    Numeric,zero filled
    Item Code           15-17	    15	             3	    Alpha numeric
    Amount (thousands)	18-29	    18	            12	    Numeric
    Survey Year	        30-31	    30	             2	    Numeric
    Year of Data	    32-33	    32	             2	    Numeric
    Origin	            34-35	    34	             2	    Alpha Numeric

    **Note: Actual length of data appears to be 38 characters vs. 35 with the additional three characters belonging
            to the amount data item (i.e. it appears to be 15 characters not 12)

    :param in_row: a row of state data
    :return: dictionary [field name: value]
    """

    out_dict = {'ID': in_row[:14], 'Item Code': in_row[14:17], 'Amount': int(in_row[18:32].strip()),
                'Survey Year': in_row[32:34], 'Year of Data': in_row[34:36], 'Origin': in_row[36:38]}

    return out_dict


def process_state_data(in_file, state_lu, item_lu):
    """
    Process a state revenue file. Parse all fields into a dictionary

    :param state_lu: state lookup table
    :param item_lu: item code lookup table
    :param in_file: state revenue file (text)
    :return: data dictionary [field name: value]
    """

    out_dict = {}

    fh = open(in_file)
    st_data = fh.read()

    # create a list, one row = one list item
    st_data_list = st_data.split('\n')

    # break row data up into the appropriate
    row_cnt = 1
    for row in st_data_list:

        # add itemized row data
        out_dict[row_cnt] = _row2dictitem(row)

        # add government name, item code name
        if out_dict[row_cnt]['ID'] in state_lu.keys():
            out_dict[row_cnt]['State'] = state_lu[out_dict[row_cnt]['ID']]['State']

        if out_dict[row_cnt]['Item Code'] in item_lu.keys():
            out_dict[row_cnt]['Item'] = item_lu[out_dict[row_cnt]['Item Code']]['Description']

        row_cnt += 1

    return out_dict


def build_lookup(in_file, key_fld):

    """
    Take the official government name and ID table and convert it into a dictionary with the ID as the key and
    state government name as the value
    :param in_file: government name/ID text file
    :param key_fld: dictionary key field
    :return: lookup dictionary [key_fld:row data]
    """

    csv_dict = csvtools.csv2dict(in_file, key_fld)

    return csv_dict

if __name__ == "__main__":

    # data files
    gov_id_file = 'data/government_ids.csv'
    gov_itemcode_file = 'data/itemcodes.csv'
    state_data_file = 'data/13state35.txt'

    # set up lookup tables
    gov_id_lookup = build_lookup(gov_id_file, 'ID Code')
    gov_itemcode_lookup = build_lookup(gov_itemcode_file, 'Item Code')

    # get state data
    state_data = process_state_data(state_data_file, gov_id_lookup, gov_itemcode_lookup)
