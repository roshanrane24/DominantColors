from typing import Union

import cv2
import numpy as np


class Image(object):
    def __init__(self, image_path: str, channel_first: bool = False):
        self.channel_first = channel_first
        self.image = self.read(image_path)
        if self.image is not None:
            self.height, self.width = self.image.shape[:-1]
        else:
            self.height, self.width = 0, 0

    @staticmethod
    def read(image_path: str) -> Union[np.ndarray, None]:
        return cv2.imread(image_path)

    def get_rgb(self) -> np.ndarray:
        if self.channel_first:
            return np.moveaxis(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB),
                               2, 0)
        else:
            return cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

    def get_hsv(self) -> np.ndarray:
        if self.channel_first:
            return np.moveaxis(cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV),
                               2, 0)
        else:
            return cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

    @staticmethod
    def show_image(image: np.ndarray, w_name: str = 'image') -> None:
        while True:
            cv2.imshow(w_name, image)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        cv2.destroyAllWindows()

    def show(self) -> None:
        if self.image is not None:
            self.show_image(self.image)
