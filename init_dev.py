import os
import sys
from tracemalloc import start

# name of docker image
DOCKER_IMG = "stm32-dev-ubuntu"
# get unix style path
STM_DEV_PATH = os.path.join(os.getcwd(), "stm32_dev").replace("\\", "/")
# Docker system headers path
HOST_SYS_HEADERS_PATH = os.path.join(os.getcwd(), ".sys_headers").replace("\\", "/")


def build_image():
    build_cmd = "docker build -t " + DOCKER_IMG + " ."
    os.system(build_cmd)

def copy_docker_headers():
    docker_cp_cmd = "docker run --rm -v " + HOST_SYS_HEADERS_PATH + ":/tmp/sys_headers " + \
                    DOCKER_IMG + " bash -c \"cp -r usr/include/* tmp/sys_headers/\""
    os.system(docker_cp_cmd)


def start_interactive():
    docker_cmd = "docker run --rm -it -v " + STM_DEV_PATH + ":/stm32_dev " + DOCKER_IMG
    os.system(docker_cmd)

def build_application():
    docker_build = "docker run --rm -it -v " + STM_DEV_PATH + ":/stm32_dev " + \
                   DOCKER_IMG + " bash -c \"cd /stm32_dev/build && cmake .. && make\""
    os.system(docker_build)

def flash_application():
    docker_flash = "docker run --rm -it -v " + STM_DEV_PATH + ":/stm32_dev " + \
                   DOCKER_IMG + " bash -c \"cd /stm32_dev/build && cmake ..\""
    os.system(docker_flash)

if __name__ == "__main__":
    args = sys.argv[1:]
    
    if args[0] == "--init" or args[0] == "-i":
        build_image()
    elif args[0] == "--build" or args[0] == "-b":
        build_application()
    elif args[0] == "--interactive" or args[0] == "-it":
        start_interactive()
    elif args[0] == "--flash" or args[0] == "-f":
        copy_docker_headers()
    else:
        print("Invalid argument!")