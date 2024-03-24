import Phase1, Phase2, Phase3
from PIL import Image

image = Image.open("practice_images/road_work.png").convert("RGB")

# print(Phase1.is_street_sign(image))

if Phase1.is_street_sign(image):
    raw_text = Phase2.image_to_json(image)
    clean_text = Phase2.json_to_string(raw_text)

    Phase3.string_to_wav(clean_text)
