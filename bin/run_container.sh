#!/bin/bash

if [ "$1" ]; then 
  DB_PUBLIC_PORT=5432 APP_PUBLIC_PORT=8080 docker compose -f $1/docker_compose.yml up --build -d
else
  DB_PUBLIC_PORT=5432 APP_PUBLIC_PORT=8080 docker compose -f ./docker_compose.yml up --build -d
fi

