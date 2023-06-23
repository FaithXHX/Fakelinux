@echo off
setlocal EnableDelayedExpansion

set "characters=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
set "length=10"
set "outputFile=output.txt"

:generate
set "result=discord.gift/"
for /L %%i in (1,1,%length%) do (
    set /A "randomIndex=!random! %% 62"
    for /F %%j in ("!randomIndex!") do (
        set "randomChar=!characters:~%%j,1!"
        set "result=!result!!randomChar!"
    )
)

set /A "randomNumber=!random! %% 10"
if !randomNumber! lss 2 (
    set "result=[working]!result!"
) else (
    set "result=[not working]!result!"
)

echo %result% >> %outputFile%
echo %result%
goto generate
