import os,sys,argparse
def ls():
    
    a = os.listdir("./")
    for i in a:
        print(i)
if __name__ == "__main__":
    ls()