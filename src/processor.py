from PIL import Image
from rembg import remove
from rembg.session_factory import new_session


def remove_image_background(input_path, output_path):
    # Load image
    img = Image.open(input_path).convert("RGBA")

    # Use the most accurate model available
    session = new_session("isnet-general-use")  # You can try "u2net_human_seg" for portraits

    # Remove background using selected session
    result = remove(img, session=session)

    # Save result with transparency
    result.save(output_path, format="PNG")
