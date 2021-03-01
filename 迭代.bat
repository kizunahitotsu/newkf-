@echo off
set a=1
for /l %%j in (1,1,%a%) do (

for /l %%i in (1,1,5) do (
newkf.exe < input_apc.txt > output.txt
start /wait /b record.py
start /wait /b change_card.py
)
start /wait /b rank.py
newkf.exe < input_rank.txt > output.txt
start /wait /b pool.py

)