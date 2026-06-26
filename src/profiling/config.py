from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class ProfilingConfig:

    output_directory: Path = Path("artifacts/profiles")

    save_csv: bool = True

    save_json: bool = True

    save_plots: bool = True

    save_reports: bool = True

    image_dpi: int = 300

    figure_width: int = 12

    figure_height: int = 7

    top_n_classes: int = 20

    random_state: int = 42