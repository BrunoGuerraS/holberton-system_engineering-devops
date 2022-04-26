# Ussing puppet - intall Web Server
# Install Nginx
exec {'Install_nginx':
  provider => shell,
  command  => 'sudo apt-get -y update ;\
               sudo apt-get -y install nginx ;\
               sudo chown -R ubuntu /var/www ;\
               sudo service nginx start',
}
# Configure redirect_me
exec {'Configure_redirect':
  provider => shell,
  command  => 'echo "Hello World" > /var/www/html/index.nginx-debian.html ;\
               sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=NdYWuo9OFAw permanent;/" /etc/nginx/sites-available/default ;\
               sudo service nginx restart',
}
# Configure redirect 404
exec {'Redirect_404':
    provider => shell,
    command  => 'sudo sed -i "s/^server\s{/server {\n\terror_page 404 \/error_404.html;/1" /etc/nginx/sites-available/default',
}
# Added header https
exec {'header_http':
    provider => shell,
    command  => 'sudo sed -i "s/^server\s{/server {\n\tadd_header X-Served-By $HOSTNAME;/1" /etc/nginx/sites-available/default;\
                 sudo service nginx restart',
}
