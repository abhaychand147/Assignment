from setuptools import setup, find_packages

setup(
    name="generate_waveform",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Click",
        "numpy",
        "matplotlib",
    ],
    entry_points="""
        [console_scripts]
        generate_waveform=util.main:get_waveform
    """,
)
