dtype = "float32" #@param ["float32", "float16", "bfloat16"]
from flask import Flask, request, jsonify, send_file
from dalle_mini import generate_image
import torch
from min_dalle import MinDalle
from PIL import Image
import numpy as np
import time, sys
import os
from multiprocessing import Process
import threading
import asyncio
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, supports_credentials=True)

def save_image(images, path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Folder '{path}' created.")
    
    images = images.numpy()
    for i, image in enumerate(images):
        im = Image.fromarray((image).astype(np.uint8))
        image_path = str(info.ip)+'_'+str(i)+'.png'
        new_image_path = os.path.join(path, os.path.basename(image_path))
        im.save(new_image_path)

def generatePic(search_query):
    print(search_query)
    images = model.generate_images(
        text=search_query,
        seed=-1,
        grid_size=1,
        is_seamless=False,
        temperature=1,
        top_k=256,
        supercondition_factor=16,
        is_verbose=False
    )
    save_image(images,'/home/tianyi/user/')

def test():
    time.sleep(10)

class info:
    ip=''
info=info()

@app.route('/search', methods=['POST','OPTIONS'])
def search():
    info.ip=request.remote_addr
    search_query = request.form['text']
    generatePic(search_query)
    print(1)
    return jsonify({'imageName':str(info.ip+'_0.png')})


if __name__ == '__main__':
    # model = MinDalle(
    # dtype=getattr(torch, dtype),
    # device='cpu',
    # is_mega=True, 
    # is_reusable=True)
    app.run(host='0.0.0.0',port=5000,threaded=False,processes=False)
    CORS(app, supports_credentials=True)