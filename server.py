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

class info:
    ip=''
info=info()

@app.route('/')
def page():
    info.ip=request.remote_addr
    return send_file('main4.html')

@app.route('/ip')
def returnip():
    return jsonify({'ip_addr':info.ip})

@app.route('/image/<ip>/<num>')
def download_image(ip,num):
    image_path = '/home/tianyi/user/'+str(ip)+'_'+str(num)+'.png'
    return send_file(image_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, threaded=False, processes=False)#34.72.227.197