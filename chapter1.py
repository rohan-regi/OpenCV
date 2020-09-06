import cv2
import numpy as np
#print("package Imported")


# img = cv2.imread("Resources/lena.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture(0)
# cap.set(3,640)# id 3 is the width
# cap.set(4,480)# id 4 is the height
# cap.set(10,100)# id 4 is brightness
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) and 0xFF ==ord('q'):
#         break


# to apply filters to an image
# img = cv2.imread("Resources/lena.png")
# kernal = np.ones((5,5),np.uint8)
#
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#for b and w
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)# for blur
# imgCanny = cv2.Canny(img,150,200)# for edge detection canny filter to cahnge the edges
# #change (img,100,100) to (img,150,200)
# imgDialation = cv2.dilate(imgCanny,kernal, iterations =1)# this is to change the thickness of the lines of the canny image
# #change iterations to increase thickness
# imgEroded = cv2.erode(imgDialation,kernal,iterations=1)# this thin's the lines
#
# cv2.imshow("GRAY IMAGE",imgGray)
# cv2.imshow("blur IMAGE",imgBlur)
# cv2.imshow("canny IMAGE",imgCanny)
# cv2.imshow("dilation IMAGE",imgDialation)
# cv2.imshow("eroded IMAGE",imgEroded)
# cv2.waitKey(0)


# cropping and resizing
# img = cv2.imread("Resources/lena.png")
# print(img.shape)
#
# imgResize = cv2.resize(img,(300,200))#width, height
# print(imgResize.shape)
#
# imgCropped = img[0:200, 200:500]#height , width
#
# cv2.imshow("Image",img)
# cv2.imshow("Image resize",imgResize)
# cv2.imshow("Image cropped",imgCropped)
# cv2.waitKey(0)

#shapes and  texts
# img = np.zeros((512,512,3),np.uint8)
# print(img.shape)
# img[200:300,100:300] = 0,255,0#img[:] to color the whole image color format BGR

# cv2.line(img,(0,0),(300,300),(0,255,0),3)#(pt1, pt2, color,thickness) to daw a line in the image
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
# cv2.circle(img,(400,50),30,(255,255,0),5)

#text on image
# cv2.putText(img,"OPEN CV",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
#
# cv2.imshow("image",img)
#
# cv2.waitKey(0)



#WARP PERPECTIVE
# img = cv2.imread("Resources/cards.jpg")
# width, height = 250,350
# pts1 = np.float32([[303,72],[460,68],[305,263],[483,253]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgOutput = cv2.warpPerspective(img, matrix,(width,height))
#
# cv2.imshow("Image", img)
# cv2.imshow("output",imgOutput)
# cv2.waitKey(0)

#joining images

#
# def stackImages(scale,imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor= np.hstack(imgArray)
#         ver = hor
#     return ver
#
#
# img = cv2.imread("Resources/lena.png")
# imgGray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgstack = stackImages(0.5,([img,imgGray,img],[img,img,img]))



# imghor = np.hstack((img,img))
# imgverti = np.vstack((img,img))
#
# cv2.imshow("Horizontal",imghor)
# cv2.imshow("vertical",imgverti)
# cv2.imshow("ImageStack",imgstack)
#
#
# cv2.waitKey(0)

#color detection

# def empty(a):
#     pass
#
# def stackImages(scale,imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor= np.hstack(imgArray)
#         ver = hor
#     return ver
#
#
# path = "Resources/lambo.png"
# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars",640,240)
# cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
# cv2.createTrackbar("Hue Max","TrackBars",19,179,empty)
# cv2.createTrackbar("Sat Min","TrackBars",110,255,empty)
# cv2.createTrackbar("Sat Max","TrackBars",240,255,empty)
# cv2.createTrackbar("Val Min","TrackBars",153,255,empty)
# cv2.createTrackbar("Val Max","TrackBars",255,255,empty)
#
# while True:
#     img = cv2.imread(path)
#     imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
#     h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
#     s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
#     s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
#     v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
#     v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
#     print(h_min, h_max, s_min, s_max, v_min, v_max)
#     lower = np.array([h_min, s_min, v_min])
#     upper = np.array([h_max, s_max, v_max])
#     mask = cv2.inRange(imghsv, lower, upper)
#     imgResult = cv2.bitwise_and(img, img, mask=mask)
#
#     # cv2.imshow("Origional",img)
#     # cv2.imshow("hsvc",imghsv)
#     # cv2.imshow("Mask", mask)
#     # cv2.imshow("Result", imgResult)
#
#     imgStack = stackImages(0.6, ([img, imghsv], [mask, imgResult]))
#     cv2.imshow("Stacked Images", imgStack)
#
#     cv2.waitKey(1)

#contours/shape detection

# def stackImages(scale,imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor= np.hstack(imgArray)
#         ver = hor
#     return ver
#
# def getContours(img):
#     contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         print(area)
#         if area > 500:
#             cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
#             peri = cv2.arcLength(cnt,True)
#             #print(peri)
#             approx=cv2.approxPolyDP(cnt,.02*peri,True)
#             print(len(approx))#print(approx)
#             objCor = len(approx)
#             x,y,w,h = cv2.boundingRect(approx)
#
#             if objCor == 3: objectType = "Tri"
#             elif objCor == 4:
#                 aspratio = w/float(h)
#                 if aspratio>0.95 and aspratio < 1.05:objectType= "Square"
#                 else:objectType="Rectangle"
#             elif objCor>4: objectType = "Circle"
#             else:objectType="None"
#
#             cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
#             cv2.putText(imgContour,objectType,
#                         (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)
#
#
# path = "Resources/shapes.png"
# img = cv2.imread(path)
# imgContour = img.copy()
#
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
# imgCanny = cv2.Canny(imgBlur,50,50)
# getContours(imgCanny)
#
# imgBlank = np.zeros_like(img)
# imgStack = stackImages(0.8,([img,imgGray,imgBlur],
#                             [imgCanny,imgContour,imgBlank]))
#
# cv2.imshow("Stack",imgStack)
#
# cv2.waitKey(0)




















