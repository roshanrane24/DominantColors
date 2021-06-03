from numpy import ndarray, ones, uint8
from dominant_colors.utils import Image
from sklearn.cluster import KMeans


class DominantColors:
    def __init__(self, path: str, no_of_colors: int = 5):
        self.image: Image = Image(path)
        self.clusters = no_of_colors
        self.colors: ndarray = self.get_colors()

    def colors_kmeans(self) -> KMeans:
        kmean = KMeans(n_clusters=self.clusters, random_state=42)
        self.image.resize()
        kmean.fit(self.image.get_rgb().reshape(self.image.width * self.image.height, 3))
        return kmean

    def get_colors(self) -> ndarray:
        if self.image.image is not None:
            return self.colors_kmeans().cluster_centers_.astype(uint8)
        else:
            return ones((3, 3), dtype=uint8) * 255
