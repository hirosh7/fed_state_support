from unittest import TestCase
import gen_stats


class TestGen_Stats(TestCase):

    def test_build_gov2id_lookup(self):
        lu_tab = gen_stats.build_lookup('../data/government_ids.csv', 'ID Code')
        self.assertEqual(lu_tab['06000000000000']['State'].strip(), 'Colorado')

    def test_row2dictitem(self):
        row = '0000000000000019U      757843061131324'
        row_items = gen_stats._row2dictitem(row)
        self.assertEqual(row_items['ID'], '00000000000000')
        self.assertEqual(row_items['Item Code'], '19U')
        self.assertEqual(row_items['Amount'], '757843061')
        self.assertEqual(row_items['Survey Year'], '13')
        self.assertEqual(row_items['Year of Data'], '13')
        self.assertEqual(row_items['Origin'], '24')



