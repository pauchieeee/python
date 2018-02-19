from easygui import *
import time 
import pygame
from time import sleep
import sys
import dropbox
import socket #internet connection checking
import random
import os
import subprocess #for keyboard popup
import signal #for keyboard popup
from firebase import firebase #trial for firebase DATABASE, not GOOGLE DRIVE
from picamera import PiCamera
import RPi.GPIO as GPIO
import cv2
import imutils
import numpy
from PIL import Image
import daltonization

#for ssim
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

#for text_overlay
from time import sleep  
from subprocess import call  
from datetime import datetime  
import sys  



camera = PiCamera()
camera.resolution = (810,435)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
camera.start_preview()

while True:
    input_state = GPIO.input(24)
#    ###for sound in IC:
#        #sound.play()
    if input_state == False:
        for i in range(3):
            sleep(0.0001)
            camera.capture('image%s.png' % i)
        camera.stop_preview()
        time.sleep(0.2)
        print("captured")
        print('Button Pressed')

        def variance_of_laplacian(image):

            return cv2.Laplacian(image, cv2.CV_64F).var()

        image = cv2.imread('image0.png')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm1 = variance_of_laplacian(gray)
        print (fm1)
        

        image = cv2.imread('image1.png')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm2= variance_of_laplacian(gray)
        print (fm2)

        image = cv2.imread('image2.png')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm3= variance_of_laplacian(gray)
        print (fm3)

        list= [fm1,fm2,fm3]
        x=max(list)
        
        
        if x==fm1:
            #PROTANOMALY
#            ###for sound in fourteen:
#                #sound.play()
            image = ("Others/CVDS4.gif")
            choices = ["Proceed"]
            reply = buttonbox(image=image, choices=choices)
       #     sound.stop()
#            ###for sound in SSP:
#                #sound.play()
                
            original = Image.open("image0.png") #Load the original image via PIL
            sim = daltonization.simulatep(original) #Simulate the effect of colourblindness on the original image
            print('done')
            sim.save("simP.jpg")#Save the simulated image
            print('SAVED SIMP')

#            ###for sound in fifteen:
 #               #sound.play()
            image = ("simP.jpg")
      #     sound.stop()
            choices = ["Proceed"]
            reply = buttonbox(image=image, choices=choices)
#            ###for sound in SSD:
#                 #sound.play()
                 

            #DEUTERANOMALY
            original = Image.open("image0.png") #Load the original image via PIL
            sim = daltonization.simulated(original) #Simulate the effect of colourblindness on the original image
            print('done')
            sim.save("simD.jpg")#Save the simulated image
            print('SAVED SIMD')

#            ###for sound in sixteen:
 #               #sound.play()
            image = ("simD.jpg")
       #     sound.stop()
            choices = ["Proceed"]
            reply = buttonbox(image=image, choices=choices)
 #           ###for sound in SST:
 #                #sound.play()
                 

            #TRITANOMALY
            original = Image.open("image0.png") #Load the original image via PIL
            sim = daltonization.simulatet(original) #Simulate the effect of colourblindness on the original image
            print('done')
            sim.save("simT.jpg")#Save the simulated image
            print('SAVED SIMT')

   #         ###for sound in seventeen:
    #            #sound.play()
            image = ("simT.jpg")
       #     sound.stop()
            choices = ["Proceed"]
            reply = buttonbox(image=image, choices=choices)

     #       ###for sound in combined:
       #         #sound.play()
            img=cv2.imread('image0.png')
            image = ("image0.png")
            choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
            reply = buttonbox(image=image, choices=choices)
           # #click
       #     sound.stop()
            
            #1
            while reply==choices[0]:
         #       ###for sound in combined:
         #           #sound.play()
                image = ("image0.png")
                choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                reply = buttonbox(image=image, choices=choices)
             #   #click
           #     sound.stop()
                
                #2
                while reply==choices[1]:
