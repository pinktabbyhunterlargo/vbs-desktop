#!/bin/bash
export inst-dir=$(pwd)
aplay files/*.mp3
export ran=$(ls settings)

if [ "$ran" = "base" ]; then
	export ran=0
	python3 apptest.py
	touch settings/firstrun
else
	export ran=1
fi

python3 vine_boom_sfx.pdf.exe.py.sh.py

