## App Runbook
### See App In Container
1. Follow [Login to Docker Container](#login-to-docker-container) instructions
2. Change directory to where the app is stored: `cd /app`
3. To exit run `exit`

## Deploying Code Changes to Container
1. Make code change
2. Build changes into docker image:
	1. `docker compose build`
3. Start the cotnainer:
	1. `docker compose up`

## Container Runbook
### See Docker Container Logs
1. Get container id with `docker ps`
2. Print logs with `docker logs {container_id}`

### Login to Docker Container
1. Get container id with `docker ps`
2. Print logs with `docker exec -it {container_id} bash`

## Running scripts with `systemctl`
### home-automation-containers.service
Location: `/etc/systemd/system/home-automation-containers.service`

See Status: `systemctl status home-automation-containers.service`

Start: `systemctl start home-automation-containers.service`

### tv_controller_interface.service
Location: `/lib/systemd/system/tv_controller_interface.service`

See Status: `systemctl status tv_controller_interface.service`

Start: `systemctl start tv_controller_interface.service`

## Rough Design
![Design diagram](/diagrams/Alexa%20TV%20Controller%20Diagram.jpg)