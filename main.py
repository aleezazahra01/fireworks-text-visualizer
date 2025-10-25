import cv2
import numpy as np
import random

#--first time implementing numpy too <3---

video = cv2.VideoCapture('fireworks.mp4')

fps = int(video.get(cv2.CAP_PROP_FPS))
width, height = int(video.get(3)), int(video.get(4))

output = cv2.VideoWriter('final.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))


greetings = [
    "Happy Diwali", "Eid Mubarak", "Merry Christmas", 
    "Happy Holi", "Ramadan Mubarak", "Happy Birthday", "I love him"
] #some random ah things you wanna display (the text is small asf so put any random shi)

frame_count = 0  #frame count

while True:
    ret, frame = video.read()
    if not ret:
        break

    blurred = cv2.GaussianBlur(frame, (15, 15), 0)


    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)  #for brighter colours
  #the following code detects the pixels that are bright
    lower_light = np.array([0, 80, 200])
    upper_light = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, lower_light, upper_light)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for contour in contours:
        if cv2.contourArea(contour) > 300:
            x, y, w, h = cv2.boundingRect(contour)
            color = [random.randint(100, 255) for _ in range(3)]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

 
            message = random.choice(greetings)  #add a random greeting
            cv2.putText(frame, message, (x, max(20, y - 20)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)


    output.write(frame)
    frame_count += 1

   #for preview
    cv2.imshow("Fireworks Celebration", frame)
    if cv2.waitKey(1) == 27:  # press ESC to stop if you want to ig
        break
      
#after-care
video.release()
output.release()
cv2.destroyAllWindows()
print("done")
