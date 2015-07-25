import os
os.chdir(r"C:\Users\Raghava\Desktop\Dump\DataAnalysis\ScourceForge\DataDump")
temp = ""
for files in os.listdir("."):
    if files.endswith(".txt"):
        f = open(files,"r")
        lines = f.readlines()
        f.close(   )
        f = open(files,"w")
        for line in lines:
            if line != temp:
                f.write(line)
            temp=line                
        f.close()
