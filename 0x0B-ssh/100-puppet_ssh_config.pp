# 100-puppet_ssh_config.pp
include stdlib

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/sshd_config',
  line   => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'Declare identity file':
  path   => '/home/vagrant/.ssh/config',
  line   => '     IdentityFile ~/.ssh/school',
  replace => true,
}
