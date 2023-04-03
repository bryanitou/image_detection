import cv2


def photo_analyzer(filename, id_wanted, show=False, output=None):
    # Local auxiliary variable
    trigger = False

    # Load the image
    frame = cv2.imread(filename)

    if show:
        cv2.imshow('Original', frame)
        cv2.waitKey(0)

    # Use the cvtColor() function to grayscale the image
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if show:
        cv2.imshow('Grayscale', gray_image)
        cv2.waitKey(0)
        # Window shown waits for any key pressing event
        # Window shown waits for any key pressing event
        # Window shown waits for any key pressing event
        
        cv2.destroyAllWindows()
#imessed up the commit
    # imessed up the commit
    dictionary_main = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    
    #bits_str = dictionary_main['marker_7']
    #print(bits_str)
    #fs = cv2.FileStorage("/home/pi/dictionary.txt")
    #dict_str = dictionary_main.writeDictionary(fs)
    a = []
    a = cv2.aruco.Dictionary.readDictionary(fn)

    # detector = cv2.aruco.ArucoDetector(dictionary, parameters)

    markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(gray_image, dictionary, parameters=parameters)
    # frame_markers = cv2.aruco.drawDetectedMarkers(frame.copy(), markerCorners, markerIds)

    if markerIds is not None:
        for id in markerIds:
            if id == id_wanted:
                trigger = True

    if show or output is not None:
        # plt.figure()
        # plt.imshow(frame_markers, origin="upper")
        if markerIds is not None:
            for i in range(len(markerIds)):
                c = markerCorners[i][0]
                # plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "+", label="id={0}".format(markerIds[i]))
                """for points in rejectedImgPoints:
                    y = points[:, 0]
                    x = points[:, 1]
                    plt.plot(x, y, ".m-", linewidth = 1.)"""
        # plt.legend()
        #if show:
        #    # plt.show()
        #if output is not None:
        #    # plt.savefig(output)

    return trigger


# TODO: remove this
if __name__ == '__main__':
    # Call main function
    photo_analyzer(filename="test/aruco_id7_grass.jpeg", id_wanted=7, show=True)
