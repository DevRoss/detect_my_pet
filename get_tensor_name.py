import tensorflow as tf
import os
from tensorflow.python.platform import gfile

GRAPH_PATH = 'training'
GRAPH_FILE = 'frozen_inference_graph.pb'
with tf.Session() as sess:
    with gfile.GFile(os.path.join(GRAPH_PATH, GRAPH_FILE), 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        g_in = tf.import_graph_def(graph_def)
    for tensor in g_in:
        print(tensor.name)
    # print(sess.graph)
