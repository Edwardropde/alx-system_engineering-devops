# 0-create_a_file.pp

file { '/tmp/school':
	ensure  => 'file',
	path    => '/tmp/school',
	owner   => 'www-data',
	group   => 'www-data',
	mode    => '0744',
	content => 'I love Puppet',
}
