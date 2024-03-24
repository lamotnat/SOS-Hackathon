Our project is a system for blind or hearing impaired individuals to be able
to navigate spaces that lack braille or other assistive technologies present.
To allow this, we built a system that waits for a photo from a connected 
camera then runs it through three phases - each with their own AI model  - to
classify the image, read from the image, and speak aloud the contents for the
user. The camera and speaker/earpiece can be swapped for any system. 

Future iterations of this project could better train or integrate the AI 
models, build a physical wearable device, or any number of user-focused
additions.

Our implementation waited for an image captured on an Arduino ArduCAM OV_2640 
Mini-2MP-Plus. We used ArduCAM_Host_V2 for our image capturing; however, the 
directory being looked at can be changed and the image itself can come from 
any source. Please ensure that the folder is empty as the program waits for 
an image to be saved into the folder. To change the directory, look in
./hardware_side/Phase0.py and replace `"<SPECIFY FILE PATH>"`.

For our AI models, we used these three:
- https://huggingface.co/google/vit-base-patch16-224 
  for Phase 1 image recognition
- https://huggingface.co/jinhybr/OCR-Donut-CORD 
  for Phase 2 text retrieval
- https://huggingface.co/microsoft/speecht5_tts
  for Phase 3 text-to-speech

