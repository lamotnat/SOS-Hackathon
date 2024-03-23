from transformers import pipeline
import torch
import re
from transformers import TrOCRProcessor, VisionEncoderDecoderModel, DonutProcessor
from PIL import Image
from datasets import load_dataset


def ms_system():
    # load image from the IAM database (actually this model is meant to be used on printed text)
    # url = 'https://fki.tic.heia-fr.ch/static/img/a01-122-02-00.jpg'
    # image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
    image = Image.open("road_work_cropped.png").convert("RGB")

    # processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-printed')
    # model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-printed')
    processor = TrOCRProcessor.from_pretrained("microsoft/trocr-large-str")
    model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-large-str")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pixel_values = processor(images=image, return_tensors="pt").pixel_values

    generated_ids = model.generate(
        pixel_values.to(device),
        max_length=model.decoder.config.max_position_embeddings,
        pad_token_id=processor.tokenizer.pad_token_id,
        eos_token_id=processor.tokenizer.eos_token_id,
        use_cache=True,
        bad_words_ids=[[processor.tokenizer.unk_token_id]],
        return_dict_in_generate=True,
    )
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    print("Text:", generated_text)


def image_to_json():
    processor = DonutProcessor.from_pretrained("jinhybr/OCR-Donut-CORD")
    model = VisionEncoderDecoderModel.from_pretrained("jinhybr/OCR-Donut-CORD")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    # load document image
    # dataset = load_dataset("D:/vscoderepos/make2024/SOS-Hackathon/software_side/imagefolder", split="test")
    # image = dataset[1]["image"]
    image = Image.open("txt.jpg").convert("RGB")

    # prepare decoder inputs
    task_prompt = "<s_rvlcdip>"
    decoder_input_ids = processor.tokenizer(
        task_prompt, add_special_tokens=False, return_tensors="pt"
    ).input_ids

    pixel_values = processor(image, return_tensors="pt").pixel_values

    outputs = model.generate(
        pixel_values.to(device),
        decoder_input_ids=decoder_input_ids.to(device),
        max_length=model.decoder.config.max_position_embeddings,
        pad_token_id=processor.tokenizer.pad_token_id,
        eos_token_id=processor.tokenizer.eos_token_id,
        use_cache=True,
        bad_words_ids=[[processor.tokenizer.unk_token_id]],
        return_dict_in_generate=True,
    )

    sequence = processor.batch_decode(outputs.sequences)[0]
    sequence = sequence.replace(processor.tokenizer.eos_token, "").replace(
        processor.tokenizer.pad_token, ""
    )
    print(sequence)
    # sequence = re.sub(
    #     r"<.*?>", "", sequence, count=1
    # ).strip()  # remove first task start token
    # print(processor.token2json(sequence))
