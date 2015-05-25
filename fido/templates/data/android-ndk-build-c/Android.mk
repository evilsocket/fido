LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE    := #PROJECT_NAME#
LOCAL_SRC_FILES := $(wildcard src/*.c) $(wildcard src/*/*.c)

LOCAL_C_INCLUDES += .
LOCAL_C_INCLUDES += include

LOCAL_CFLAGS += -Wall -pie -fPIE
LOCAL_LDFLAGS += -pie -fPIE

include $(BUILD_EXECUTABLE)
