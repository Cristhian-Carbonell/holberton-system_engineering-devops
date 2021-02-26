# to login with the holberton user and open a file
file { 'login_file':
  ensure  =>  present,
  path    =>  '/etc/security/limits.conf',
  content =>  '#File erased'
}
