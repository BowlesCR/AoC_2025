import fileinput
import itertools
import re

re_first = re.compile(r"^\[(?P<lights>[.#]+)] (?P<wiring>\([0-9(), ]+\)) \{(?P<joltage>[0-9,]+)}$")
re_wiring = re.compile(r"\(([0-9,]+)\)")


class Machine:
    def __init__(self, lights: int, buttons: list[int]) -> None:
        self.lights = lights
        self.buttons = buttons

    def configure(self) -> int:
        for i in range(1, len(self.buttons) + 1):
            for combo in itertools.combinations(self.buttons, i):
                check = 0
                for button in combo:
                    check ^= button
                if check == self.lights:
                    return i
        return -1


def main():
    presses = 0
    for line in fileinput.input():
        matches = re_first.match(line)
        del line

        lights = int("".join("1" if x == "#" else "0" for x in matches.group("lights")), 2)
        num_lights = len(matches.group("lights"))

        wiring = re_wiring.findall(matches.group("wiring"))
        buttons: list[int] = []
        for w in wiring:
            button = 0
            for bit in [int(x) for x in w.split(",")]:
                button += 1 << num_lights - bit - 1
            buttons.append(button)

        presses += Machine(lights, buttons).configure()
    print(presses)


if __name__ == "__main__":
    main()
