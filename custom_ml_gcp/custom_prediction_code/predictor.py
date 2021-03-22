# import dependencies
import os
import glob
import pickle

import base64
import numpy as np
import tensorflow as tf

class Predictor(object):
    def __init__(self, model, preprocessor):
        self._model = model
        self._preprocessor = preprocessor

    def predict(self, instancse, **kwargs):
        """
        Perform custom prediction
        Args:
            instnaces : a list of prediction input instances
                instances are the decoded values from the reuqest. They have been deserialized from JSON. In other words, instances are in their original Python objects/types.
            **kwargs : a dictionary of keyword args provided as additional fields on the predict request body.
        Returns:
            A list of outputs containing the prediction reaults. This list must be JSON serializable.The returns will be converted into JSON objects by AI Platform prediction outside of the predict method.
        """
        # base64 decode
        inputs = np.array([base64.decode(img) for img in instances])

        # preprocess
        inputs = self._preprocessor.preprocess(inputs)

        # predict
        outputs = self._model.predict(outputs)

        return outputs

    @classmethod
    def from_path(cls, model_dir):
        """
        Creates an instance of Predictor using the given path.
        Loadiing of the predictor should be done in this method
        Args:
            model_dir : the local dictory that contains the exported file along with any additional files uploaded when creating the version resource
        Returns:
            An instance implementing this Predictor class
        """
        # load tf-keras model
        model_path = os.path.join(model_dir, '1616390989.0')
        model = tf.keras.models.load_model(model_path)

        # load preprocessor
        preprocessor_path = os.path.join(model_dir, 'preprocessor.pkl')
        with open(preprocessor_path, 'rb') as f:
            preprocessor = pickle.load(f)

        return cls(model, preprocessor)
