#!/bin/bash
DB_PUBLIC_PORT=5432 APP_PUBLIC_PORT=8080 docker compose -f ./docker_compose.yml up --build -d