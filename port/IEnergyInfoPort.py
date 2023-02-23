
from domain.model import ConsumptionData


class IEnergyInfoPort:    

    def consumed_energy(self) -> ConsumptionData:
        raise NotImplementedError
