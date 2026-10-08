# MainUtils

Tools, templates and notes I use day to day.

## Contents

| Path | What it is |
| --- | --- |
| `Templates/` | File templates (matplotlib plots, Xournal++, text) |
| `copyTemplates.sh` | Installs the templates for the file manager |
| `apptainer/` | Containers for data processing and code formatting |
| `posReset.sh` | Ubuntu post-install setup |

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
