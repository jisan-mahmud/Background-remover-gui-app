from PIL import Image
from rembg import remove


def remove_image_background(input_path, output_path):
    img = Image.open(input_path)
    result = remove(img)
    result.save(output_path)
