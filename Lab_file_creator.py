#Lab file Makeing script

import  os
inpPath= input("😄 your folder's path: ")
labNumber = input("😄 your Lab number(Example: 03): ")
Id = input("😄 your ID: ")
Sec = input("😄 your section(Optional): ")
os_type = os.name
directory_seperator = ""


#Checks if os is Unix-based and changes the directory seperator accordingly
#Works well with tilda too ^-^ be lazy!

if os.name == "posix":
    directory_seperator = "/"
    if "~/" in inpPath:
        inpPath = os.path.expanduser(inpPath)

else:
    directory_seperator = "\\"


if directory_seperator in inpPath:
    converter1 = inpPath.split("\\")
    pathCon = "/".join(converter1)

if Sec == "":
    Sec = "14"
folderName = f"LabSection{Sec}_{Id}_CSE221LabAssignment{labNumber}_Fall2023"
os.mkdir(f"{pathCon}/{folderName}")
path = f"{pathCon}/{folderName}"

taskNumInp = int(input("😄 How many tasks do we have? : "))

for i in range(taskNumInp):
    os.mkdir(f"{path}/Task{i+1}")
    crePyFile = open(f"{path}/Task{i+1}/Task{i+1}.py","w")
    crePyFile.close()
    creInpFile = open(f"{path}/Task{i+1}/input{i+1}.txt","w")
    creInpFile.close()
    creOutFile = open(f"{path}/Task{i+1}/output{i+1}.txt","w")
    creOutFile.close()

    crePyFile = open(f"{path}/Task{i + 1}/Task{i + 1}.py", "w")
    crePyFile.write(f'inp1=open("input{i+1}.txt","r")\n')
    crePyFile.write(f'out1=open("output{i+1}.txt","w")\n')
    crePyFile.write(f'#Start From Here\n')
    crePyFile.write(f'\n')
    crePyFile.write(f'inp1.close()\n')
    crePyFile.write(f'out1.close()')

print()
print("🎉 Great!")
print("🤘 you are good to go!")