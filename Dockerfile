FROM ubuntu:22.04


ARG ARM_TOOLCHAIN_URL="https://developer.arm.com/-/media/Files/downloads/gnu-rm/10.3-2021.10/gcc-arm-none-eabi-10.3-2021.10-x86_64-linux.tar.bz2"
ARG STM32_CMAKE_GIT="https://github.com/ObKo/stm32-cmake.git"

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    build-essential \
    git \
    cmake \
    wget && \
    apt-get clean 

RUN wget -O arm-toolchain.tar.bz2 ${ARM_TOOLCHAIN_URL} &&\
    mkdir /toolchain && \
    tar xvf arm-toolchain.tar.bz2 --strip-components=1 -C /toolchain && \
    rm arm-toolchain.tar.bz2 &&\
    cd .. &&\ 
    git clone ${STM32_CMAKE_GIT}

ENV STM32_CMAKE "/stm32-cmake"
ENV PATH "/toolchain/bin:$PATH"
