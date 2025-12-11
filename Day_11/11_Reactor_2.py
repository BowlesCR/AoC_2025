import fileinput
import re
from functools import lru_cache


class Rack:
    def __init__(self, devices: dict[str, set[str]]) -> None:
        self.devices = devices

    @lru_cache(maxsize=None)
    def search(self, device: str) -> tuple[int, int, int, int]:
        paths_none = 0
        paths_dac = 0
        paths_fft = 0
        paths_fft_dac = 0
        for next_device in self.devices[device]:
            if next_device == "out":
                paths_none += 1
                continue
            t = self.search(next_device)
            if next_device == "dac":
                paths_dac += t[0] + t[1]
                paths_fft_dac += t[2]
            elif next_device == "fft":
                paths_fft += t[0] + t[2]
                paths_fft_dac += t[1]
            else:
                paths_none += t[0]
                paths_dac += t[1]
                paths_fft += t[2]
                paths_fft_dac += t[3]
        return (paths_none, paths_dac, paths_fft, paths_fft_dac)


def main():
    devices: dict[str, set[str]] = {}

    for line in fileinput.input():
        matches = re.findall(r"\w{3}", line)
        devices[matches[0]] = set(matches[1:])

    rack = Rack(devices)
    print(rack.search("svr")[3])


if __name__ == "__main__":
    main()
