from transformers import pipeline
import torch
import re
from transformers import TrOCRProcessor, VisionEncoderDecoderModel, DonutProcessor
from PIL import Image
from datasets import load_dataset


def image_to_json(image: Image) -> str:
    #setup system
    processor = DonutProcessor.from_pretrained("jinhybr/OCR-Donut-CORD")
    model = VisionEncoderDecoderModel.from_pretrained("jinhybr/OCR-Donut-CORD")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    # prepare decoder inputs
    task_prompt = "<s_rvlcdip>"
    decoder_input_ids = processor.tokenizer(
        task_prompt, add_special_tokens=False, return_tensors="pt"
    ).input_ids

    pixel_values = processor(image, return_tensors="pt").pixel_values

    #run the model
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

    #clean output some
    sequence = processor.batch_decode(outputs.sequences)[0]
    sequence = sequence.replace(processor.tokenizer.eos_token, "").replace(
        processor.tokenizer.pad_token, ""
    )
    
    return sequence


def json_to_string(s):

    words = []

    while len(s) > 1:
        start = s.index(">")
        if start + 1 >= len(s):
            break
        s = s[start + 1 :]
        end = s.index("<")

        word = s[:end]
        s = s[end:]

        if word == "" or word == " " or len(word) > 50:
            continue

        if word in words:
            break

        words.append(word)

    s = ""
    for word in words:
        s = s + word

    return s
