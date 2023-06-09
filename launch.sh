#!/bin/bash

n=1  # Nombre de niveaux à remonter à partir du répertoire courant

current_directory=$(pwd)
parent_directory=$current_directory

for ((i=1; i<=$n; i++))
do
  parent_directory=$(dirname "$parent_directory")
done

menu_py_path=$(find "$parent_directory" -type f -name "menu.py" -path "*/services/*")

if [[ -n "$menu_py_path" ]]; then
  research_dir=$(dirname "$menu_py_path")
  cd "$research_dir" || exit 1
  chmod +x menu.py  # Changer les permissions pour le rendre exécutable
  python3 menu.py
fi
