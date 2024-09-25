class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


import unittest


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.obj_1 = Runner("Усэйн", speed=10)
        self.obj_2 = Runner("Андрей", speed=9)
        self.obj_3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)

    def test_1(self):
        tournament = Tournament(90, self.obj_1, self.obj_3)
        result = tournament.start()
        self.all_results[1] = result
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")

    def test_2(self):
        tournament = Tournament(90, self.obj_2, self.obj_3)
        result = tournament.start()
        self.all_results[2] = result
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")

    def test_3(self):
        tournament = Tournament(90, self.obj_1, self.obj_2, self.obj_3)
        result = tournament.start()
        self.all_results[3] = result
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")


if __name__ == '__main__':
    unittest.main()


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

            if all(p.distance >= self.full_distance for p in self.participants):
                break

        return {place: runner.name for place, runner in finishers.items()}
