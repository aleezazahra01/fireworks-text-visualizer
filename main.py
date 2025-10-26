import cv2
import numpy as np
import random
import time

#--first time implementing numpy too <3---

# color palettes for variety 
possible_colors = [
    (255, 200, 200), (200, 255, 200), (200, 200, 255),
    (255, 255, 150), (255, 180, 255), (180, 255, 255)
]
video = cv2.VideoCapture('fireworks.mp4')

# getting basic video info
fps = int(video.get(cv2.CAP_PROP_FPS))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# making sure output matches input size + fps
output = cv2.VideoWriter('final.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

# just some random greetings that’ll appear when fireworks are detected
greetings = [
    "Happy Diwali", "Eid Mubarak", "Merry Christmas",
    "Happy Holi", "Ramadan Mubarak", "Happy Birthday", "I love him"
]  # some random ah things you wanna display (the text is small asf so put any random shi)

frame_count = 0  # frame counter cuz why not



while True:
    ret, frame = video.read()
    if not ret:
        break

    # blur the video a bit to make fireworks pop out
    blurred = cv2.GaussianBlur(frame, (15, 15), 0)

    # convert to HSV because it’s easier to pick bright areas
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # this code detects the brighter pixels 
    lower_light = np.array([0, 80, 200])
    upper_light = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, lower_light, upper_light)

   
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # loop through each detected sparkle / region
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300:  # ignore tiny dots
            x, y, w, h = cv2.boundingRect(contour)

            # pick a random color each time
            color = random.choice(possible_colors)

            # draw that box
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
             message = random.choice(greetings)
            # make text placement slightly random so it doesn't overlap perfectly
            text_x = x + random.randint(-20, 20)
            text_y = y - random.randint(10, 40)

            # safety so text doesn't go out of frame
            text_x = max(10, min(text_x, width - 200))
            text_y = max(30, text_y)

        
            txt_color = random.choice([(255, 255, 255), (255, 230, 230), (200, 255, 255)])

            cv2.putText(frame, message, (text_x, text_y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, txt_color, 2, cv2.LINE_AA)

  

    # write current frame into final output
    output.write(frame)
    frame_count += 1

    # for preview
    cv2.imshow("Fireworks Celebration", frame)


    if frame_count % 100 == 0:
        time.sleep(0.05)  # just a breather for CPU 

    if cv2.waitKey(1) == 27:  # press ESC to stop if you want to ig
        break

# after-care 
video.release()
output.release()
cv2.destroyAllWindows()
print("done ")
