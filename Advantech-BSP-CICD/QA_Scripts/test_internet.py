import subprocess

def test_internet():
    try:
        # Ping Google DNS
        subprocess.check_call(["ping", "-c", "3", "8.8.8.8"])
    except subprocess.CalledProcessError:
        raise AssertionError("Internet connectivity test failed")

if __name__ == "__main__":
    try:
        test_internet()
        print("Internet test passed ✅")
    except AssertionError as e:
        print("❌", e)
        exit(1)