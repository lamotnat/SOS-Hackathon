import software_side.Phase1, software_side.Phase2, software_side.Phase3
import hardware_side.Phase0
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

filepath = hardware_side.Phase0.retrieve_image()

image = Image.open(filepath).convert("RGB")

if software_side.Phase1.is_street_sign(image):
    raw_text = software_side.Phase2.image_to_json(image)
    clean_text = software_side.Phase2.json_to_string(raw_text)

    software_side.Phase3.string_to_wav(clean_text)
    software_side.Phase3.play_wav()
