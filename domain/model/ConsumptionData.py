class ConsumptionData:
    def __init__(self, milli_amps, volt, elapsed_seconds):
        self._milli_amps = milli_amps
        self._volt = volt
        self._elapsed_seconds = elapsed_seconds

    @property
    def milli_amps(self) -> int:
        return self._milli_amps

    @milli_amps.setter
    def milli_amps(self, value) -> None:
        self._milli_amps = value

    @property
    def volt(self) -> int:
        return self._volt

    @volt.setter
    def volt(self, value) -> None:
        self._volt = value

    @property
    def elapsed_seconds(self) -> int:
        return self._elapsed_seconds

    @elapsed_seconds.setter
    def elapsed_seconds(self, value) -> None:
        self._elapsed_seconds = value
