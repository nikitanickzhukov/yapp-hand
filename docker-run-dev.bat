@echo off
set cwd=%~dp0
set vol=%cwd%app:/usr/local/app
echo %vol%

docker build --file Dockerfile-dev --tag yapp-hand:dev . && ^
docker run --rm --volume %vol% --publish 8020:80 --name yapp-hand-dev yapp-hand:dev
