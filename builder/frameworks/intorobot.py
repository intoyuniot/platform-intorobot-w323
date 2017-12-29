# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
IntoRobot

IntoRobot Wiring-based Framework allows writing cross-platform software to
control devices attached to a wide range of Arduino boards to create all
kinds of creative coding, interactive objects, spaces or physical experiences.

www.intorobot.com
"""

# Extends: https://github.com/platformio/platform-espressif32/blob/develop/builder/main.py

from os.path import isdir, join

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()
platform = env.PioPlatform()
board = env.BoardConfig()

FRAMEWORK_NAME = "framework-intorobot-w323"
FRAMEWORK_DIR = platform.get_package_dir(FRAMEWORK_NAME)
FRAMEWORK_VERSION = platform.get_package_version(FRAMEWORK_NAME)
assert isdir(FRAMEWORK_DIR)

env.Append(
    ASFLAGS=[ "-c", "-g", "-MMD" ],
    CCFLAGS=[ "-g", "-w", "-Wfatal-errors" ],
    CXXFLAGS=[ "-fpermissive" ],

    CPPDEFINES=[
        ("INTOROBOT", 1),
        ("INTOYUN", 1),
        ("FIRMLIB_VERSION_STRING", FRAMEWORK_VERSION),
        ("PLATFORM_THREADING", 0),
        ("INTOROBOT_ARCH_XTENSA"),
        ("INTOROBOT_PLATFORM"),
        ("RELEASE_BUILD")
    ],

    LIBSOURCE_DIRS=[
        join(FRAMEWORK_DIR, "libraries")
    ],

    LINKFLAGS=[
        "-Wl,-EL",
        "-T", "esp32.common.ld",
        "-T", "esp32.rom.ld",
        "-T", "esp32.peripherals.ld",
        "-T", "esp32.rom.spiram_incompatible_fns.ld"
    ],

    UPLOADERFLAGS=[
        board.get("upload.address")    # flash start address
    ]
)

env.Prepend(
    CFLAGS=["-Wno-old-style-declaration"],

    CCFLAGS=[
        "-Wno-error=deprecated-declarations",
        "-Wno-unused-parameter",
        "-Wno-sign-compare",
        "-fstack-protector"
    ],

    CPPPATH=[
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "hal", "inc"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "hal", "shared"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "IntoRobot_Firmware_Driver", "inc"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "config"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "bluedroid"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "app_trace"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "app_update"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "bt"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "driver"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "esp32"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "esp_adc_cal"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "ethernet"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "fatfs"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "freertos"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "heap"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "jsmn"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "log"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "mdns"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "mbedtls"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "mbedtls_port"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "newlib"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "nvs_flash"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "openssl"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "spi_flash"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "sdmmc"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "spiffs"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "tcpip_adapter"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "vfs"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "ulp"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "wear_levelling"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "xtensa-debug-module"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "console"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "soc"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "coap"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "wpa_supplicant"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "expat"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "json"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "nghttp"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "lwip"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "include", "bootloader_support"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "shared", "inc"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "services", "inc"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "system", "inc"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "user", "inc"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "wiring", "inc"),
        join(FRAMEWORK_DIR, "variants", board.get("build.variant"), "hal", "inc"),
        join(FRAMEWORK_DIR, "variants", board.get("build.variant"), "wiring_ex", "inc"),
        join(FRAMEWORK_DIR, "variants", board.get("build.variant"), "communication", "mqtt", "inc")
    ],
    LIBPATH=[
        join(FRAMEWORK_DIR, "cores", board.get("build.core"), "platform", "MCU", "ESP32-Arduino", "sdk", "lib"),
        join(FRAMEWORK_DIR, "variants", board.get("build.variant"), "lib"),
        join(FRAMEWORK_DIR, "variants", board.get("build.variant"), "build", "linker")
    ],
    LIBS=[
        "wiring", "wiring_ex", "hal", "platform", "services", "communication", "system",
        "gcc", "openssl", "btdm_app", "fatfs", "wps", "coexist", "wear_levelling", "halhal", "newlib", "driver",
        "bootloader_support", "pp", "smartconfig", "jsmn", "wpa", "ethernet", "phy", "app_trace", "console", "ulp",
        "wpa_supplicant", "freertos", "bt", "micro-ecc", "cxx", "xtensa-debug-module", "mdns", "vfs", "soc", "core",
        "sdmmc", "coap", "tcpip_adapter", "c_nano", "rtc", "spi_flash", "wpa2", "esp32", "app_update", "nghttp",
        "spiffs", "espnow", "nvs_flash", "esp_adc_cal", "log", "expat", "m", "c", "heap", "mbedtls", "lwip",
        "net80211", "pthread", "json", "stdc++"
    ],
)

