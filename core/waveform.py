"""Module to generate waveform
"""

import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as pt


class Waveform:
    amplitude = 1
    showPlot = False

    def __init__(
        self,
        rise_time: float,
        fall_time: float,
        pulse_width: float,
        period: int,
        output_path: str,
    ):
        self.rise_time = rise_time
        self.fall_time = fall_time
        self.pulse_width = pulse_width
        self.period = period
        self.output_path = output_path

    def activatePlot(self):
        """Set showPlot class variable.
        Default value is set as False.
        """
        Waveform.showPlot = True

    def calculate_pulse_width_at_max_amplitude(self) -> float:
        """Calculate the pulse width at the
        maximum amplitude. In this case, amplitude is 1.

        Returns:
            float: pulse width at maximum aplitude
        """
        rise_time_50_to_100 = (self.rise_time / 0.8) * 0.5
        fall_time_100_to_50 = (self.fall_time / 0.8) * 0.5
        pulse_width_at_max_amp = self.pulse_width - (
            rise_time_50_to_100 + fall_time_100_to_50
        )

        return pulse_width_at_max_amp

    def generate_waveform(self):
        """Generate the waveform based on rise time,
        fall time, period, pulse width and amplitude.
        """
        rise_end_time = self.rise_time / 0.8
        full_fall_time = self.fall_time / 0.8

        pulse_width_at_max_amp = self.calculate_pulse_width_at_max_amplitude()

        fall_start_time = pulse_width_at_max_amp + rise_end_time
        fall_end = fall_start_time + self.fall_time / 0.8

        # Time Array
        time_arr = np.linspace(0, self.period, 1000)

        # Initialize waveform array
        waveform = np.zeros_like(time_arr)

        try:
            for iter in range(len(time_arr)):
                if time_arr[iter] < rise_end_time:
                    waveform[iter] = (
                        time_arr[iter] / rise_end_time
                    ) * Waveform.amplitude  # NOQA: E501
                elif time_arr[iter] < fall_start_time:
                    waveform[iter] = Waveform.amplitude
                elif time_arr[iter] < fall_end:
                    waveform[iter] = (
                        Waveform.amplitude
                        - ((time_arr[iter] - fall_start_time) / full_fall_time)
                        * Waveform.amplitude
                    )
                else:
                    waveform[iter] = 0
        except Exception as err:
            raise RuntimeError("Failed to generate the waveform!") from err

        self.write_waveform_output(self.output_path, waveform, time_arr)
        if Waveform.showPlot:
            self.generate_plot(time_arr, waveform)

    @staticmethod
    def write_waveform_output(output_path: str, waveform: np.array, time_arr: np.array):
        """Write waveform output to specified output path.

        Args:
            output_path (str): Path to write the output.
            waveform (np.array): Waveform array
        """
        waveform_df = pd.DataFrame({"time": time_arr, "amplitude": waveform})

        if not os.path.exists(output_path):
            os.mkdir(output_path)
        output_path = os.path.join(output_path, "waveform_out.csv")
        waveform_df.to_csv(output_path, index=False)

    @staticmethod
    def generate_plot(time_arr: np.array, waveform: np.array):
        """Generate the wavefrom plot.
        This method can be called if you have time array and
        waveform array and can be used to generate the plot.

        Args:
            time_arr (np.array): Time Array
            waveform (np.array): Waveform Array
        """
        pt.plot(time_arr, waveform)
        pt.title("Waveform")
        pt.xlabel("Time")
        pt.ylabel("Amplitude")
        pt.grid(True)
        pt.show()
