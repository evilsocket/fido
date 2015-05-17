TARGET    = #PROJECT_NAME#
MAIN_SRCS = src/main.cpp
MAIN_OBJS = $(MAIN_SRCS:.cpp=.o)

CXX		  = g++
CXXFLAGS  = -I. -Iinclude
LDFLAGS   =

all: $(MAIN_OBJS)
	@$(CXX) $(CXXFLAGS) -o $(TARGET) $(MAIN_OBJS) $(LDFLAGS)

%.o: %.cpp
	@$(CXX) $(CXXFLAGS) -c -o $@ $<

clean:
	@rm -f src/*.o $(TARGET)
