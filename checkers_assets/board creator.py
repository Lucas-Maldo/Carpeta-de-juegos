
from PIL import Image, ImageDraw

def create_checkers_board(board_size=8, square_size=100, wood_color=(139, 69, 19)):
    # Calculate the total image size
    image_size = board_size * square_size

    # Create a blank image with a wooden color background
    image = Image.new("RGB", (image_size, image_size), wood_color)
    draw = ImageDraw.Draw(image)

    # Draw alternating dark and light squares
    for row in range(board_size):
        for col in range(board_size):
            square_color = "dark" if (row + col) % 2 == 1 else "light"
            draw_square(draw, row, col, square_size, square_color)

    return image

def draw_square(draw, row, col, square_size, square_color):
    # Calculate the position of the square
    x = col * square_size
    y = row * square_size

    # Determine the color of the square a9 77 53
    color = (96, 60, 36) if square_color == "dark" else (238, 201, 143)  # Dark and light wooden colors
    #dark = (38, 26, 18)
    # Draw the square
    draw.rectangle([x, y, x + square_size, y + square_size], fill=color)

# Example usage:
board_image = create_checkers_board(board_size=8, square_size=100)

# Save the image
board_image.save("checkers_board.png", format="PNG")