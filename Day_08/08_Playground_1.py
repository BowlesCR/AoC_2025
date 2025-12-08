import fileinput
import math
from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True)
class Box:
    x: int
    y: int
    z: int

    def distance(self: Box, other: Box):
        return math.sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )


class Circuits:
    def __init__(self, boxes: set[Box]):
        self.circuits: list[set[Box]] = [{box} for box in boxes]

    def _find_circuit(self, box: Box) -> set[Box] | None:
        for circuit in self.circuits:
            if box in circuit:
                return circuit
        return None

    def connect_boxes(self, a: Box, b: Box):
        circuit_a = self._find_circuit(a)
        circuit_b = self._find_circuit(b)
        if circuit_a != circuit_b:
            circuit_a.update(circuit_b)
            self.circuits.remove(circuit_b)

    def get_lengths(self) -> list[int]:
        return sorted([len(circuit) for circuit in self.circuits], reverse=True)


boxes: set[Box] = set()

for line in fileinput.input():
    boxes.add(Box(*map(int, line.rstrip().split(","))))
del line

distances: set[tuple[float, Box, Box]] = set()

for combo in combinations(boxes, 2):
    distances.add((combo[0].distance(combo[1]), combo[0], combo[1]))
del combo

pairs: list[tuple[float, Box, Box]] = sorted(distances, key=lambda x: x[0])[:1000]
del distances

circuits = Circuits(boxes)

for _, a, b in pairs:
    circuits.connect_boxes(a, b)

print(math.prod(circuits.get_lengths()[:3]))
