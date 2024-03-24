import Phase1, Phase2, Phase3
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

image = Image.open("practice_images/i_sure_hope_it_does.jpg").convert("RGB")

# print(Phase1.is_street_sign(image))

if Phase1.is_street_sign(image):
    raw_text = Phase2.image_to_json(image)
    clean_text = Phase2.json_to_string(raw_text)

    print(raw_text)
    print(clean_text)

    Phase3.string_to_wav(clean_text)
    Phase3.play_wav()
