import tensorflow as tf

def load_and_preprocess_image(filename, img_shape=224, scale=True):
    """
    Reads an image file, converts it into a tensor, resizes it, and normalizes pixel values.
    """
    img = tf.io.read_file(filename)
    img = tf.image.decode_jpeg(img)
    img = tf.image.resize(img, [img_shape, img_shape])
    return img / 255. if scale else img
