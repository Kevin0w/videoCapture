import cv2
import difference as diff

cap = cv2.VideoCapture(0)
isTrue, first_frame = cap.read()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # diff.mse(first_frame, frame)
    diff.compare_images(first_frame, frame, "test")

    # Outline the image

    # edges = cv2.Canny(frame, 100, 200)
    # plt.subplot(121), plt.imshow(frame, cmap='gray')
    # plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(edges, cmap='gray')
    # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    # plt.show()
    # Display the resulting frame
    cv2.imshow("prev_frame", first_frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
