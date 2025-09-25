"""
Lumache - A fictional Python library
"""

__version__ = "0.1.0"

class RecipeNotFoundError(Exception):
    """Custom exception when recipe is not found."""
    pass

def get_random_recipe(kind=None):
    """Return a random recipe.
    
    :param kind: Optional type of recipe.
    :return: A list of ingredients.
    :raises RecipeNotFoundError: If no recipe is found.
    """
    return ["spam", "eggs", "bacon"]