from falcon import testing

from application.startup import api


class BaseTestCase(testing.TestCase):
    def setUp(self):
        super().setUp()
        self.app = api


class TestIdentifier(BaseTestCase):
    url = '/v1/identifier'

    def test_success(self):
        result = self.simulate_get(
            self.url,
            params={
                'game': 'Holdem',
                'board': ['Ac', 'Kc', 'Jc', '2s', '2d'],
                'pocket': ['Qc', 'Tc'],
            },
            params_csv=False,
        )
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json['high']['hand'], 'StraightFlush')

    def test_wrong_game(self):
        result = self.simulate_get(
            self.url,
            params={
                'game': 'WrongPoker',
                'board': ['Ac', 'Kc', 'Jc', '2s', '2d'],
                'pocket': ['Qc', 'Tc'],
            },
            params_csv=False,
        )
        self.assertEqual(result.status_code, 400)

    def test_long_pocket(self):
        result = self.simulate_get(
            self.url,
            params={
                'game': 'Holdem',
                'board': ['Ac', 'Kc', 'Jc', '2s', '2d'],
                'pocket': ['Qc', 'Tc', '7s', '8s'],
            },
            params_csv=False,
        )
        self.assertEqual(result.status_code, 400)

    def test_short_pocket(self):
        result = self.simulate_get(
            self.url,
            params={
                'game': 'Holdem',
                'board': ['Ac', 'Kc', 'Jc', '2s', '2d'],
                'pocket': ['Qc'],
            },
            params_csv=False,
        )
        self.assertEqual(result.status_code, 400)

    def test_long_board(self):
        result = self.simulate_get(
            self.url,
            params={
                'game': 'Holdem',
                'board': ['Ac', 'Kc', 'Jc', '2s', '2d', '7s'],
                'pocket': ['Qc', 'Tc'],
            },
            params_csv=False,
        )
        self.assertEqual(result.status_code, 400)

    def test_short_board(self):
        result = self.simulate_get(
            self.url,
            params={
                'game': 'Holdem',
                'board': ['Ac', 'Kc'],
                'pocket': ['Qc', 'Tc'],
            },
            params_csv=False,
        )
        self.assertEqual(result.status_code, 400)
