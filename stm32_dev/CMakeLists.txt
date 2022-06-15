cmake_minimum_required(VERSION 3.16)
set(CMAKE_TOOLCHAIN_FILE $ENV{STM32_CMAKE}/cmake/stm32_gcc.cmake)

# Set your stm32 propreties here
SET(STM_CHIP "H7::M7")
SET(STM_BOARD "STM32H7")


project(test_fetch_cmsis C ASM)

stm32_fetch_cmsis(H7)


find_package(CMSIS COMPONENTS ${STM_BOARD} REQUIRED)
#find_package(HAL COMPONENTS ${STM_BOARD}  REQUIRED)

set(PROJECT_SOURCES
    src/main.c
)

include_directories(
    ${CMAKE_SOURCE_DIR}/inc
)


add_executable(${PROJECT_NAME} ${PROJECT_SOURCES})
target_link_libraries(${PROJECT_NAME} CMSIS::STM32::${STM_CHIP} STM32::NoSys)
stm32_print_size_of_target(${PROJECT_NAME})