#                    ###for sound in combined:
 #                       #sound.play()
                    image = ("simP.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)
               #     #click
   #                 sound.stop()
                    
                    #3
                    while reply==choices[0]:
     #                   ###for sound in combined:
     #                       #sound.play()
                        image = ("image0.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                 #       #click
       #                 sound.stop()
                        
                    while reply==choices[2]:
         #               ###for sound in combined:
           #                 #sound.play()
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
               #         #click
             #           sound.stop()
                        
                    while reply==choices[3]:
           #             ###for sound in combined:
         #                   #sound.play()
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
             #           #click
               #         sound.stop()
                        
                #2      
                while reply==choices[2]:
            #        ###for sound in combined:
              #          #sound.play()
                    image = ("simD.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)
                #    #click
                  #  sound.stop()
                    
                    #3
                    while reply==choices[0]:
                    #    ###for sound in combined:
                      #      #sound.play()
                        image = ("image0.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                        ##click
                        #sound.stop()
                        
                    while reply==choices[1]:
                #        ##for sound in combined:
                 #           #sound.play()
                        image = ("simP.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                  #      #click
                    #    sound.stop()
                        
                    while reply==choices[3]:
                      #  ##for sound in combined:
                        #    #sound.play()
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                       # #click
                       # sound.stop()
                        
                #2
                while reply==choices[3]:
                   # ##for sound in combined:
                    #    #sound.play()
                    image = ("simT.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)
                    ##click
                   # sound.stop()
                    
                    #3
                    while reply==choices[0]:
                     #   ##for sound in combined:
                       #     #sound.play()
                        image = ("image0.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                        ##click
                        #sound.stop()
                        
                    while reply==choices[1]:
                   #     ##for sound in combined:
                     #       #sound.play()
                        image = ("simP.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                       # #click
                       # sound.stop()
                        
                    while reply==choices[2]:
                    #    ##for sound in combined:
                      #      #sound.play()
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                        ##click
                        #sound.stop()
                        
            #1
            while reply==choices[1]:
                ##for sound in combined:
                    #sound.play()
                image = ("simP.jpg")
                choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                reply = buttonbox(image=image, choices=choices)
                #click
                #sound.stop()
#################sound incomplete here          
               #2
                while reply==choices[0]:
                    image = ("image0.png")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[1]:
                        image = ("simP.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[2]:
                    image = ("simD.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image0.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[1]:
                        image = ("simP.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[3]:
                    image = ("simT.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[1]:
                        image = ("simP.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[0]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                

            #1
            while reply == choices[2]:
                image = ("simD.jpg")
                choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[0]:
                    image = ("image0.png")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[1]:
                        image = ("simP.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                        
                #2 
                while reply==choices[1]:
                    image = ("simP.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image0.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)


                #2
                while reply==choices[3]:
                    image = ("simT.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[1]:
                        image = ("simP.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[0]:
                        image = ("image0.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                
            #1
            while reply == choices[3]:
                image = ("simT.jpg")
                choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[0]:
                    image = ("image0.png")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[1]:
                        image = ("simP.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[1]:
                    image = ("simP.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image0.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[2]:
                    image = ("simD.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image0.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[1]:
                        image = ("simP.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
             
           
        elif x==fm2:
            #PROTANOMALY
            image = ("Others/CVDS4.gif")
            choices = ["Proceed"]
            reply = buttonbox(image=image, choices=choices)
            
            original = Image.open("/home/pi/Desktop/gui_final/image0.png") #Load the original image via PIL
            sim = daltonization.simulatep(original) #Simulate the effect of colourblindness on the original image
            print('done')
            sim.save("/home/pi/Desktop/gui_final/simP.jpg")#Save the simulated image
            print('SAVED SIMP')

            image = ("/home/pi/Desktop/gui_final/simP.jpg")
            choices = ["Proceed"]
            reply = buttonbox(image=image, choices=choices)
         

            #DEUTERANOMALY
            original = Image.open("/home/pi/Desktop/gui_final/image0.png") #Load the original image via PIL
            sim = daltonization.simulated(original) #Simulate the effect of colourblindness on the original image
            print('done')
            sim.save("/home/pi/Desktop/gui_final/simD.jpg")#Save the simulated image
            print('SAVED SIMD')

            image = ("/home/pi/Desktop/gui_final/simD.jpg")
            choices = ["Proceed"]
            reply = buttonbox(image=image, choices=choices)
         

            #TRITANOMALY
            original = Image.open("/home/pi/Desktop/gui_final/image0.png") #Load the original image via PIL
            sim = daltonization.simulatet(original) #Simulate the effect of colourblindness on the original image
            print('done')
            sim.save("/home/pi/Desktop/gui_final/simT.jpg")#Save the simulated image
            print('SAVED SIMT')

            image = ("/home/pi/Desktop/gui_final/simT.jpg")
            choices = ["Proceed"]
            reply = buttonbox(image=image, choices=choices)
            
            img=cv2.imread('/home/pi/Desktop/gui_final/image0.png')
            image = ("image0.png")
            choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
            reply = buttonbox(image=image, choices=choices)

            #1
            while reply==choices[0]:
                image = ("image1.png")
                choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[1]:
                    image = ("simP.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image1.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2      
                while reply==choices[2]:
                    image = ("simD.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image1.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[1]:
                        image = ("simP.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[3]:
                    image = ("simT.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image1.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[1]:
                        image = ("simP.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                
            #1
            while reply==choices[1]:
                image = ("simP.jpg")
                choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                reply = buttonbox(image=image, choices=choices)

               #2
                while reply==choices[0]:
                    image = ("image1.png")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[1]:
                        image = ("simP.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[2]:
                    image = ("simD.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image1.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[1]:
                        image = ("simP.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[3]:
                    image = ("simT.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[1]:
                        image = ("simP.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[0]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                

            #1
            while reply == choices[2]:
                image = ("simD.jpg")
                choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[0]:
                    image = ("image1.png")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[1]:
                        image = ("simP.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                        
                #2 
                while reply==choices[1]:
                    image = ("simP.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image1.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)


                #2
                while reply==choices[3]:
                    image = ("simT.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[1]:
                        image = ("simP.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[0]:
                        image = ("image1.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                
            #1
            while reply == choices[3]:
                image = ("simT.jpg")
                choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[0]:
                    image = ("image1.png")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[1]:
                        image = ("simP.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[1]:
                    image = ("simP.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image1.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[2]:
                    image = ("simD.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image1.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[1]:
                        image = ("simP.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
            
                   
        elif x==fm3:
            #PROTANOMALY
            image = ("Others/CVDS4.gif")
            choices = ["Proceed"]
            reply = buttonbox(image=image, choices=choices)
            
            original = Image.open("/home/pi/Desktop/gui_final/image0.png") #Load the original image via PIL
            sim = daltonization.simulatep(original) #Simulate the effect of colourblindness on the original image
            print('done')
            sim.save("/home/pi/Desktop/gui_final/simP.jpg")#Save the simulated image
            print('SAVED SIMP')

            image = ("/home/pi/Desktop/gui_final/simP.jpg")
            choices = ["Proceed"]
            reply = buttonbox(image=image, choices=choices)
         

            #DEUTERANOMALY
            original = Image.open("/home/pi/Desktop/gui_final/image0.png") #Load the original image via PIL
            sim = daltonization.simulated(original) #Simulate the effect of colourblindness on the original image
            print('done')
            sim.save("/home/pi/Desktop/gui_final/simD.jpg")#Save the simulated image
            print('SAVED SIMD')

            image = ("/home/pi/Desktop/gui_final/simD.jpg")
            choices = ["Proceed"]
            reply = buttonbox(image=image, choices=choices)
         

            #TRITANOMALY
            original = Image.open("/home/pi/Desktop/gui_final/image0.png") #Load the original image via PIL
            sim = daltonization.simulatet(original) #Simulate the effect of colourblindness on the original image
            print('done')
            sim.save("/home/pi/Desktop/gui_final/simT.jpg")#Save the simulated image
            print('SAVED SIMT')

            image = ("/home/pi/Desktop/gui_final/simT.jpg")
            choices = ["Proceed"]
            reply = buttonbox(image=image, choices=choices)
            
            img=cv2.imread('/home/pi/Desktop/gui_final/image0.png')
            image = ("image0.png")
            choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
            reply = buttonbox(image=image, choices=choices)


            #1
            while reply==choices[0]:
                image = ("image2.png")
                choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[1]:
                    image = ("simP.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image2.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2      
                while reply==choices[2]:
                    image = ("simD.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image2.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[1]:
                        image = ("simP.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[3]:
                    image = ("simT.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image2.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[1]:
                        image = ("simP.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                
            #1
            while reply==choices[1]:
                image = ("simP.jpg")
                choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                reply = buttonbox(image=image, choices=choices)

               #2
                while reply==choices[0]:
                    image = ("image2.png")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[1]:
                        image = ("simP.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[2]:
                    image = ("simD.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image2.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[1]:
                        image = ("simP.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[3]:
                    image = ("simT.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[1]:
                        image = ("simP.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[0]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                

            #1
            while reply == choices[2]:
                image = ("simD.jpg")
                choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[0]:
                    image = ("image2.png")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[1]:
                        image = ("simP.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                        
                #2 
                while reply==choices[1]:
                    image = ("simP.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image2.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)


                #2
                while reply==choices[3]:
                    image = ("simT.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[1]:
                        image = ("simP.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[0]:
                        image = ("image2.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                
            #1
            while reply == choices[3]:
                image = ("simT.jpg")
                choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[0]:
                    image = ("image2.png")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[1]:
                        image = ("simP.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[1]:
                    image = ("simP.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image2.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[2]:
                        image = ("simD.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)

                #2
                while reply==choices[2]:
                    image = ("simD.jpg")
                    choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                    reply = buttonbox(image=image, choices=choices)

                    #3
                    while reply==choices[0]:
                        image = ("image2.png")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[1]:
                        image = ("simP.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)
                    while reply==choices[3]:
                        image = ("simT.jpg")
                        choices = ["Image without Transformation","Protanomaly","Deuteranomaly", "Tritanomaly","Exit"]
                        reply = buttonbox(image=image, choices=choices)



