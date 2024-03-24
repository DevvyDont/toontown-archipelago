#!/bin/sh
cd ..


MAX_CHANNELS=999999
STATE_SERVER=4002
ASTRON_IP="127.0.0.1:7199"
EVENT_LOGGER_IP="127.0.0.1:7197"
BASE_CHANNEL=401000000
DISTRICT_NAME="Toon Valley"

python3 -m pip install -r requirements.txt

while true
do
    python3 -m toontown.ai.AIStart --base-channel ${BASE_CHANNEL} \
               --max-channels ${MAX_CHANNELS} --stateserver ${STATE_SERVER} \
               --astron-ip ${ASTRON_IP} \
               --eventlogger-ip ${EVENT_LOGGER_IP} --district-name "${DISTRICT_NAME}"
    sleep 5
done
