from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB, title):

    m = mse(imageA, imageB)
    s = ssim(imageA, imageB, multichannel=True)
    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    print("MSE: %.2f, SSIM: %.2f" % (m, s))
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    # plt.imshow(imageA, cmap=plt.cm.gray)
    # plt.axis("off")
    # show the second image
    ax = fig.add_subplot(1, 2, 2)

    if m > 40000 and s < 0.8:
        cv2.imwrite("query.jpg", imageB)
        print("Change found")

    # plt.imshow(imageB, cmap=plt.cm.gray)
    # plt.axis("off")
    # show the images
    # plt.show()

