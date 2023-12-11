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


app = Flask(__name__)

def save_image(images, path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Folder '{path}' created.")
    
    images = images.numpy()
    for i, image in enumerate(images):
        im = Image.fromarray((image).astype(np.uint8))
        image_path = 'image_'+str(info.ip)+'_'+str(i)+'.png'
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

@app.route('/')
def page():
    info.ip=request.remote_addr
    return send_file('main3.html')

@app.route('/image/<ip>/<num>')
def download_image(ip,num):
    print(ip)
    print(num)
    image_path = '/home/tianyi/user/image_'+str(ip)+'_'+str(num)+'.png'
    print(image_path)
    return send_file(image_path, as_attachment=True)

@app.route('/getStatus', methods=['POST'])
def getStatus():
    return jsonify({'status':os.path.exists('/home/tianyi/user/image_'+str(info.ip)+'_'+'0.png')})

@app.route('/search', methods=['POST'])
def search():
    # 处理从前端发送的搜索内容
    start = time.time()
    search_query = request.get_json().get('query', '')
    
    # thread=threading.Thread(target=generatePic,args=(search_query,))
    # thread.start()
    p=Process(target=generatePic,args=([search_query]))
    # generatePic(search_query)
    p.start()
    print(1)
    # time.sleep(10)
    end = time.time()
    return jsonify({'ip':str(info.ip)})


if __name__ == '__main__':
    model = MinDalle(
    dtype=getattr(torch, dtype),
    device='cpu',
    is_mega=True, 
    is_reusable=True)
    app.run(host='0.0.0.0',port=5000, processes=True)#146.148.97.242