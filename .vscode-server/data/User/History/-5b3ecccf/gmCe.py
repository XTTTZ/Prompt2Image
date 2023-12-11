dtype = "float32" #@param ["float32", "float16", "bfloat16"]
import torch
from min_dalle import MinDalle
from PIL import Image
import numpy as np
import time, sys

def generate_image(model, text, temperature = 1, top_k = 256, supercondition_factor=16, grid_size=4, seamless=False):
    images = model.generate_images(
        text=text,
        seed=-1,
        grid_size=grid_size,
        is_seamless=seamless,
        temperature=temperature,
        top_k=top_k,
        supercondition_factor=supercondition_factor,
        is_verbose=False
    )
    return images

if __name__ == "__main__":
    start = time.time()
    ini = time.time()
    text = sys.argv[1]
    print("Text: ", text)
    model = MinDalle(
    dtype=getattr(torch, dtype),
    device='cuda',
    is_mega=True, 
    is_reusable=True)
    ini1 = time.time()
    print("Time taken for model init: ", ini1-ini)
    # model.save_model('dalle.pt')
    # torch.save(model.state_dict(), 'dalle.pth')
    
    images = generate_image(model, text)
    images = images.to('cpu').numpy()
    for i, image in enumerate(images):
        im = Image.fromarray((image).astype(np.uint8))
        im.save('image_{}.png'.format(i))
    end = time.time()
    print("Time taken: ", end-start)
    

