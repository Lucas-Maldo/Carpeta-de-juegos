from PIL import Image, ImageDraw

def create_checkers_piece(piece_color, piece_size=95, num_layers=3):
    # Create a blank image with a transparent background
    image = Image.new("RGBA", (piece_size, piece_size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Draw multiple circles as layers to create a radial gradient effect
    for layer in range(num_layers):
        layer_radius = piece_size // 2 - (layer * layer*6)  # Adjust the offset for each layer

        # Calculate the position of the layer
        layer_position = (piece_size // 2 - layer_radius, piece_size // 2 - layer_radius)
        layer_opacity = int(256 - (layer * (10 / num_layers)))

        # Calculate the gradient color toward the center
        gradient_color = (
            int(piece_color[0] * (1 - layer / 10)),
            int(piece_color[1] * (1 - layer / 10)),
            int(piece_color[2] * (1 - layer / 10)),
            layer_opacity
        )

        # Draw the circle for the layer with the gradient color
        draw.ellipse([(layer_position[0], layer_position[1]),
                      (layer_position[0] + layer_radius * 2, layer_position[1] + layer_radius * 2)],
                     fill=gradient_color)

    return image

def create_checkers_king(king_color, piece_size=95, num_layers=3):
    # Create a blank image with a transparent background
    image = Image.new("RGBA", (piece_size, piece_size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Draw multiple circles as layers to create a 3D effect for the kings
    for layer in range(num_layers):
        layer_radius = piece_size // 2 - (layer * layer*6)  # Adjust the offset for each layer

        # Calculate the position of the layer
        layer_position = (piece_size // 2 - layer_radius, piece_size // 2 - layer_radius)
        layer_opacity = int(256 - (layer * (10 / num_layers)))  # Vary transparency (more opaque than regular pieces)

        gradient_color = (
            int(king_color[0] * (1 - layer / 3)),
            int(king_color[1] * (1 - layer / 3)),
            int(king_color[2] * (1 - layer / 3)),
            layer_opacity
        )

        # Draw the circle for the layer
        draw.ellipse([(layer_position[0], layer_position[1]),
                      (layer_position[0] + layer_radius * 2, layer_position[1] + layer_radius * 2)],
                     fill=gradient_color)

    return image

def add_crown(piece):
    crown = Image.open("Carpeta-de-juegos/checkers_assets/crown.png")
    crown = crown.resize((67, 67))
    crown = crown.convert("RGBA")  # Including the "A" in RGB
    
    piece.paste(crown, (14, 9), crown)
    return piece


# Example usage with the specified RGB values:
black_piece = create_checkers_piece((60, 40, 20, 255))
white_piece = create_checkers_piece((199, 137, 63, 255))

black_king = add_crown(create_checkers_king((60, 40, 20, 255)))
white_king = add_crown(create_checkers_king((199, 137, 63, 255)))

# Save the images
black_piece.save("Carpeta-de-juegos/checkers_assets/black_checkers_piece.png", format="PNG")
white_piece.save("Carpeta-de-juegos/checkers_assets/white_checkers_piece.png", format="PNG")
black_king.save("Carpeta-de-juegos/checkers_assets/black_checkers_king.png", format="PNG")
white_king.save("Carpeta-de-juegos/checkers_assets/white_checkers_king.png", format="PNG")
