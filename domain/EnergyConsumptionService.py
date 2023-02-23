from port.IEnergyInfoPort import IEnergyInfoPort
from domain.model.ConsumptionData import ConsumptionData


class EnergyConsumptionService(IEnergyInfoPort):
    def __init__(self) -> None:
        self._consumption_data = None
        self._consumed_energy(16000, 240, 7200)

    @property
    def consumed_energy(self) -> ConsumptionData:
        return self._consumption_data

    def _consumed_energy(self, milli_amps, volt, elapsed_seconds) -> None:
        self._consumption_data = ConsumptionData(milli_amps, volt, elapsed_seconds)
