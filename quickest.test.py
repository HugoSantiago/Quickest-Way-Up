import quickest
import unittest

class TestQuickest(unittest.TestCase):

    ladders_set = []
    snakes_set = []
    correct_answers = [3,3,17,3,3,17,3,3,17]

    def cargar_escenarios_exitosos(self):
        fptr = open('test_files/myTest.txt', 'r')

        t = int(fptr.readline().strip())
    
        for t_itr in range(t):
            n = int(fptr.readline().strip())

            ladders = []

            for _ in range(n):
                ladders.append(list(map(int, fptr.readline().rstrip().split())))

            TestQuickest.ladders_set.append(ladders)
            m = int(fptr.readline().strip())

            snakes = []

            for _ in range(m):
                snakes.append(list(map(int, fptr.readline().rstrip().split())))

            TestQuickest.snakes_set.append(snakes)

        fptr.close()
    
    def test_quickest_correct(self):
        TestQuickest.cargar_escenarios_exitosos(self)
        for i in range(len(TestQuickest.snakes_set)):
            self.assertEqual(quickest.quickestWayUp(TestQuickest.ladders_set[i], TestQuickest.snakes_set[i]),TestQuickest.correct_answers[i])
    


if __name__ == '__main__':
    unittest.main()