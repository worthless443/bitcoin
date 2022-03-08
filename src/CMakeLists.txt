project(bitcoin_test_build)

file(GLOB SRCES ./*)
set(ALL_INCLUDE ./ ./wallet ./leveldb/include ./univalue/include)

include_directories(${ALL_INCLUDE})
add_library(libtest.a ${SRCES})
