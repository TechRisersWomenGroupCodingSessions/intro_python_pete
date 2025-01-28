import pytest
from  baker import cake

# STEP 1: write the production code to ensure the test passes. 
def test_returns_0_if_no_ingredients_available():
    available = {}
    recipe = {"flour": 400}
    max_cakes = cake(available, recipe)
    assert max_cakes == 0

# STEP 2: delete the @pytest.mark.skip decorator to use the test, then adjust the production code to make it pass.
# Then proceed to the next test.

@pytest.mark.skip
def test_returns_3_if_triple_of_recipe():
    available = {"apples": 3}
    recipe = {"apples" : 1}
    assert cake(available, recipe) == 3

@pytest.mark.skip
def test_returns_0_if_ingredient_missing():
    available = {"sugar": 500, "eggs": 4}
    recipe = {"flour": 600, "butter": 200, "eggs": 2}
    result = cake(available, recipe)
    assert result == 0

# STEP 3 : Now write your own tests for any missing scenarios, some ideas:
# - the function returns 0 if an ingredient is available in insufficient quantity
# - the return value should be rounded down to the nearest integer
# - the number of cakes is determined by the quantity of the least available ingredient   
