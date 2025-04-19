import usb_hid

GAMEPAD_REPORT_DESCRIPTOR = bytes((
    0x05, 0x01,       # Usage Page (Generic Desktop)
    0x09, 0x05,       # Usage (Game Pad)
    0xA1, 0x01,       # Collection (Application)
    0x85, 0x04,       # Report ID 4
    0x05, 0x09,       #   Usage Page (Button)
    0x19, 0x01,       #   Usage Minimum (1)
    0x29, 0x10,       #   Usage Maximum (16)
    0x15, 0x00,       #   Logical Minimum (0)
    0x25, 0x01,       #   Logical Maximum (1)
    0x75, 0x01,       #   Report Size (1)
    0x95, 0x10,       #   Report Count (16)
    0x81, 0x02,       #   Input (Data,Var,Abs)
    0x05, 0x01,       #   Usage Page (Generic Desktop)
    0x15, 0x81,       #   Logical Minimum (-127)
    0x25, 0x7F,       #   Logical Maximum (127)
    0x09, 0x30,       #   Usage X
    0x09, 0x31,       #   Usage Y
    0x09, 0x32,       #   Usage Z
    0x09, 0x35,       #   Usage Rz
    0x75, 0x08,       #   Report Size (8)
    0x95, 0x04,       #   Report Count (4)
    0x81, 0x02,       #   Input (Data,Var,Abs)
    0xC0              # End Collection
))

gamepad = usb_hid.Device(
    report_descriptor=GAMEPAD_REPORT_DESCRIPTOR,
    usage_page=0x01,           # Generic Desktop
    usage=0x05,                # Gamepad
    report_ids=(4,),
    in_report_lengths=(6,),
    out_report_lengths=(0,)
)

usb_hid.enable((gamepad,))
