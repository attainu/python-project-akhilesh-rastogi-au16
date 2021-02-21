# Junk File Organizer
# Python Project To Sort Files 

import os ,shutil

print("WELCOME TO JUNK FILE ORGANISER")
print("PROGRAME BY - AKHILESH RASTOGI")

class FileOrganiser:
    def __init__(self):
        self.audio = [".mp3",".wma",".aac",".aac",".m4a"]
        self.video = [".mp4",".wmv",".avi",".mkv",".flv",".MKV",".mpeg"]
        self.docs = [".docx",".pdf",".xls",".xlsx",".ppt",".pptx",".xps"]
        self.software = [".exe",".apk"]
        self.zips = [".rar",".zip",".7z"]


    def junkFileOrganiser(self):  
        path ="C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing"
        folders = os.listdir(path)
        os.mkdir("C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\audio")
        os.mkdir("C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\video")
        os.mkdir("C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\docs")
        os.mkdir("C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\software")
        os.mkdir("C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\zips")
        os.mkdir("C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\unknow")
        os.mkdir("C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\code")
        for folder in folders:
            extension = os.path.splitext(folder)[1]
            if extension == "":
                print("it is a folder")
                files = os.listdir("C:\\Users\\Lenovo\\oneDrive\\Desktop\\testing\\"+folder)
                for file in files:
                    ext = os.path.splitext(file)[1]
                    newpath = path +"\\"+folder+"\\"
                    if ext in self.audio:
                        shutil.move(newpath + file, "C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\audio")
                    elif ext in self.video:
                        shutil.move(newpath + file, "C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\video")
                    elif ext in self.docs:
                        shutil.move(newpath + file, "C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\docs")
                    elif ext in self.software:
                        shutil.move(newpath + file, "C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\software")
                    elif ext in self.zips:
                        shutil.move(newpath + file, "C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\zips")
                    else:
                        shutil.move(newpath + file, "C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\unknow")
            elif extension in self.audio:
                shutil.move(path+"\\"+folder, "C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\audio")
            elif extension in self.video:
                shutil.move(path+"\\"+folder, "C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\video")
            elif extension in self.docs:
                shutil.move(path+"\\"+folder, "C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\docs")
            elif extension in self.software:
                shutil.move(path+"\\"+folder, "C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\software")
            elif extension in self.zips:
                shutil.move(path+"\\"+folder, "C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\zips")
            else:
                shutil.move(path+"\\"+folder, "C:\\Users\\Lenovo\\OneDrive\\Desktop\\testing\\unknow")

if __name__ == "__main__":
    print('#'*86)
    fileOrganiser = FileOrganiser()
    fileOrganiser.junkFileOrganiser()