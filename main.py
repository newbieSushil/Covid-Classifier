# imports for UI
from flask import *  
from IPython.display import display, Image
from PIL import Image
import os

# ML imports

import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.layers import *
from keras.models import * 
from keras.preprocessing import image
import cv2
import glob
from IPython.display import display, Image

from keras.models import load_model
model = load_model("model1.h5")


def solve(var):
	#img = image.load_img("./testImages/" + "1-s2.0-S1684118220300608-main.pdf-002.jpg", target_size = (224,224))
	#img = image.load_img("C:/Users/sushi/Downloads/1.jpeg", target_size = (224,224))

	img = image.load_img(var, target_size = (224,224))
	img = image.img_to_array(img)
	img = np.expand_dims(img,axis = 0)
	p = model.predict_classes(img)
	
	if p == [[0]]:
		return True
	else:
		return False
###########################################################
###########################################################

app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("upload.html")  
 
@app.route('/result', methods = ['POST'])  
def result():  
    if request.method == 'POST':  
        f = request.files['img'] 
        var=os.path.join(app.root_path, 'static/' + f.filename)
        f.save(var)      


        flag = solve(var)
        message = "Positive"
        if flag == False:
        	message = "Negative"

        image_path = f.filename

        return render_template("result.html",diagnosis  = message, path_to_image = image_path)

#############################################################
#############################################################

app.run(debug = True)