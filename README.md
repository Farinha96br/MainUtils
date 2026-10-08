# MainUtils

Tools, templates and notes I use day to day.

## Contents

| Path | What it is |
| --- | --- |
| `Templates/matplotlib/` | Small, self-contained matplotlib examples (line, scatter, bar, histogram, heatmap, contour, 3D surface, animation, ...) sharing the same serif / LaTeX-like style. |
| `Templates/xournal.xopp` | Blank Xournal++ notebook template. |
| `Templates/text.txt` | Empty text file template. |
| `copyTemplates.sh` | Copies everything in `Templates/` into the system templates folder, so the files show up in the file manager's "New Document" menu. |
| `apptainer/data-processing.def` | Python 3.11 container with numpy, pandas, matplotlib, Jupyter Notebook and gnuplot. |
| `apptainer/formatting.def` | Python container that formats code with isort + black. |
| `posReset.sh` | Post-install setup script for a fresh Ubuntu (apt/snap packages: LaTeX, OBS, VLC, GSL, Boost, ...). |

## Usage

### Templates

```bash
./copyTemplates.sh
```

The destination is resolved automatically (`XDG_TEMPLATES_DIR`, `xdg-user-dir`, or a localised folder such as `~/Modelos`), falling back to `~/Templates`.

### Apptainer images

Build from inside `apptainer/`:

```bash
cd apptainer
mkdir -p sif
apptainer build sif/data-processing.sif data-processing.def
apptainer build sif/formatting.sif formatting.def
```

Run:

```bash
# Jupyter Notebook on port 49173
apptainer run sif/data-processing.sif

# format files/directories with isort, then black
apptainer run sif/formatting.sif <paths>
```

### Post-install setup

```bash
sudo bash posReset.sh
```
