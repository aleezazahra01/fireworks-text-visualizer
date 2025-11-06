# Fireworks Text Visualizer
### Working:
It detects brighter pixels using numpy and displays random celebration slogans dynamically and highlights the detected part with rectangles.It converts each frame to 
"HSV Color space" to detect colors and write that stufff and then save it in mp4 version.But you cant run this big ahh video on yo phone so you gotta re-encode it.
```bash
ffmpeg -i final.mp4 -vcodec libx264 -crf 18 -preset slow -pix_fmt yuv420p fixed.mp4
```
If you're my wifey Ayesha, here are the steps 
OFC you'd have python installed already ,run this shit in your terminal

```bash
pip install opencv
```
```bash
pip install numpy
```

Place your video to the same dir as your file.And just run the program and do the re-encode shii I've mentioned above.

It doesn’t use a real AI or deep learning mode LMAO just opencv and color detection.


<img width="699" height="495" alt="image" src="https://github.com/user-attachments/assets/543a9bd1-cfa2-424d-9532-76ac4b377f7e" />
