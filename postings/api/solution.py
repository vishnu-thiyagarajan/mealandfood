def common_elements(food_ids, food_ids_of_meals):
    for elem in food_ids: 
        if elem not in food_ids_of_meals: 
            return False
    return True

def get_matching_meals(meal_data, food_ids):
    """Returns all the meal IDs in meal_data that have all of the given food IDs.

    Args:
        meal_data: list of dictionary of meals (check sample_mealdata.py for sample)
        food_ids: list of food IDs.
    
    Returns:
        list of int: The matching meal IDs

    """
    # Implement this method.
    meal_ids = []
    for item in meal_data:
        food_ids_of_meals = list((dct.get('food_id') for dct in item['foods']))
        if common_elements(food_ids, food_ids_of_meals):
            meal_ids.append(item['meal_id'])
    return meal_ids