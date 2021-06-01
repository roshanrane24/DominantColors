from numpy import ndarray, ones
from utils import Image
from sklearn.cluster import KMeans


class DominantColors:
    def __init__(self, path: str):
        self.image: Image = Image(path)
        self.colors: ndarray = self.get_colors()

    @staticmethod
    def colors_kmeans(image: Image, clusters: int = 3) -> KMeans:
        kmean = KMeans(n_clusters=clusters, random_state=42)
        kmean.fit(image.get_rgb().reshape(image.width * image.height, 3))
        return kmean

    def get_colors(self) -> ndarray:
        if self.image.image is not None:
            return self.colors_kmeans(self.image).cluster_centers_.astype(int)
        else:
            return ones((3, 3)) * 255
