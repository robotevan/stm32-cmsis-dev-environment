cmake_minimum_required(VERSION 3.16)
set(CMAKE_TOOLCHAIN_FILE $ENV{STM32_CMAKE}/cmake/stm32_gcc.cmake)

project(stm32-fetch-cmsis-hal C ASM)

stm32_fetch_cmsis(F4 H7)
stm32_fetch_hal(F4 H7)

#find_package(CMSIS COMPONENTS STM32F407VG  REQUIRED)
find_package(CMSIS COMPONENTS STM32H743ZI_M7  REQUIRED)
#find_package(HAL COMPONENTS STM32F4 REQUIRED)


#include_directories("${CMAKE_SOURCE_DIR}/build/_deps/stm32-cmsis-h7-src/Include")

set(PROJECT_SOURCES
    src/main.c
)

add_executable(stm32-fetch-f4 ${PROJECT_SOURCES})
target_link_libraries(stm32-fetch-f4 CMSIS::STM32::H743ZI::M7 STM32::NoSys)
stm32_print_size_of_target(stm32-fetch-f4)

