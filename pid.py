from matplotlib import pyplot as plt
from typing import Optional, Callable
from random import random


class ksys:
    def __init__(self, initialStat: float, errorFunc: Callable[[], float]):
        self.initialStat = initialStat
        self.errorFunc = errorFunc


class generalSystem:
    def __init__(self, k: ksys):
        self.status = k.initialStat
        self.errorFunc = k.errorFunc

    def control(self, force: float):
        self.status += force + self.errorFunc()

    def getStatus(self) -> float:
        return self.status


class kpid:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def __iter__(self):
        return (self.kp, self.ki, self.kd).__iter__()


class ctrllog:
    def __init__(self, expected):
        self._loglist = []
        self.expected = expected

    def append(self, stat: float, err: float, force: float):
        self._loglist.append({"stat": stat, "err": err, "force": force})

    def __len__(self) -> int:
        return len(self._loglist)

    def __iter__(self):
        for elem in self._loglist:
            yield elem

    def to_dict(self) -> dict[str, list[float]]:
        d = {}
        for item in self._loglist:
            for key, value in item.items():
                if key not in d:
                    d[key] = []
                d[key].append(value)
        return d

    def plot(self, keys: list[str] = ["stat", "expected"]):
        d = self.to_dict()
        if "expected" in keys:
            plt.plot([self.expected] * len(self), label="expected")
            keys = [k for k in keys if k != "expected"]
        for key, value in d.items():
            if key in keys:
                plt.plot(value, label=key)
        plt.show()


def pidController(
    system: generalSystem,
    expected: float,
    acceptableError: float,
    k: kpid,
) -> ctrllog:
    def error(system: generalSystem, expected):
        return expected - system.getStatus()

    kp, ki, kd = tuple(k)
    vp, vi, vd, lastvp = 0, 0, 0, 0
    log = ctrllog(expected)

    while abs(err := error(system, expected)) >= acceptableError:
        # calc
        vp = err
        vi += vp
        vd = vp - lastvp
        lastvp = vp

        # add
        oldstat = system.getStatus()
        force = kp * vp + ki * vi + kd * vd
        system.control(force)

        # log
        log.append(oldstat, err, force)

    return log


def crit(log: ctrllog) -> float:
    # smaller is better
    return len(log)


def trainPid(epochs: int, initial: Optional[kpid] = None) -> kpid:
    ktrained = initial if initial is not None else kpid(random(), random(), random())

    for _ in range(epochs):
        pass
    return ktrained


if __name__ == "__main__":
    expected = 40

    system = generalSystem(ksys(0, lambda: -10 + random() * 0.1))
    log = pidController(system, expected, 0.01, kpid(0.4, 0.2, 0.1))
    log.plot()
