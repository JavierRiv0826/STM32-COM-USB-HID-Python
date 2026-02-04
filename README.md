# ♆ STM32 USB-HID + Python

📌 Description
This project demonstrates a custom USB HID device implemented on the STM32F103C6 (Bluepill) using STM32CubeMX + HAL.
A Python (hidapi) tool is provided to communicate with the device from a PC.

This is a vendor-defined HID device (not mouse/keyboard), so it is safe to connect without affecting OS input behavior.

---

## 🚀 Features

- ✔ HID IN report (device → PC):  2 Byte counter
- ✔ Periodic Tick: Sends "Tick" message every 1 second as a simple timer example. (1st IN byte)
- ✔ Implemented button input. (2nd IN byte)
- ✔ HID OUT report (PC → device): 1‑byte command
- ✔ LED control via HID OUT report.
- ✔ PC communication using Python + hidapi

## 📦 USB Descriptor Summary
- HID Report Descriptor (Vendor Defined)
- Usage Page: 0xFF00 (Vendor)
- IN report: 2 bytes
- OUT report: 1 byte
- This descriptor is defined in:
```bash
Middlewares/STM32_USB_Device_Library/Class/HID/Src/usbd_hid.c
```
- And the reception control in funtion:
*USBD_HID_DataOut*

⚠️ Important Note About OUT Reports (Read This)
Although the OUT report payload is 1 byte, the host (Python hidapi) always sends a Report ID byte, report ID is ignored at reception.
Therefore in python side:
```bash
dev.write([0, value]) # Report ID + payload
```

## 🔄 Clock
- HSE = 8 MHz
- PLL ×9 → SYSCLK = 72 MHz
- USB clock = 48 MHz (mandatory for USB FS)

## ♆ USB Device
- Connectivity → USB_DEVICE → Device (FS)
- Middleware → USB_DEVICE → Class: HID (Human Interface Device)
## ↔️ GPIO
- PA11 → USB_DM
- PA12 → USB_DP

## 🖥️ PC‑Side Python Requirements
```bash
pip install hidapi
```
---
## 💡 How to Run 🧪

### 1. Clone the Repository
```bash
git clone https://github.com/JavierRiv0826/STM32-COM-USB-HID-Python.git
```
### 2. Open in STM32CubeIDE
- File → Open Projects from File System  
- Select the project folder

### 3. Build the Project
Press **Ctrl + B**  
or  
Project → Build Project

### 4. Flash the Microcontroller
- Connect ST-Link or USB-to-Serial (bootloader mode)
- Press **Debug** or **Run*

### 5. Connect a data USB cable to the Bluepill USB port.
### 6. Run the Python tool:
```bash
python HID_Tool.py
```
### 7. Select your  HID device (usually [0]):
```bash
VID=0x0483 PID=0x572B
Manufacturer: Xavi Embedded Lab
```
### 8. Choose mode read/write.
### 9. When "read" → "Tick" messages appear every second  + button state
### 10. When "write" → Send 0 or 1 to control LED
---
## 🗝️ Key Code Snippets
### Make hUsbDeviceFS visible globally
Add at the end of usb_device.h:
```bash
extern USBD_HandleTypeDef hUsbDeviceFS;
```
### Customize Manufacturer String:
Edit in usbd_desc.c:
```bash
#define USBD_MANUFACTURER_STRING     "Xavi Embedded Lab"
```
---
## 🧩 Hardware Overview

### **Microcontroller**
- STM32F103C6
- ARM Cortex-M3 @ 72 MHz  
- 64 KB Flash, 20 KB RAM  
- USB: Full-speed device (PA11 = USB_DM, PA12 = USB_DP)
- Power: USB only (avoid connecting ST-Link 5V simultaneously)

### **Clock Configuration**
- HSE: 8 MHz external crystal  
- SYSCLK: 72 MHz  
- AHB: 72 MHz  
- APB1: 36 MHz  
- APB2: 72 MHz  
- USB clock = 48 MHz
---

## 🛠 Development Tools
- **STM32CubeIDE**
- **STM32CubeMX**
- **Git & GitHub**
- **Python: For testing HID IN/OUT reports**

---

## 📂 Project Structure
/Core

/Inc → Header files

/Src → Main application source files
/Drivers → HAL drivers provided by STM32CubeMX
/Middlewares → USB descriptors & logic
/USB_DEVICE →  USB Parameter Settings
/Python Tool →  Python HID tool script
/STM32F103C6.ioc → CubeMX project file
README.md → Project description

---

## 👤 Author
**Javier Rivera**  
GitHub: *JavierRiv0826*
