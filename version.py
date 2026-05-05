from pathlib import Path

from win32api import HIWORD, LOWORD, GetFileVersionInfo


def get_dll_version(filename):
    info = GetFileVersionInfo(filename, "\\")
    ms = info["FileVersionMS"]
    ls = info["FileVersionLS"]
    return HIWORD(ms), LOWORD(ms), HIWORD(ls), LOWORD(ls)


if __name__ == "__main__":
    DNX64_PATH = Path(__file__).resolve().parent / "DNX64" / "DNX64.dll"
    major_v, minor_v, build_v, revision_v = get_dll_version(DNX64_PATH)
    print(f"DNX64.dll version: {major_v}.{minor_v}.{build_v}.{revision_v}")
