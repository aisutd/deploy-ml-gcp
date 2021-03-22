# import dependencies
import cv2

class Preprocessor(object):
    def __init__(self):
        pass

    def preprocess(self, image):
        """
        Resize and standardize images
        Args:
            image : np.array

        Returns;
            image : np.array
        """

        # resize
        image = cvl.resize(src = image, dsize = (224, 224), interpolation = cv2.INTER_LINEAR)

        # standardize
        image = (image - image.mean(axis = (0, 1, 2))) / image.std(axis = (0,1,2))

        return image
