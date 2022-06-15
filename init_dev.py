import os
from tkinter.messagebox import RETRY

DOCKER_IMG = "stm32-dev-ubuntu"

# get unix style path
STM_DEV_PATH = os.path.join(os.getcwd(), "stm32_dev").replace("\\", "/")

DOCKER_CMD = "docker run --rm -it -v " + STM_DEV_PATH + ":/stm32_dev " + DOCKER_IMG

os.system(DOCKER_CMD)