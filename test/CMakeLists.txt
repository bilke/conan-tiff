project(MyTiff C)
cmake_minimum_required(VERSION 2.8.12)

include(conanbuildinfo.cmake)

conan_basic_setup()

include_directories(${TIFF_INCLUDE_DIRS})
add_executable(tifftest tifftest.c)

target_link_libraries(tifftest ${CONAN_LIBS})
