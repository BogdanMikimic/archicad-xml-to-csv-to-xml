from main import count_t, compare_number_of_t_and_indicate_direction, check_item_is_closing_tag

from unittest import TestCase



class TestingAllFunctions(TestCase):

    def test_count_of_t(self):
        with open('test.xml', 'r') as txt:
            line_count = 0
            for line in txt:
                if line_count == 0:
                    self.assertEqual(count_t(line), 0, "Line contains more than 0 \\t characters")
                elif line_count == 1:
                    self.assertEqual(count_t(line), 0, "Line contains more than 0 \\t characters")
                elif line_count == 2:
                    self.assertEqual(count_t(line), 1, "Line does not contain 1 \\t characters")
                elif line_count == 3:
                    self.assertEqual(count_t(line), 1, "Line does not contain 1 \\t characters")
                elif line_count == 4:
                    self.assertEqual(count_t(line), 2, "Line does not contain 2 \\t characters")
                elif line_count == 5:
                    self.assertEqual(count_t(line), 2, "Line does not contain 2 \\t characters")
                elif line_count == 6:
                    self.assertEqual(count_t(line), 3, "Line does not contain 3 \\t characters")
                line_count += 1

    def test_direction_indicator(self):
        self.assertEqual(compare_number_of_t_and_indicate_direction(1, 2, '<abc>'), 'child')
        self.assertEqual(compare_number_of_t_and_indicate_direction(2, 2, '\t\t<sas>'), 'sibling')
        self.assertEqual(compare_number_of_t_and_indicate_direction(2, 2, '<sdasdas>'), 'sibling')
        self.assertEqual(compare_number_of_t_and_indicate_direction(2, 2, '</sas>'), 'closing tag')
        self.assertEqual(compare_number_of_t_and_indicate_direction(2, 1, '\t\t<fdsf>'), 'parent')

    def test_check_item_is_closing_tag(self):
        self.assertTrue(check_item_is_closing_tag('</jlkhlkajshfd flhdsjalh>'))
        self.assertTrue(check_item_is_closing_tag(' </fjhflashfd'))
        self.assertTrue(check_item_is_closing_tag('   \n </fjhflashfd\n'))
        self.assertTrue(check_item_is_closing_tag('   \t\t</fjhflashfd\n'))
        self.assertFalse(check_item_is_closing_tag('<fjhflashfd\n'))