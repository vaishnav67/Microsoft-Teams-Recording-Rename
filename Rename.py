import os
directory=r"C:\Enter\The\Folder\Where\The\Videos\Are\Stored\Here"
os.chdir(directory)
file=os.listdir(directory)[0]
x=0
for i in range(0,len(file)):
    if(file[i]=='-'):
        x=i
        break
for file in os.listdir(directory):
    year=file[x+1:x+5]
    month=file[x+5:x+7]
    day=file[x+7:x+9]
    dmy=day+"-"+month+"-"+year
    src=directory+file 
    dst=directory+dmy+".mp4"
    print(file)
    os.rename(os.path.join(directory,file),os.path.join(directory,dmy+".mp4"))
