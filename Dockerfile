FROM python:3.8

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./toad_sp_command ./toad_sp_command
COPY ./run.sh ./run.sh

RUN mkdir ./config
VOLUME ./config

CMD ["./run.sh"]

# docker run --network=iotoad_network -v $(pwd)/config:/app/config toad_sp_command