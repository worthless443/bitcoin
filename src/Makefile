CXX=g++
SRC_=$(shell ls *.cpp)
SRC=$(patsubst %.cpp,%,$(SRC_))
INCLUDE_FLAGS=-I./  -I./wallet -I./leveldb/include -I./univalue/include
LINK=$(shell ls build/*.o)
#LINK=$(patsubst %,build/%,$(LINK_))

.PHONY: src $(SRC)
src:$(SRC)
$(SRC):
	$(CXX) -c $@.cpp $(INCLUDE_FLAGS)  -o build/$(@).o
