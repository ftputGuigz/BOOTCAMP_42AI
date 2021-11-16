from ImageProcessor import ImageProcessor 

imp = ImageProcessor()
arr = imp.load("non_existing_file.png")
# Output
#Exception: FileNotFoundError -- strerror: No such file or directory

print(arr) 
# Output 
# None

arr = imp.load("empty_file.png")
# Output
Exception: OSError -- strerror: None

print(arr) 
# Output 
# None
arr = imp.load("../resources/42AI.png") 
# Output
#Loading image of dimensions 200 x 200

arr
# Output
#array([[[0.03529412, 0.12156863, 0.3137255 ],
#        [0.03921569, 0.1254902 , 0.31764707],
#        [0.04313726, 0.12941177, 0.3254902 ],
#        ...,
#        [0.02745098, 0.07450981, 0.22745098],
#        [0.02745098, 0.07450981, 0.22745098],
#        [0.02352941, 0.07058824, 0.22352941]],
#       [[0.03921569, 0.11764706, 0.30588236],
#        [0.03529412, 0.11764706, 0.30980393],
#        [0.03921569, 0.12156863, 0.30980393],
#        ...,
#        [0.02352941, 0.07450981, 0.22745098],
#        [0.02352941, 0.07450981, 0.22745098],
#        [0.02352941, 0.07450981, 0.22745098]],
#       [[0.03137255, 0.10980392, 0.2901961 ],
#        [0.03137255, 0.11372549, 0.29803923],
#        [0.03529412, 0.11764706, 0.30588236],
#        ...,
#        [0.02745098, 0.07450981, 0.23137255],
#        [0.02352941, 0.07450981, 0.22745098],
#        [0.02352941, 0.07450981, 0.22745098]],
#...,
#       [[0.03137255, 0.07450981, 0.21960784],
#        [0.03137255, 0.07058824, 0.21568628],
#        [0.03137255, 0.07058824, 0.21960784],
#        ...,
#        [0.03921569, 0.10980392, 0.2784314 ],
#        [0.03921569, 0.10980392, 0.27450982],
#        [0.03921569, 0.10980392, 0.27450982]],
#       [[0.03137255, 0.07058824, 0.21960784],
#        [0.03137255, 0.07058824, 0.21568628],
#        [0.03137255, 0.07058824, 0.21568628],
#        ...,
#        [0.03921569, 0.10588235, 0.27058825],
#        [0.03921569, 0.10588235, 0.27058825],
#        [0.03921569, 0.10588235, 0.27058825]],
#       [[0.03137255, 0.07058824, 0.21960784],
#        [0.03137255, 0.07058824, 0.21176471],
#        [0.03137255, 0.07058824, 0.21568628],
#        ...,
#        [0.03921569, 0.10588235, 0.26666668],
#        [0.03921569, 0.10588235, 0.26666668],
#        [0.03921569, 0.10588235, 0.26666668]]], dtype=float32)
# 
imp.display(arr)

img = ImageProcessor.load("elon_canaGAN.png")
print(type(img))
print(img)
ImageProcessor.display(img)