WPC Stand-alone_python_release changelog
=======================================

v0.5.12 Date: 2024/02/21, Developer: Chunglee_people
----------------------------------------------------
### Fixed
- example code:
    - AI_N_samples_with_logger.py
    - modbus slave & master

v0.5.11 Date: 2024/01/26, Developer: Chunglee_people
----------------------------------------------------
### Added
- Support Modbus_master
- example code: Series of `Modbus master` code

v0.5.10 Date: 2024/01/18, Developer: Chunglee_people
---------------------------------------------------
### Added
- Four mechanisms to prevent the execution of main.py:
    - Safe pin on the board.
    - Counting the number of reboots within a short period. If it exceeds N times, main.py will no longer be executed.
    - In the web configuration, the option to disable/enable main.py.
    - In MicroPython, the addition of Sys_disableMain() / Sys_enableMain(), allowing users to change the execution status of main.py at any time.

v0.5.6 Date: 2023/12/07, Developer: Chunglee_people
---------------------------------------------------
### Added
- Add `Web_editor` in examples/PC
- example code: AHRS_read.py
- Support Web editor

v0.5.0 Date: 2023/11/20, Developer: Chunglee_people
---------------------------------------------------
### Added
- Get Started for user
- example code: hello_world.py

### Fixed
- The content of Thread_LED.py
- Add a conditional statement inside the while loop in Wifi_connect.py

v0.4.1 Date: 2023/10/05, Developer: Chunglee_people
---------------------------------------------------
### Added
- New function: OLED_erase and OLED_writeLine in PYCO_ETH

### Fixed
- Fix LED_control.py's example code

v0.4.0 Date: 2023/10/02, Developer: Chunglee_people
---------------------------------------------------
### Added
- Add SDcard, Save pin
- Advantage of PYCO at documentation
- function: pywpc.LED_reset

### Removed
- All accelerometer relative functions
- DO_writePins and DI_readPins in PYCO_ETH

v0.3.1 Date: 2023/09/21, Developer: Chunglee_people
----------------------------------------------------
### Added
- pywpc_sd.mpy

### Changed
- example name:
    - SDCard -> SD Card

### Removed
- pywpc_ex.mpy

v0.3.0 Date: 2023/09/19, Developer: Chunglee_people
----------------------------------------------------
### Added
- The content of main.py when execute initial setup
(micropython/ports/esp32/modules/inisetup.py)
- pywpc_ex.mpy, pywpc_ota.mpy, sdcard.mpy in ports/esp32/modules
- modify_configuration/PYCO_ETH.md & PYCO_WIFI.md

### Fixed
- The print content when file system corrupted
- The content of boot.py when execute initial setup
- The content of mip.install.py example code

### Removed
- examples/External/pywpc_ex.py

v0.2.2 Date: 2023/09/18, Developer: Chunglee_people
----------------------------------------------------
### Changed
- example name:
    - gesture_detect -> acceleration_movement

### Fixed
- The content in Tutorial_ETH/Thread_AIO.py, OLED_writeLine.py

### Removed
- Inappropriate words

v0.2.1 Date: 2023/09/18, Developer: Chunglee_people
----------------------------------------------------
### Added
- gesture detect.py in Sphinx

v0.2.0 Date: 2023/09/14, Developer: Chunglee_people
----------------------------------------------------
### Added
- tinyml's folder

### Changed
- API name:
    - getFiles -> getFileDirectory

v0.1.1 Date: 2023/09/13, Developer: Chunglee_people
----------------------------------------------------
### Added
- pywpc_ex.py
- v0.1.1_20230913.bin file

### Changed
- example name:
    - Read from SDCard -> Read from SD Card
    - Write into SDCard -> Write to SD Card

### Fixed
- mip.install.py's contents
- Initialize sdcard pin in the class of SDcard

v0.1.0 Date: 2023/09/11, Developer: Chunglee_people
----------------------------------------------------
### Added
- examples_PYCO_ETH.rst & examples_PYCO_WIFI.rst
- SDCard example code: Read from SDCard.py, Write into SDCard.py

### Changed
- example name:
    - FFT (simulate)  -> FFT (simulated)
    - FFT (AI sample) -> FFT (AI Nsample)

### Fixed
- Depended on product's modules, rearrange the display of example codes

### Removed
- examples.rst

v0.0.18 Date: 2023/09/08, Developer: Chunglee_people
----------------------------------------------------
### Added
- Example: TCP server write U8 list, FFT (AI sample), FFT (plot)
- PC example: CSV_plot_AI.py, TCP_client_with_plot_FFT.py

### Changed
- Example name:
    - TCP server write -> TCP server write string
    - FFT -> FFT (simulate)

v0.0.17 Date: 2023/09/05, Developer: Chunglee_people
----------------------------------------------------
### Added
- Decorate sphinx's homepage

### Changed
- Example name: Fourier transform -> FFT
- friendly_repl_reset's messages

v0.0.16 Date: 2023/09/01, Developer: Chunglee_people
----------------------------------------------------
### Added
- external library: ulab
- New example code: forurier_transform.py

v0.0.15 Date: 2023/08/29, Developer: Chunglee_people
----------------------------------------------------
### Added
- OTA update user guide in sphinx

### Changed
- python example file name: upip_install->mip_install

v0.0.14 Date: 2023/08/21, Developer: Chunglee_people
---------------------------------------------------
### Added
- Example code: Wifi connect & New package install

v0.0.13.1 Date: 2023/08/10, Developer: Chunglee_people
---------------------------------------------------
### Fixed
-  Fix website

v0.0.13 Date: 2023/08/10, Developer: Chunglee_people
---------------------------------------------------
### Added
-  Add example code and create sphinx.
