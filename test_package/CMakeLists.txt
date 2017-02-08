cmake_minimum_required(VERSION 2.8)
project(conan-glib-test)

# Solve Conan packages ########################################################
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package (PkgConfig REQUIRED)
pkg_check_modules (GLIB2   glib-2.0)

# Build Test ##################################################################
add_executable(${PROJECT_NAME} main.c)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

# Run Tests ###################################################################
find_program(GTESTER gtester)
enable_testing()
add_custom_target(check ${CMAKE_CTEST_COMMAND} -V)
add_test(NAME TestAll
        COMMAND ${GTESTER} ${PROJECT_NAME} --keep-going
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
add_dependencies(check ${PROJECT_NAME})