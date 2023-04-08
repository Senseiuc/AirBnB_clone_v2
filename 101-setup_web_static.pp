# A script that sets up web servers for the deployment of web_static

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
}

file {'/data/web_static/releases/test/':
	ensure => 'directory',
	owner => 'ubuntu',
	group => 'ubuntu',
}

file {'/data/web_static/shared/':
	ensure => 'directory',
        owner => 'ubuntu',
        group => 'ubuntu',
}


file {'/data/web_static/releases/test/index.html':
	ensure => 'present',
        owner => 'ubuntu',
        group => 'ubuntu',
	content => 'Test Nginx'
}

file { '/data/web_static/current':
  	ensure => link,
	target => '/data/web_static/releases/test/',
	force => true,
	replace => true,
}

exec {'configure nginx':
	command => 'sudo sed -i \
"\\\tlocation /hbnb_static/{\n\t\talias /data/web_static/current/;\n\t}\n $MS" \ 
/etc/nginx/sites-available/default',
    	path    => '/usr/local/bin/:/bin/',
}
exec { '/usr/bin/env sudo service nginx restart' : }


	
