import cv2
import os

os.system("pwd > temp.txt")
path_name_list = open("temp.txt", "r").readline().split("/")
os.system("rm temp.txt")
if not os.path.exists("./images/"):
    os.makedirs("images")
video_num = str(path_name_list[-1][:-1])
place = str(path_name_list[-2])
videofile = "video.mov"
cap = cv2.VideoCapture(videofile)
num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(int(num_frames))
mod = 1000 
while(True):
    ret, frame = cap.read()
    pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)  # 0-based index of the frame to be decoded/captured next

    if ret:
        # the frame is ready and already captured
        #print(str(int(pos_frame-1))+" frames")
        if int(pos_frame-1) % mod == 0:
            cv2.imwrite("./images/"+place+"_"+video_num+"_"+str(int((pos_frame-1)/mod))+".jpg", frame)
            print("saved "+"./images/"+place+"_"+video_num+"_"+str(int((pos_frame-1)/mod))+".jpg")
    else:
        # the frame is not ready so try again to capture it
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame-1)
        print("frame is not ready")
        cv2.waitKey(1000)  # wait till frame is ready

    # check if all frames were captured
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        break