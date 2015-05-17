cmake_minimum_required(VERSION 2.6)

project(#PROJECT_NAME# C)

set( PROJECT "#PROJECT_NAME#" )

include_directories("${PROJECT_SOURCE_DIR}")
include_directories("${PROJECT_SOURCE_DIR}/include")

set( CMAKE_C_FLAGS "-Wall" )

file( GLOB MAIN_SOURCES src/*.c )

add_executable( ${PROJECT} ${MAIN_SOURCES} )

set( CMAKE_COMPILE_FLAGS ${CMAKE_C_FLAGS})
