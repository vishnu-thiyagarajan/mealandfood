from solution import get_matching_meals
import unittest
meal_data = [
    {
        'meal_id': 1,
        'foods': [
            {
                'food_id': 1,
                'food_name': 'Idli'
            },
            {
                'food_id': 10,
                'food_name': 'Sambar'
            },
        ]
    },
    {
        'meal_id': 2,
        'foods': [
            {
                'food_id': 1,
                'food_name': 'Idli'
            },
            {
                'food_id': 11,
                'food_name': 'Chutney'
            },
        ]
    },
    {
        'meal_id': 3,
        'foods': [
            {
                'food_id': 1,
                'food_name': 'Idli'
            },
            {
                'food_id': 10,
                'food_name': 'Sambar'
            },
            {
                'food_id': 11,
                'food_name': 'Chutney'
            },
        ]
    },
    {
        'meal_id': 4,
        'foods': [
            {
                'food_id': 2,
                'food_name': 'Dosa'
            },
            {
                'food_id': 10,
                'food_name': 'Sambar'
            },
        ]
    },
]
class SimpleTest(unittest.TestCase):

    def test(self):
        self.assertEqual(get_matching_meals(meal_data=meal_data, food_ids=[1]),[1,2,3])
        self.assertEqual(get_matching_meals(meal_data=meal_data, food_ids=[11]),[2,3])
        self.assertEqual(get_matching_meals(meal_data=meal_data, food_ids=[1,10]),[1,3]) 

if __name__ == '__main__': 
    unittest.main() 
