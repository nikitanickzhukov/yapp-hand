docker build --file Dockerfile --tag yapp-hand:prod . && ^
docker run --publish 8020:80 --name yapp-hand-prod yapp-hand:prod
