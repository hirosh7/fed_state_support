from unittest import TestCase
import gen_stats


class TestGenStats(TestCase):

    def test_build_lookup(self):
        lu_tab = gen_stats.build_lookup('../data/government_ids.csv', 'ID Code')
        self.assertEqual(lu_tab['06000000000000']['State'].strip(), 'Colorado')

    def test_row2dictitem(self):
        row = '0600000000000019U      757843061131324'
        row_items = gen_stats._row2dictitem(row)
        self.assertEqual(row_items['ID'], '06000000000000')
        self.assertEqual(row_items['Item Code'], '19U')
        self.assertEqual(row_items['Amount'], 757843061)
        self.assertEqual(row_items['Survey Year'], '13')
        self.assertEqual(row_items['Year of Data'], '13')
        self.assertEqual(row_items['Origin'], '24')

    def test_process_state_data(self):

        # data files
        gov_id_file = '../data/government_ids.csv'
        gov_itemcode_file = '../data/itemcodes.csv'
        state_data_file = '../data/13state35.txt'

        # set up lookup tables
        gov_id_lookup = gen_stats.build_lookup(gov_id_file, 'ID Code')
        gov_itemcode_lookup = gen_stats.build_lookup(gov_itemcode_file, 'Item Code')

        # get state data
        state_data = gen_stats.process_state_data(state_data_file, gov_id_lookup, gov_itemcode_lookup)
        self.assertEqual(state_data[12000]['State'], 'Washington')
        self.assertEqual(state_data[12000]['Item'], 'Construction - Fish & Game')
        self.assertEqual(state_data[10]['State'], 'No State')
