#!/usr/bin/env bash
# copy everything under ./Templates into the ubuntu templates folder,
# so the files show up in the file manager's "New Document" menu.
# the folder is localised (Templates, Modelos, Plantillas, Modeles, Vorlagen, ...),
# so the name is resolved from the system instead of hardcoded
set -euo pipefail

src="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/Templates"

# 1. explicit environment override
dest="${XDG_TEMPLATES_DIR:-}"

# 2. ask xdg (returns $HOME when the entry is unset, which is not an answer)
if [ -z "$dest" ] && command -v xdg-user-dir >/dev/null; then
    dest="$(xdg-user-dir TEMPLATES)"
    if [ "$dest" = "$HOME" ]; then
        dest=""
    fi
fi

# 3. read the config file directly, in case xdg-user-dirs is not installed
conf="${XDG_CONFIG_HOME:-$HOME/.config}/user-dirs.dirs"
if [ -z "$dest" ] && [ -f "$conf" ]; then
    line="$(grep -m1 '^[[:space:]]*XDG_TEMPLATES_DIR=' "$conf" || true)"
    if [ -n "$line" ]; then
        eval "dest=${line#*=}"  # the value is written as "$HOME/yyy"
    fi
fi

# 4. no config at all: pick up a localised folder if one already exists
if [ -z "$dest" ]; then
    for name in Templates Modelos Plantillas Modèles Vorlagen Modelli Sjablonen \
                Szablony Mallar Mallit Шаблоны Şablonlar Πρότυπα 模板 テンプレート 템플릿; do
        if [ -d "$HOME/$name" ]; then
            dest="$HOME/$name"
            break
        fi
    done
fi

# 5. nothing found, create the untranslated default
dest="${dest:-$HOME/Templates}"

mkdir -p "$dest"
cp -rv "$src"/. "$dest"/
echo "templates copied to $dest"
