import os 

os.system("sort -n -k 6 annotations.txt > res.txt")
os.system("identify reference.jpg > temp.txt")

f=open("res.txt","r")
f1 = open("temp.txt","r")

dim = (f1.readline().split(' ')[2]).split('x')
dim_x,dim_y = float(dim[0]),float(dim[1])

os.system("pwd > temp.txt")
path = open("temp.txt","r").readline().split('/')
folder1,folder2 = (path[-1])[:-1],path[-2] 
n=1000 #capture every nth frame


dictionary = {'"Pedestrian"\n': 0, '"Biker"\n' : 1, '"Bus"\n':2, '"Car"\n':3,'"Skater"\n':4,'"Cart"\n':5}
os.system("rm somefile.txt")
temp2 = 0
for line in f:
	num_list=line.split(' ')
	temp = dictionary[num_list[9]]
	num_list = [float(x) for x in num_list[:-1]]
	num_list.append(temp)
	if num_list[5]%n == 0 :
		if temp2 != int(num_list[5]/n):
			temp2 = int(num_list[5]/n)
			with open('somefile.txt', 'a') as the_file:
				the_file.write('\n')
		x_centre = float("{0:.6f}".format((num_list[1]+num_list[3])/(2*dim_x)))
		y_centre = float("{0:.6f}".format((num_list[2]+num_list[4])/(2*dim_y)))
		x_len = float("{0:.6f}".format(((num_list[3]-num_list[1])/dim_x)))
		y_len = float("{0:.6f}".format(((num_list[4]-num_list[2])/dim_y)))
		string = str(num_list[9])+" "+str(x_centre)+" "+str(y_centre)+" "
		string += str(x_len)+" "+str(y_len)
		with open('somefile.txt', 'a') as the_file:
			the_file.write(string+"\n")

f3 = open("somefile.txt","r").read().split("\n\n")
os.system("mkdir labels")
for i in range(len(f3)):
	filename="labels/"+str(folder2)+"_"+str(folder1)+"_"+str(i)+".txt"
	with open(filename, 'a') as the_file:
		the_file.write(f3[i])	

os.system("rm somefile.txt temp.txt res.txt")