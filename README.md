# YAPP Hand
A microservice responsible for hands' identification

## User story
- identify hero's hand by game, pocket and board cards

## Implementation
- Gunicorn Web Server: https://gunicorn.org/
- Falcon Web Framework: https://falconframework.org/
- Andrew Prock's pokerstove library: https://github.com/andrewprock/pokerstove (with minor additions)

## Deployment
- `./docker-run.bat` - building and running container for production
- `./docker-run-dev.bat` - building and running container for development (direct code mounting, hot reload)

## API docs
http://localhost:8020/v1/docs

## Dependencies
No
