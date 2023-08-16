import pytest
from unittest.mock import MagicMock
from src.controllers.recipecontroller import RecipeController
# add your test case implementation here
@pytest.fixture
def recipe_controller():
    mock_dao = MagicMock()
    return RecipeController(items_dao=mock_dao)

@pytest.mark.unit
def test(recipe_controller):
    mock_items = [
        {"name": "item1", "quantity": 5},
        {"name": "item2", "quantity": 10}
    ]
    recipe_controller.get_all = MagicMock(return_value=mock_items)
    result = recipe_controller.get_available_items(minimum_quantity=8)
    expected_result = {"item2": 10}
    assert result == expected_result

@pytest.mark.unit
def test_returned_null(recipe_controller):
    mock_items = None
    recipe_controller.get_all = MagicMock(return_value=mock_items)
    with pytest.raises(TypeError):
        result = recipe_controller.get_available_items(minimum_quantity=8)


@pytest.mark.unit
def test_empty_list(recipe_controller):
    mock_items = []
    recipe_controller.get_all = MagicMock(return_value=mock_items)
    result = recipe_controller.get_available_items(minimum_quantity=8)
    expected_result = {}
    assert result == expected_result

@pytest.mark.unit
def test_one_item(recipe_controller):
    mock_items = [{"name": "item1", "quantity": 5}]
    recipe_controller.get_all = MagicMock(return_value=mock_items)
    result = recipe_controller.get_available_items(minimum_quantity=0)
    assert len(result) == 1

@pytest.mark.unit
@pytest.mark.parametrize("quantity,exected_result", [(4, 0), (5, 1), (6, 1)])
def test_boudary(recipe_controller, quantity, exected_result):
    mock_items = [{"name": "item1", "quantity": quantity}]
    recipe_controller.get_all = MagicMock(return_value=mock_items)
    result = recipe_controller.get_available_items(minimum_quantity=5)
    assert len(result) == exected_result