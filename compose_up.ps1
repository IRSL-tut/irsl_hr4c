# power-shell script for launching docker-compose

$scriptPath = $MyInvocation.MyCommand.Path
# echo $scriptPath

$scrdir = Split-Path -Parent $scriptPath
$compfile = $scrdir + "\docker\docker-compose-win2.yaml"
# echo $scrdir
# echo $compfile

docker compose -f $compfile up

pause
