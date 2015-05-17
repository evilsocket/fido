TARGET    = #PROJECT_NAME#
MAIN_SRCS = src/main.c
MAIN_OBJS = $(MAIN_SRCS:.c=.o)

# you can override this
ifndef ANDROID_SYSROOT
SYSROOT = $(HOME)/android/ndk/platforms/android-18/arch-arm/
else
SYSROOT = $(ANDROID_SYSROOT)
endif

PREFIX  = arm-linux-androideabi-
CC		= $(PREFIX)gcc
CFLAGS  = -I. -Iinclude -fPIC -fPIE -pie --sysroot $(SYSROOT)
LDFLAGS = -llog

all: $(MAIN_OBJS)
	@$(CC) $(CFLAGS) -o $(TARGET) $(MAIN_OBJS) $(LDFLAGS) 

%.o: %.c
	@$(CC) $(CFLAGS) -c -o $@ $<

clean:
	@rm -f src/*.o $(TARGET)
