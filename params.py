from dataclasses import dataclass

@dataclass
class TokamakParams:
    epsilon: float = 0.4
    kappa: float = 2
    delta: float = 0.75
    alfa: float = 50.0
    v : float = 1
    thickness: float = 5.0
    bend_radius: float = 0.5

    @property
    def R0(self) -> float:
        return self.alfa / self.epsilon

def coil_R0(vessel_params: TokamakParams) -> float:
    return vessel_params.R0   # same central axis — coil is concentric with the vessel

def coil_bore_radius(vessel_params: TokamakParams, gap: float) -> float:
    # how far out the coil's cross-section center sits, measured from R0
    return vessel_params.alfa + vessel_params.thickness + gap