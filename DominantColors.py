from PIL import Image
import numpy as np
from scipy.cluster.vq import whiten
from scipy.cluster.vq import kmeans2
import pandas as pd
from typing import List, Tuple


def img2df(img_file: str) -> pd.DataFrame:
    img: Image = Image.open(img_file)
    img_arr: np.ndarray = np.array(img).reshape((img.size[0] * img.size[1], 3))

    return pd.DataFrame(img_arr, columns=['red', 'green', 'blue'])


def dominant_colors(df: pd.DataFrame,
                    no_of_colors: int = 3) -> List[Tuple[int]]:
    df['scaled_color_red'] = whiten(df['red'])
    df['scaled_color_blue'] = whiten(df['blue'])
    df['scaled_color_green'] = whiten(df['green'])

    cluster_centers, _ = kmeans2(df[['scaled_color_red',
                                     'scaled_color_blue',
                                     'scaled_color_green']],
                                 no_of_colors)
    dominant_colors_list = []
    red_std, green_std, blue_std = df[['red', 'green', 'blue']].std()

    for cluster_center in cluster_centers:
        red_scaled, green_scaled, blue_scaled = cluster_center
        dominant_colors_list.append((
            round(red_scaled * red_std),
            round(green_scaled * green_std),
            round(blue_scaled * blue_std)))

    return dominant_colors_list


def get_dominant_colors(img_file: str) -> List[Tuple[int]]:
    return dominant_colors(img2df(img_file))


if __name__ == "__main__":
    df = img2df("./bulgaria.jpg")
    colors = dominant_colors(df)
    for color in colors:
        print(color)
        Image.new("RGB", (256, 256), color).show()
        input("Continue?")
