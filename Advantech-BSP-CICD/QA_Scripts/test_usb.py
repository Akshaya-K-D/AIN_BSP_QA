import os

def test_usb():
    # On Linux/Android boards, USB devices usually show in /dev or /storage
    usb_path = "/dev/bus/usb"
    assert os.path.exists(usb_path), f"USB devices not detected at {usb_path}"

if __name__ == "__main__":
    try:
        test_usb()
        print("USB test passed")
    except AssertionError as e:
        print("NO", e)
        exit(1)