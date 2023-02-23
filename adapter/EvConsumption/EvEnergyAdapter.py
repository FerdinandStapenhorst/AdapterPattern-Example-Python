from adapter.EvConsumption.IEvEnergyAdapter import IEvEnergyAdapter

class EvEnergyAdapter(IEvEnergyAdapter):
    def __init__(self, energy_info_port) -> None:
        self._energy_info_port = energy_info_port

    def to_string(self) -> str:
        kwh = self._calculate_kwh()
        return f"Consumed {kwh}kWh"

    def _calculate_kwh(self) -> float:
        sec = self._energy_info_port.consumed_energy.elapsed_seconds
        if sec <= 0:
            return 0.0

        hours = self._energy_info_port.consumed_energy.elapsed_seconds / 3600
        ampere = self._energy_info_port.consumed_energy.milli_amps / 1000
        kwh = ampere * self._energy_info_port.consumed_energy.volt / 1000 / hours
        return kwh
