import os
from pathlib import Path

import matplotlib.pyplot as plt


def _get_project_dir():
    # Get the current script file path
    current_script_path = Path(__file__)
    # Get the project directory
    parent_directory = current_script_path.parent.parent.parent

    return os.path.join(parent_directory, "assets/figures")


def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(_get_project_dir(), f"{fig_id}.{fig_extension}")
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)
