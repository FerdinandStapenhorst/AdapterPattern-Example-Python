from domain.EnergyConsumptionService import EnergyConsumptionService
from adapter.EvConsumption.EvEnergyAdapter import EvEnergyAdapter
from adapter.Consumption.EnergyAdapter import EnergyAdapter

# Instance of the EnergyInfo port
energy_info_port = EnergyConsumptionService()

# Instance of the EnergyInfo Adapter injecting the port interface
# We can get the energy in three separate elements:milli amps, volt, and elapsed seconds
energy_info_adapter = EnergyAdapter(energy_info_port)
print(energy_info_adapter.to_string())

# Instance of the EvEnergyInfo Adapter injecting the port interface
# We now can get the consumed energy in kWh
ev_energy_info_adapter = EvEnergyAdapter(energy_info_port)
print(ev_energy_info_adapter.to_string())

