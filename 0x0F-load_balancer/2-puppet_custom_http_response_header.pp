#!/usr/bin/env bash
# Add a custom HTTP header with Puppet
exec {'http':
    commnad => 'sudo apt-get update && sudo apt-get install nginx -y &&
                custom_header="\\\tadd_header X-Served-By \$HOSTNAME:\n"
                && sudo sed -i "17i $custom_header" /etc/nginx/nginx.conf
                sudo service nginx restart',
}
