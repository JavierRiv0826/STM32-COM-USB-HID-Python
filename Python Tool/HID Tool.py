import hid
import time

# -----------------------------
# 1️⃣ List HID devices
# -----------------------------
devices = hid.enumerate()

if not devices:
    print("No HID devices found")
    exit()

print("\nAvailable HID devices:")
for i, d in enumerate(devices):
    print(f"[{i}] VID={hex(d['vendor_id'])} "
          f"PID={hex(d['product_id'])} "
          f"Manufacturer={d['manufacturer_string']} "
          f"Product={d['product_string']}")

# -----------------------------
# 2️⃣ Select device
# -----------------------------
idx = int(input("\nSelect device number: "))
selected = devices[idx]

VID = selected['vendor_id']
PID = selected['product_id']

dev = hid.device()
dev.open(VID, PID)

print("\nDevice opened")
print("Manufacturer:", dev.get_manufacturer_string())
print("Product:", dev.get_product_string())

# -----------------------------
# 3️⃣ Choose operation
# -----------------------------
while True:
    mode = input("\nChoose mode (r = read, w = write): ").lower()

    # -----------------------------
    # 4️⃣ READ MODE
    # -----------------------------
    if mode == 'r':
        print("\nReading data (Ctrl+C to stop)...")
        dev.set_nonblocking(True)

        try:
            while True:
                data = dev.read(2)   # adjust report size
                if data:
                    print("Counter:", data[0], " Button: ",data[1])
                time.sleep(0.01)
        except KeyboardInterrupt:
            print("\nStopped")

    # -----------------------------
    # 5️⃣ WRITE MODE
    # -----------------------------
    elif mode == 'w':
        print("\nWrite mode (Ctrl+C to stop)")
        print("Sending: [ReportID, Value]")

        try:
            while True:
                value = int(input("LED 1(ON), 0(OFF): "))
                dev.write([0,value]) # Report ID = 0
        except KeyboardInterrupt:
            print("\nStopped")

    else:
        print("Invalid mode")

dev.close()
