from os import sys
from subprocess import Popen

def main(argv=[]):
    if(sys.platform == "win32"):
        newArgs = ' '.join(argv)
        p = Popen('ktlint-wrapper.bat ' + newArgs)
        stdout, stderr = p.communicate()
        print(stdout)
        print()
        print(stderr)
    else:
        newArgs = ' '.join(argv)
        p = Popen('ktlint-wrapper.sh ' + newArgs)
        stdout, stderr = p.communicate()
        print(stdout)
        print()
        print(stderr)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
