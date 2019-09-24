import unittest
from utils import *

class TestUtils(unittest.TestCase):

    def test_structure_string(self):
        t1 = '[font face="Times-Bold" size="12.106"]t).  (15). [/font][font face="Times-BoldItalic" size="11.960"]n [/font][font face="Times-Bold" size="12.106"]Rekurs der Regierung  des  Kantons  Luzern.  [/font][font face="Times-Roman" size="10.602"]Bericht des  Bundesrates vom  [/font][font face="Times-Bold" size="12.106"]27.  [/font][font face="Times-Roman" size="10.602"]November [/font][font face="Times-Bold" size="12.106"]1908  [/font][font face="Times-Roman" size="10.602"](Bundesblatt  VI,  [/font]'

        structured_t1 = structure_text_sting(t1)
        t1_true = [{'font': 'Times-Bold', 'size': 12.106, 'text': 't).  (15). ', 'l_text': 11},
         {'font': 'Times-BoldItalic', 'size': 11.96, 'text': 'n ', 'l_text': 2},
         {'font': 'Times-Bold', 'size': 12.106, 'text': 'Rekurs der Regierung  des  Kantons  Luzern.  ', 'l_text': 45},
         {'font': 'Times-Roman', 'size': 10.602, 'text': 'Bericht des  Bundesrates vom  ', 'l_text': 30},
         {'font': 'Times-Bold', 'size': 12.106, 'text': '27.  ', 'l_text': 5},
         {'font': 'Times-Roman', 'size': 10.602, 'text': 'November ', 'l_text': 9},
         {'font': 'Times-Bold', 'size': 12.106, 'text': '1908  ', 'l_text': 6},
         {'font': 'Times-Roman', 'size': 10.602, 'text': '(Bundesblatt  VI,  ', 'l_text': 19}]

        self.assertEqual(t1_true, structured_t1)

        t2 = '[font face="Times-Bold" size="12.106"]27.  [/font][font face="Times-Roman" size="10.044"](47). [/font][font face="Times-BoldItalic" size="11.959"]n [/font][font face="Times-Bold" size="12.106"]Postulat  Winiger,  betreffend  Gotthardbahr.  [/font][font face="Times-Roman" size="10.044"]Bericht  des  Bundesrates  vom  14.  Dezember  1908  (B.B.  VI,  397)  [/font]'

        structured_t2 = structure_text_sting(t2)
        t2_true = [{'font': 'Times-Bold', 'size': 12.106, 'text': '27.  ', 'l_text': 5},
                   {'font': 'Times-Roman', 'size': 10.044, 'text': '(47). ', 'l_text': 6},
                   {'font': 'Times-BoldItalic', 'size': 11.959, 'text': 'n ', 'l_text': 2},
                   {'font': 'Times-Bold', 'size': 12.106, 'text': 'Postulat  Winiger,  betreffend  Gotthardbahr.  ', 'l_text': 47},
                   {'font': 'Times-Roman', 'size': 10.044, 'text': 'Bericht  des  Bundesrates  vom  14.  Dezember  1908  (B.B.  VI,  397)  ', 'l_text': 71}]

        self.assertEqual(t2_true, structured_t2)