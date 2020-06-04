FROM python:3.8-alpine

WORKDIR /usr/local

RUN apk add build-base boost-dev cmake git && \
    git clone https://github.com/andrewprock/pokerstove.git

COPY ./pokerstove/ps-id /usr/local/pokerstove/src/programs/ps-id
RUN echo "add_subdirectory(programs/ps-id)" >> /usr/local/pokerstove/src/CMakeLists.txt && \
    echo "add_subdirectory(ps-id)" >> /usr/local/pokerstove/src/programs/CMakeLists.txt

RUN mkdir pokerstove/build && \
    cd pokerstove/build && \
    cmake -DCMAKE_BUILD_TYPE=Release .. && \
    make && \
    make test

ENV PATH="/usr/local/pokerstove/build/bin:${PATH}"

COPY ./app /usr/local/app
WORKDIR /usr/local/app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install gunicorn

EXPOSE 80

CMD python -m unittest discover test && \
    gunicorn application.startup:api \
        --bind=0.0.0.0:80 \
        --workers=4 \
        --log-level info
