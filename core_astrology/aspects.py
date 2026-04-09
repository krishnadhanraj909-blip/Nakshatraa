# aspects.py

def calculate_aspect(planet1, planet2):
    """
    Calculate the aspect between two planets based on their positions.
    
    Parameters:
    planet1 (float): Position of the first planet.
    planet2 (float): Position of the second planet.

    Returns:
    str: The type of aspect ('conjunction', 'opposition', 'trine', etc.).
    """
    # Placeholder for real calculation logic
    aspect_angle = abs(planet1 - planet2) % 360

    if aspect_angle == 0:
        return 'conjunction'
    elif aspect_angle == 180:
        return 'opposition'
    elif aspect_angle in [120, 240]:
        return 'trine'
    elif aspect_angle in [60, 300]:
        return 'sextile'
    else:
        return 'no significant aspect'

def interpret_aspect(aspect):
    """
    Interpret the meaning of a particular planetary aspect.
    
    Parameters:
    aspect (str): The aspect to be interpreted.

    Returns:
    str: Interpretation of the aspect.
    """
    interpretations = {
        'conjunction': "A powerful blend of energies; can signify strong potential.",
        'opposition': "Conflict or tension requiring balance between the two energies.",
        'trine': "Harmonious support, often signifying ease and flow.",
        'sextile': "Opportunities and growth; favorable interactions.",
        'no significant aspect': "Little to no direct influence."
    }
    return interpretations.get(aspect, "Unknown aspect")
