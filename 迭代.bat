@echo off
set a=1
start /wait /b starting.py

for /l %%j in (1,1,%a%) do (

start /wait /b clear_record.py
for /l %%i in (1,1,6) do (
newkf.exe < input_apc.txt > output.txt
start /wait /b record_change_card.py
)
start /wait /b rank.py
newkf.exe < input_rank.txt > output.txt
start /wait /b pool.py

)
