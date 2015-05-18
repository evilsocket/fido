TARGET    = #PROJECT_NAME#
MAIN_SRCS = src/main.cpp
MAIN_OBJS = $(MAIN_SRCS:.cpp=.o)

# you can override this
ifndef ANDROID_SYSROOT
SYSROOT = #NDK_PATH#/platforms/android-18/arch-arm/
else
SYSROOT = $(ANDROID_SYSROOT)
endif

ifndef ANDROID_STLPORT_INCLUDES
STLPORT_INC = #NDK_PATH#/sources/cxx-stl/stlport/stlport/
else
STLPORT_INC = $(ANDROID_STLPORT_INCLUDES)
endif

ifndef ANDROID_STLPORT_LIBS
STLPORT_LIBS = #NDK_PATH#/sources/cxx-stl/stlport/libs/armeabi/
else
STLPORT_LIBS = $(ANDROID_STLPORT_LIBS)
endif

PREFIX   = arm-linux-androideabi-
CXX		 = $(PREFIX)g++
CXXFLAGS = -I. -Iinclude -I$(STLPORT_INC) -L$(STLPORT_LIBS) -fPIC -fPIE -pie --sysroot $(SYSROOT)
LDFLAGS  = -llog -lstlport_static

all: $(MAIN_OBJS)
	@$(CXX) $(CXXFLAGS) -o $(TARGET) $(MAIN_OBJS) $(LDFLAGS)

%.o: %.cpp
	@$(CXX) $(CXXFLAGS) -c -o $@ $<

clean:
	@rm -f src/*.o $(TARGET)
