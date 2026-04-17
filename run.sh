#!/bin/bash

source .venv/bin/activate 2>log.txt
output=$(cat log.txt)
if echo "$output" | grep -q "No such file or directory"; then
    echo "install virtual environment..."
    python3 -m venv .venv
    echo "finished installing virtual environment"
fi

python3 scripts/main.py 2>log.txt
output=$(cat log.txt)

if echo "$output" | grep -q "ModuleNotFoundError"; then
	echo "installing modules..."
	source .venv/bin/activate
    pip install -r ./requirements.txt
    echo "finished installing modules:"
    pip list
	python3 scripts/main.py
    
    exit;
fi
cat log.txt
