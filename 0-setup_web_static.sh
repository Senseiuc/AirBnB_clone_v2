#!/usr/bin/env bash

#A script that sets up your web
#servers for the deployment of web_static
#check if nginx is installed

if ! command -v nginx > /dev/null 2>&1; then
	#update server
	sudo apt-get update
	#upgrade server
	sudo apt-get -y upgrade
	#install nginx
	sudo apt-get -y install nginx
	#start nginx
	sudo service nginx start
	#end statement
fi
#define location code structure
MS="\\\tlocation /hbnb_static/{\n\t\talias /data/web_static/current/;\n\t}\n"
#mkdir recursively
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
#add user to group and make owner
sudo chown -hR ubuntu:ubuntu /data/
#create file and add text into it
echo "Test the ngilnx configuration!" | sudo tee /data/web_static/releases/test/index.html
#symlink file
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
#write into the nginx config file
sudo sed -i "50i $MS"  /etc/nginx/sites-available/default
#restart nginx
sudo service nginx restart
