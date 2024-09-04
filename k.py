def calculate_final_speed(initial_speed, degrees):
    """
    Calculates the final speed of a character traversing a terrain
    with varying inclines.

    Args:
        initial_speed: The starting speed of the character.
        degrees: An array of integers representing the angles of inclination
        of each piece of land.

    Returns:
        The final speed of the character after traversing the terrain.
    """

    final_speed = initial_speed
    for degree in degrees:
        # Speed change proportional to the incline.
        speed_change = degree / 2  # Adjusted proportionality
        final_speed += speed_change

        # Speed cannot go below 0.
        if final_speed <= 0:
            final_speed = 0
            return final_speed

    return final_speed

# Example usage
initial_speed = 60
degrees = [30, -30, 45]
final_speed = calculate_final_speed(initial_speed, degrees)
print(f"Final speed: {final_speed}")
