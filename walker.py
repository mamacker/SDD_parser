import os

if not os.path.exists("../videos/images/"):
    os.makedirs("../videos/images/")

for d in os.listdir("../videos/"):
    path = ("../videos/"+d+"/")
    for d1 in os.listdir(path):
        path1 = path+d1+"/"
        os.system("cp video.py "+path1+"video.py")
        os.system("sh ../../python-envs/nnenv/bin/activate && cd "+path1+" && python video.py")
        os.system("cp "+path1+"images/* ../videos/images/")
        os.system("rm "+path1+"video.py")