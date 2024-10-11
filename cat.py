import os,sys,pathlib
path = pathlib.Path.cwd()
print(path,type(path))

cwd = os.getcwd()

def fun(filepath):
        filepath = path / filepath
        try:
             file = open(filepath,"r")
        except:
             sys.exit("cannot open {}".format(filepath))
        for i in file:
            print(i,end="")
        print()
        file.close()
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("cat.py command except 2 argument but {} was given".format(len(sys.argv)))
    fun(sys.argv[1])