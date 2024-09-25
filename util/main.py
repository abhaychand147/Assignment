import click
from core.waveform import Waveform


class PositiveFloat(click.ParamType):
    name = "positive float"

    def convert(self, value, param, ctx):
        try:
            float_value = float(value)
            if float_value <= 0:
                raise click.BadParameter("Must be a positive value.")
            return float_value
        except ValueError:
            self.fail(f"{value} is not a valid float.")


@click.command()
@click.option(
    "--rise-time",
    prompt="Rise Time (Must be greater than zero)",
    type=PositiveFloat(),
    help="Rise Time",
)
@click.option(
    "--fall-time",
    prompt="Fall time (Must be greater than zero)",
    type=PositiveFloat(),
    help="Fall Time",
)
@click.option(
    "--period", prompt="Period", type=PositiveFloat(), help="Period"
)  # NOQA: E501
@click.option(
    "--pulse-width",
    prompt="Pulse Width",
    type=PositiveFloat(),
    help="Pulse Width",  # NOQA: E501
)
@click.option(
    "--output-path",
    prompt="Output Path (folder/filename.csv)",
    default="result",
    type=str,
    help="Output path directory for saving waveform result.",
)
@click.option(
    "--show-plot",
    default=False,
    type=bool,
    prompt="Do you want to see plot as well?",
    help="If you want to see the plot",
)
def get_waveform(
    rise_time: float,
    fall_time: float,
    pulse_width: float,
    period: int,
    output_path: str,
    show_plot: bool,
) -> None:
    """This function calls core function to generate waveform
    based on the specified arguements.

    Args:
        rise_time (float): Duration for waveform to rise
            from 10% to 90% of amplitude.
        fall_time (float):  Duration for waveform to fall
          from 90% back to 10% of amplitude.
        pulse_width (float): Duration between 50% rise to 50% down.
        period (float): total time taken for one complete cycle of the waveform.
        output_path (str): Output Path Directory to write generated waveform.
            <output_path>
        show_plot (bool): If you want to generate a plot. Defaults to False.
    Returns:
        None.
    """
    for param_name, param in zip(
        ["rise_time", "fall_time", "pulse_width", "period"],
        [rise_time, fall_time, pulse_width, period],
    ):
        if param <= 0:
            raise ValueError(f"{param_name} should be positive!")

    waveform_obj = Waveform(rise_time, fall_time, pulse_width, period, output_path)

    # Setting showplot
    if show_plot:
        waveform_obj.activatePlot()

    # calling generate waveform
    waveform_obj.generate_waveform()


if __name__ == "__main__":
    """Calling get_waveform function"""
    get_waveform()
