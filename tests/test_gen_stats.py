from unittest import TestCase
import gen_stats

class TestGen_Stats(TestCase):

    def test_build_gov2id_lookup(self):
        lu_tab = gen_stats.build_gov2id_lookup('../data/government_ids.csv')
        self.assertEqual(lu_tab['06000000000000']['State'].strip(), 'Colorado')
