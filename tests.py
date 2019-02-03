import unittest
import powerAttackOrNot

class TestStringMethods(unittest.TestCase):
    def test_touching_chance(self):
        self.assertEqual(powerAttackOrNot.touching_chance(10, 20), 11/20)
        self.assertEqual(powerAttackOrNot.touching_chance(1, 40), 1/20)
        self.assertEqual(powerAttackOrNot.touching_chance(40, 1), 19/20)

    def test_chance_of_n_hits(self):
        touching_chances = [powerAttackOrNot.touching_chance(10, 20)]*5
        actual = powerAttackOrNot.chance_of_n_hits(touching_chances, 20)[0]
        self.assertAlmostEqual(sum(actual), 1)
        expected = [0.01845281249999999, 0.11276718749999996, 0.27565312499999994, 0.3369093750000001, 0.20588906250000008, 0.050328437500000024]
        for i, j in zip(actual, expected):
            self.assertAlmostEqual(i, j)

    def test_chance_to_be_nth_success(self):
        touching_chances = [powerAttackOrNot.touching_chance(10, 20)]*5
        actual = powerAttackOrNot.chance_of_n_hits(touching_chances, 20)[1]
        for i in range(len(actual)):
            proba_of_miss = (1-touching_chances[i])
            self.assertAlmostEqual(sum(actual[i])+proba_of_miss, 1)

unittest.main()
