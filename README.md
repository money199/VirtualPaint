# Virtual Paint

White brush painting on the canvas.

## Description

A replica of the paintbrush. The white tip of any object is detected and through the centre of the rectangular contour white colour is painted on the canvas. It works live on webCam i.e the colour is painted with the continuous movement of the tip of the object which is white. So a continuous line is painted tracking the live trajectory of the object's tip.

![whiteBrush](https://user-images.githubusercontent.com/61883605/131408705-861c2f65-76fd-41eb-97bc-78f01a55e9d4.JPG)


## Function's Explanation

### GetContours()

* Detect the corners of all the objects and bound the rectangle on each object detected.
* returns the coordinates (x,y) of the centre of all the bounded rectangles.

### findColor()

* Detect colour from the original image and pass mask of white colour into the GetContours(), which returns the tip of the brush.
* It also appends each point when called multiple times as the object moves in front of the webcam.

### drawOnCanvas()

* Draw a white trajectory of the object through the tip of the brush.



