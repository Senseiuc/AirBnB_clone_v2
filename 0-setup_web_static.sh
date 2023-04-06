#!/usr/bin/env bash

#A script that sets up your web
#servers for the deployment of web_static

if ! which nginx > /dev/null 2>&1; then
	sudo apt-get update
	sudo apt-get -y upgrade
	sudo apt-get -y install nginx
	sudo service nginx start
fi
MS="\\\tlocation /hbnb_static/{\n\t\talias /data/web_static/current/;\n\t}\n"
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sudo chown -hR ubuntu:ubuntu /data/
echo "Test the ngilnx configuration!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i "50i $MS"  /etc/nginx/sites-available/default
sudo service nginx restart
