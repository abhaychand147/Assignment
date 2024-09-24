import click
from core.waveform import Waveform


@click.command()
@click.option(
    "--raise-time",
    prompt="Please provide raise time duration",
    type=float,
    help="Raise Time",
)
@click.option(
    "--fall-time",
    prompt="Please provide fall time duration",
    type=float,
    help="Fall Time",
)
@click.option("--period", prompt="Please provide period", type=int, help="Period")
@click.option(
    "--pulse-width", prompt="Please provide pulse width", type=float, help="Pulse Width"
)
@click.option(
    "--output-path",
    prompt="Please provide output path and file name in for csv file",
    default="result/waveform_out.csv",
    type=str,
    help="Output path for saving waveform result. Path should \
        be in out_path/out_filename.csv format",  # NOQA: E501
)
@click.option(
    "--show-plot",
    default=False,
    type=bool,
    prompt="Do you want to see plot as well?",
    help="If you want to see the plot",
)
def get_waveform(
    raise_time: float,
    fall_time: float,
    pulse_width: float,
    period: int,
    output_path: str,
    show_plot: bool,
) -> None:
    """This function calls core function to generate waveform
    based on the specified arguements.

    Args:
        raise_time (float): Duration for waveform to rise from 10% to 90% of amplitude.
        fall_time (float):  Duration for waveform to fall from 90% back to 10% of amplitude.
        pulse_width (float): Duration between 50% rise to 50% down.
        period (float): total time taken for one complete cycle of the waveform.
        output_path (str): Output Path to write generated waveform.
            <output_path>/<output_filename>.csv
        show_plot (bool): If you want to generate a plot. Defaults to False.
    Returns:
        None.
    """
    waveform_obj = Waveform(raise_time, fall_time, pulse_width, period, output_path)
    waveform_obj.generate_waveform()

    if show_plot:
        waveform_obj.activatePlot()


if __name__ == "__main__":
    """Calling get_waveform function
    """
    get_waveform()
