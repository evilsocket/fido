TARGET    = #PROJECT_NAME#
MAIN_SRCS = $(wildcard src/*.c) $(wildcard src/*/*.c)
MAIN_OBJS = $(MAIN_SRCS:.c=.o)

# you can override this
ifndef ANDROID_SYSROOT
SYSROOT = #NDK_PATH#/platforms/android-18/arch-arm/
else
SYSROOT = $(ANDROID_SYSROOT)
endif

PREFIX  = arm-linux-androideabi-
CC		= $(PREFIX)gcc
CFLAGS  = -I. -Iinclude -fPIC -fPIE -pie --sysroot $(SYSROOT)
LDFLAGS = -llog

all: $(MAIN_OBJS)
	@$(CC) $(CFLAGS) -o $(TARGET) $(MAIN_OBJS) $(LDFLAGS)

run: all
	@adb push #PROJECT_NAME# /data/local/tmp/
	@adb shell chmod 777 /data/local/tmp/#PROJECT_NAME#
	@adb shell /data/local/tmp/#PROJECT_NAME#

%.o: %.c
	@$(CC) $(CFLAGS) -c -o $@ $<

clean:
	@rm -f src/*.o $(TARGET)
