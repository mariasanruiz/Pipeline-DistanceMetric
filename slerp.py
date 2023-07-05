import numpy as np


# SLERP IMPLEMENTATION BETWEEN IMAGE EMBEDS to compute z*1audio = z0audio + slerp(z1frame - z0frame);
# To compute in the next phase the distance (z1audio - z*1audio)

# p0 = ref_img_embed (1)
# p1 = obj_img_embed (N)

def slerp(p0, p1_list, t):
    """Spherical Linear Interpolation between a single point p0 and a list of points p1."""
    interpolated_embeddings = []
    for p1 in p1_list:
        omega = np.arccos(np.dot(p0/np.linalg.norm(p0), p1/np.linalg.norm(p1)))
        so = np.sin(omega)
        interpolate = np.sin((1.0 - t) * omega) / so * p0 + np.sin(t * omega) / so * p1
        interpolated_embeddings.append(interpolate)
    return interpolated_embeddings



