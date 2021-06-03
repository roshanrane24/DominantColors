import cv2
from numpy import array, float64, ndarray, uint8


def rgb2hsl(color: ndarray) -> ndarray:
    R, G, B = color.astype(float64)
    R, G, B = R/255, G/255, B/255

    xmax = max(color)/255
    xmin = min(color)/255
    delta = xmax - xmin

    # Luminance
    L = (xmax + xmin)/2

    # Saturation (Hue when xmax=xmin)
    if xmax == xmin:
        return array([0, 0, L], dtype=uint8)
    elif L < 0.5:
        S = (delta)/(xmax + xmin)
    else:
        S = (delta)/(2 - xmax + xmin)

    # Hue
    if R == xmax:
        H = G - B/(delta)
    elif G == xmax:
        H = 2 + (B - R)/(delta)
    elif B == xmax:
        H = 4 + (R - G)/(delta)
    else:
        H = 0

    return array([H * 60, S * 100, L * 100], dtype=uint8)


def hsl2rgb(color: ndarray) -> ndarray:
    Hi, Si, Li = color.astype(float64)
    H, S, L = Hi/360, Si/100, Li/100

    if S == 0:
        return array([L * 255, L * 255, L * 255], dtype=uint8)

    if L < 0.5:
        t2 = L * (1 + S)
    else:
        t2 = L + S - L * S

    t1 = 2 * L - t2
    Rt = H + 1/3
    Gt = H
    Bt = H - 1/3

    return array([temp2rgb(t1, t2, Rt) * 255,
                  temp2rgb(t1, t2, Gt) * 255,
                  temp2rgb(t1, t2, Bt) * 255], dtype=uint8)


def temp2rgb(t1: ndarray, t2: ndarray, t3: ndarray) -> ndarray:
    if t3 < 0:
        t3 += 1
    elif t3 > 1:
        t3 -= 1

    if 6 * t3 < 1:
        return t1 + (t2 - t1) * 6 * t3
    elif 2 * t3 < 1:
        return t2
    elif 3 * t3 < 2:
        return t1 + (t2 - t1) * (2/3 - t3) * 6
    else:
        return t1


def rgb2hex(color: ndarray) -> str:
    r = "{}".format(hex(color[0]).split('x')[1].zfill(2))
    g = "{}".format(hex(color[1]).split('x')[1].zfill(2))
    b = "{}".format(hex(color[2]).split('x')[1].zfill(2))

    return "#{}{}{}".format(r, g, b)


def hsl2hex(color: ndarray) -> str:
    return rgb2hex(hsl2rgb(color))
