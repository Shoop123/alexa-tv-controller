start: copy-systemctl-files start-systemctl
	@echo "Started services"

stop: stop-systemctl
	@echo "Stopped services"

start-systemctl:
	@echo "Starting systemctl services..."
	systemctl start home-automation-containers.service
	systemctl start tv_controller_interface.service

stop-systemctl:
	@echo "Stopping systemctl services..."
	systemctl stop home-automation-containers.service
	systemctl stop tv_controller_interface.service

copy-systemctl-files:
	@echo "Copying systemctl files..."
	cp systemctl_scripts/home-automation-containers.service /etc/systemd/system/home-automation-containers.service
	cp systemctl_scripts/tv_controller_interface.service /lib/systemd/system/tv_controller_interface.service

	@echo "Reloading systemctl daemon"
	systemctl daemon-reload