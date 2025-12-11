import fileinput
import re


class Rack:
    def __init__(self, devices: dict[str, set[str]]) -> None:
        self.devices = devices
        self.paths = 0

    def search(self, path: list[str]) -> None:
        device = path[-1]
        for next_device in self.devices[device]:
            assert next_device not in path
            if next_device == "out":
                self.paths += 1
                continue
            self.search(path + [next_device])


def main():
    devices: dict[str, set[str]] = {}

    for line in fileinput.input():
        matches = re.findall(r"\w{3}", line)
        devices[matches[0]] = set(matches[1:])

    rack = Rack(devices)
    rack.search(["you"])
    print(rack.paths)


if __name__ == "__main__":
    main()
