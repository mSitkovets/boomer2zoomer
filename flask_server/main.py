import os
# for using a tensorflow model
import tensorflow as tf
import numpy as np
from tensorflow.keras import datasets, layers, models

# setting up a flask web server
from flask import (Flask, request, jsonify)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# setup the model to serve predict sound REST/AJAX request
speech_recognition = tf.saved_model.load("../model_1")

fftsize = 512 # size of a Short time fourier transform (STFT) window
windowsize = 256 # size of/distance between each window

# function for processing a voice clip using fft and the model
def process_audio(clip):
    # convert to np array
    data = np.array(clip)
    # array to store the transformed data
    fft_res = []
    # if the clip is stereo, take only the first channel
    if len(data.shape) >= 2:
        data = data[:, 0]
    # get the number of samples
    numsamples = data.shape[0]
    if numsamples > 32000: # if clip longer than 2 seconds
        data = data[:32000] # cut it off at 2 seconds
    elif numsamples < 32000: # if too short
        data = np.concatenate((data, np.zeros(32000 - numsamples))) # pad silence until 2 seconds

    # re-define numsamples to 32000
    numsamples = 32000
    # for each period of <fftsize> samples
    while index_ct < numsamples - fftsize:
        # grab <fftsize> samples from the current part of the file
        elems = data[index_ct:index_ct+fftsize]
        # perform the fft
        res = np.fft.fft(elems)
        res = np.abs(res) # only take the magnitude of the sequence
        # add it to temp array
        fft_res.append(res)
        # to the next section
        index_ct += windowsize
    # turn it into a single 2D tensor
    fft_res = np.array(fft_res)
    # normalize all elements into a real number between 0 and 1 (essentially normalizing volume)
    if np.amax(fft_res) != 0:
        fft_res = fft_res / np.amax(fft_res)

    # reshape the tensor with an extra dimension as 'color channel' so it will fit into the CNN
    shap = fft_res.shape
    fft_res.reshape((shap[0], shap[1], 1))
    # predict using neural network
    result = speech_recognition(fft_res)

    return result

@app.route('/word-detect')
def serve_word_detect():
    # get the audio clip as a numeric/float array inside the data of the POST request
    audio_signal = request.form.get("audio")
    # predict using the neural network
    result = process_audio(audio_signal)
    # return the result
    return jsonify(result=result)
