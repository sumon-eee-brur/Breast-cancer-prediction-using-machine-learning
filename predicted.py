import tensorflow as tf
import numpy as np
from sklearn.preprocessing import StandardScaler

model_path = r"G:\python\code\basic code\project with tkinter\assets\model.h5"

try:
    import h5py
    model = tf.keras.models.load_model(model_path)
    print(model.summary())
except Exception as e:
    print(f"Error loading model: {e}")


class PredictedClass:
    def __init__(self, *args):
        feature_names = [
            'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean',
            'concavity_mean', 'concave_mean', 'symmetry_mean', 'fractional_dimension_mean',
            'radius_seq', 'texture_seq', 'perimeter_seq', 'area_seq', 'smoothness_seq', 'compactness_seq',
            'concavity_seq', 'concave_seq', 'symmetry_seq', 'fractional_dimension_seq',
            'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst',
            'concavity_worst', 'concave_worst', 'symmetry_worst', 'fractional_dimension_worst'
        ]

        if len(args) != len(feature_names):
            raise ValueError(f"Expected {len(feature_names)} arguments, got {len(args)}")

        self.features = dict(zip(feature_names, args))

    def get_predict(self):
        try:
            input_data = np.array([float(value) for value in self.features.values()]).reshape(1, -1)

            prediction = model.predict(input_data)
            prediction_label = [np.argmax(prediction)]
        except Exception as e:
            print(f"Error during prediction: {e}")
            return None, None

        print(prediction)
        return prediction, prediction_label
