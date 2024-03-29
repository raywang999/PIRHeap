EXEC = test
CXX = g++ 

SOURCES := $(shell find ./src ./lib -name "*.cc")
OBJECTS= $(SOURCES:.cc=.o)
DEPENDS = $(OBJECTS:.o=.d)

LDLIBS = -lncurses

INCLUDE=$(shell pwd)
INCLUDE_PARAMS=$(INCLUDE:%=-I%)

CPPFLAGS = -MMD ${INCLUDE_PARAMS}
CXXFLAGS = -std=c++20 -g -Wall

${EXEC}: ${OBJECTS}
	${CXX} ${CXXFLAGS} ${CPPFLAGS} ${LIB_INCLUDE} ${OBJECTS} ${LDLIBS} -o ${EXEC}

-include ${DEPENDS}

.PHONY: clean

clean:
	rm ${OBJECTS} ${DEPENDS} ${EXEC}

.PHONY: check

check: 
	bash testall.bash


