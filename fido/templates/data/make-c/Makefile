TARGET    = #PROJECT_NAME#
MAIN_SRCS = src/main.c
MAIN_OBJS = $(MAIN_SRCS:.c=.o)

CC		  = gcc
CFLAGS    = -I. -Iinclude
LDFLAGS   =

all: $(MAIN_OBJS)
	@$(CC) $(CFLAGS) -o $(TARGET) $(MAIN_OBJS) $(LDFLAGS)

%.o: %.c
	@$(CC) $(CFLAGS) -c -o $@ $<

clean:
	@rm -f src/*.o $(TARGET)
