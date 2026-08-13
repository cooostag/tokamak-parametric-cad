from dataclasses import dataclass

@dataclass
class TokamakParams:
    epsilon: float = 0.4
    kappa: float = 2
    delta: float = 0.75
    alfa: float = 50.0
    v = 1
    thickness: float = 5.0
    bend_radius: float = 0.5

    @property
    def R0(self) -> float:
        return self.alfa / self.epsilon