# we use the SED command to change class-wp-locale.phpp to class-wp-locale.php in wp-settings.php file
exec { 'fixer':
    command => 'sed -i "s|class-wp-locale.phpp|class-wp-locale.php|g" /var/www/html/wp-settings.php',
    provider => shell,
}
