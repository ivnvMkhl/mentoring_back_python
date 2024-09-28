#!/bin/bash

cp -i /root/mentor_app/bin/_resources/mentor_hub.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable mentor_hub.service
systemctl start mentor_hub.service