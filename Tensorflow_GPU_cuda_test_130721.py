'''
#Created by: Jack Cornwall
#Email: hello@jackcornwall.co.uk
#Git hub: https://github.com/JackDCornwall
#Website:https://jackcornwall.co.uk/

#Project: Cuda/tensorflow GPU test
#Date: 13.07.21
#Description: Following this guide: https://towardsdatascience.com/installing-tensorflow-with-cuda-cudnn-and-gpu-support-on-windows-10-60693e46e781
Attempting to verify if Tensorflow can use the GPU in the machine.
'''
# importing required packages
import tensorflow as tf
import os

os.add_dll_directory("C://Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.4")
# added this line based on this page:https://github.com/tensorflow/tensorflow/issues/48868

print(tf.test.is_built_with_cuda()) #testing for cuda support

#testing if GPU is available
print(tf.test.is_gpu_available(cuda_only=False,min_cuda_compute_capability=None))