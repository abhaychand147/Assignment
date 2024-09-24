import numpy as np
from matplotlib import pyplot as pt


class Waveform:
    amplitude = 1
    showPlot = False

    def __init__(
        self,
        raise_time: float,
        fall_time: float,
        pulse_width: float,
        period: int,
        output_path: str,
    ):
        self.raise_time = raise_time
        self.fall_time = fall_time
        self.pulse_width = pulse_width
        self.period = period
        self.output_path = output_path

    def activatePlot(self):
        Waveform.showPlot = True

    def generate_waveform(self):
        if Waveform.showPlot:
            self.generate_plot()
        pass

    def generate_plot(self):
        pass
