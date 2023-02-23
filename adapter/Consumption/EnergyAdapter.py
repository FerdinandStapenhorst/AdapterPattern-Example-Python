from adapter.Consumption.IEnergyAdapter import IEnergyAdapter

class EnergyAdapter(IEnergyAdapter):
    def __init__(self, energy_info_port) -> None:
        self._energy_info_port = energy_info_port
        
    def to_string(self) -> str:
        amps = self._energy_info_port.consumed_energy.milli_amps
        volt = self._energy_info_port.consumed_energy.volt
        seconds = self._energy_info_port.consumed_energy.elapsed_seconds
        return f"Consumed {amps}mA at {volt}V for {seconds} seconds."