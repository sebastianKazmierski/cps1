import numpy as np
import math
from signals.signal import Signal
from signal_generators2.signal_generator import SignalGenerator
from enums.signal_parameters import SignalParameters
from enums.signal_type import SignalType
from enums.type_of_periodical import SignalPeriodic


class SinStraightenedInTwoHalf(SignalGenerator):
    def generate(self, amplitude: float, start_time: float, duration: float, period: float,
                 sampling_frequency: float) -> Signal:
        x = self.get_arguments(start_time, duration, sampling_frequency)

        y = amplitude * abs(np.sin(((2 * math.pi) / period) * (x - start_time)))

        return Signal(start_time, 1 / period, sampling_frequency, y, SignalType.REAL, SignalPeriodic.YES)

    def get_name(self) -> str:
        return "Sygnał sinusoidalny wyprostowany dwupołówkowo"

    def get_list_required_parameters(self):
        return [SignalParameters.AMPLITUDE, SignalParameters.START_TIME, SignalParameters.DURATION,
                SignalParameters.PERIOD, SignalParameters.SAMPLING_FREQUENCY]
