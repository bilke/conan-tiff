project(MyTiff C)
cmake_minimum_required(VERSION 2.8.12)

include(conanbuildinfo.cmake)

conan_basic_setup()

#set(CMAKE_RUNTIME_OUTPUT_DIRECTORY bin)
#message("${CONAN_CMAKE_MODULE_PATH}")
#set(CMAKE_MODULE_PATH ${CONAN_CMAKE_MODULE_PATH} ${CMAKE_MODULE_PATH})
#find_package(Tiff REQUIRED)

include_directories(${TIFF_INCLUDE_DIRS})
add_executable(tifftest tifftest.c)

target_link_libraries(tifftest ${CONAN_LIBS})
#target_link_libraries(shptest ${Tiff_LIBRARIES})
