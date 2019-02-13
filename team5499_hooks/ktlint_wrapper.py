import os
from subprocess import Popen

def main(argv=[]):
    print("0.3.12")
    if(os.sys.platform == "win32"):
        newArgs = ' '.join(argv)
        executable = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ktlint-wrapper.bat')
        p = Popen(executable + ' ' + newArgs)
        stdout, stderr = p.communicate()
        print(stdout)
        print()
        print(stderr)
    else:
        newArgs = ' '.join(argv)
        executable = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ktlint-wrapper.sh')
        p = Popen(executable + ' ' + newArgs)
        stdout, stderr = p.communicate()
        print(stdout)
        print()
        print(stderr)

if __name__ == '__main__':
    os.sys.exit(main(os.sys.argv[1:]))
