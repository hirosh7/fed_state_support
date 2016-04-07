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


def build_gov2id_lookup(in_file):
    """
    Take the official government name and ID table and convert it into a dictionary with the ID as the key and
    state government name as the value
    :param in_file: government name/ID text file
    :return: lookup dictionary [ID:gov_name]
    """

    csv_dict = csvtools.csv2dict(in_file, 'ID Code')

    return csv_dict

if __name__ == "__main__":

    # data files
    gov_id_file = 'data/government_ids.csv'

    # set up lookup tables
    gov_id_lookup = build_gov2id_lookup(gov_id_file)
