import sys

if (
    (sys.version_info.major != 3)
    or (sys.version_info.minor != 14)
    or (sys.version_info.micro != 2)
):
    print("Incorrect Python version")
    print(sys.version)
else:
    print("Correct Python version")
