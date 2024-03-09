from PIL import Image, ImageDraw, ImageFont

# Create a blank image
image_size = 300
image = Image.new("RGB", (image_size, image_size), (0, 0, 139))
draw = ImageDraw.Draw(image)

# Draw the Tic Tac Toe board
cell_size = image_size // 3
for i in range(1, 3):
    line_position = cell_size * i
    draw.line([(0, line_position), (image_size, line_position)], fill="white", width=2)
    draw.line([(line_position, 0), (line_position, image_size)], fill="white", width=2)

# Save the image
image.save("tic_tac_toe_board.png")

# Create a blank image
image = Image.new("RGBA", (image_size, image_size), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Load the BIPs font (replace "path/to/bips/font.ttf" with the actual path)
font_path = "C:\Windows\Fonts\BAUHS93.ttf"
font_size = 300
font = ImageFont.truetype(font_path, font_size)

# Draw the letter "X" in the BIPs font
text = "O"
# text = "X"
if(text == "X"):
    text_width, text_height = draw.textsize(text, font)
    text_position = ((image_size - text_width) // 2+9, (image_size - text_height-60) // 2)
    draw.text(text_position, text, font=font, fill=(0, 0, 0, 255))

if(text == "O"):
    text_width, text_height = draw.textsize(text, font)
    text_position = ((image_size - text_width) // 2+3, (image_size - text_height-60) // 2)
    draw.text(text_position, text, font=font, fill=(0, 0, 0, 255))


# Save the image
image.save("tic_tac_toe_images\O_tic_tac.png")
# image.save("tic_tac_toe_images\X_tic_tac.png")
