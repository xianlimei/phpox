from replacement import execute, shell_exec, system, passthru, popen, getenv, ini_get, fsockopen
from replacement import fgets, php_uname


FUNCTIONS = {
             "disk_free_space;" : "\treturn '%s';" % "36698988544", 
             "diskfreespace;" : "\treturn '%s';" % "36698988544", 
             "disk_total_space;" : "\treturn '%s';" % "51221590016", 
             "exec;$cmd;&$ret;" : execute.call(),
             "fgets;$handle;$length;" : fgets.call(),
             #"function_exists;" : "\treturn true;",
             "fsockopen;$hostname;$port;$errno;$errstr;$timeout;" : fsockopen.call(), 
             "getcwd;" : "\treturn '%s';" % "/var/www",
             "getenv;$varname;" : getenv.call(),
             "get_current_user;" : "\treturn '%s';" % "root", 
             "getmyuid;" : "\treturn '%s';" % "0",
             "getmygid;" : "\treturn '%s';" % "0",
             "ini_get;$varname;" : ini_get.call(), 
             "is_writable;" : "\treturn true;", 
             "is_callable;" : "\treturn true;",
             "php_uname;" : php_uname.call(), 
             "passthru;$cmd;&$ret;" : passthru.call(),
             "popen;$cmd;" : popen.call(),
             "shell_exec;$cmd;" : shell_exec.call(),
             "system;$cmd;&$ret;" : system.call(),
             }

FUNCTIONS2 = {
             "dl;" : "", 
             "escapeshellarg;" : "", 
             "escapeshellcmd;" : "", 
             "proc_close;" : "", 
             "proc_get_status;" : "", 
             "proc_nice;" : "", 
             "proc_open;" : "", 
             "proc_terminate;" : "",
             "checkdnsrr;" : "", 
             "closelog;" : "", 
             "define_syslog_variables;" : "", 
             "dns_check_record;" : "", 
             "dns_get_mx;" : "", 
             "dns_get_record;" : "", 
             "getcwd;" : "", 
             "gethostbyaddr;" : "", 
             "gethostbyname;" : "", 
             "gethostbynamel;" : "", 
             "gethostname;" : "", 
             "getmxrr;" : "", 
             "getprotobyname;" : "", 
             "getprotobynumber;" : "", 
             "getservbyname;" : "", 
             "getservbyport;" : "", 
             "header_remove;" : "", 
             "header;" : "", 
             "headers_list;" : "", 
             "headers_sent;" : "", 
             "inet_ntop;" : "", 
             "inet_pton;" : "", 
             "ip2long;" : "", 
             "long2ip;" : "",
             "fclose;" : "", 
             "feof;" : "", 
             "fgets;" : "", 
             "fgetss;" : "", 
             "file;" : "", 
             "fopen;" : "", 
             "fwrite;" : "", 
             "mail;" : "", 
             "pfsockopen;" : "",
             "openlog;" : "", 
             "setcookie;" : "", 
             "setrawcookie;" : "", 
             "socket_recvfrom;" : "", 
             "socket_recv;" : "", 
             "stream_socket_recvfrom;" : "", 
             "msg_receive;" : "", 
             "socket_get_status;" : "", 
             "socket_set_blocking;" : "", 
             "socket_set_timeout;" : "", 
             "syslog;" : "", 
             "basename;" : "", 
             "chgrp;" : "", 
             "chmod;" : "", 
             "chown;" : "", 
             "clearstatcache;" : "", 
             "copy;" : "", 
             "dirname;" : "", 
             "disk_free_space;" : "36698988544", 
             "disk_total_space;" : "51221590016", 
             "diskfreespace;" : "36698988544", 
             "fclose;" : "", 
             "feof;" : "", 
             "fflush;" : "", 
             "fgetc;" : "", 
             "fgetcsv;" : "", 
             "fgets;" : "", 
             "fgetss;" : "", 
             "file_exists;" : "", 
             "file_get_contents;" : "", 
             "file_put_contents;" : "", 
             "file;" : "", 
             "fileatime;" : "", 
             "filectime;" : "", 
             "filegroup;" : "", 
             "fileinode;" : "", 
             "filemtime;" : "", 
             "fileowner;" : "", 
             "fileperms;" : "", 
             "filesize;" : "", 
             "filetype;" : "", 
             "flock;" : "", 
             "fnmatch;" : "", 
             "fopen;" : "", 
             "fpassthru;" : "", 
             "fputcsv;" : "", 
             "fputs;" : "", 
             "fread;" : "", 
             "fscanf;" : "", 
             "fseek;" : "", 
             "fstat;" : "", 
             "ftell;" : "", 
             "ftruncate;" : "", 
             "fwrite;" : "", 
             "glob;" : "", 
             "is_dir;" : "", 
             "is_executable;" : "", 
             "is_file;" : "", 
             "is_link;" : "", 
             "is_readable;" : "", 
             "is_uploaded_file;" : "", 
             "is_writeable;" : "", 
             "lchgrp;" : "", 
             "lchown;" : "", 
             "link;" : "", 
             "linkinfo;" : "", 
             "lstat;" : "", 
             "mkdir;" : "", 
             "move_uploaded_file;" : "", 
             "parse_ini_file;" : "", 
             "parse_ini_string;" : "", 
             "pathinfo;" : "", 
             "pclose;" : "", 
             "popen;" : "", 
             "readfile;" : "", 
             "readlink;" : "", 
             "realpath_cache_get;" : "", 
             "realpath_cache_size;" : "", 
             "realpath;" : "", 
             "rename;" : "", 
             "rewind;" : "", 
             "rmdir;" : "", 
             "set_file_buffer;" : "", 
             "stat;" : "", 
             "symlink;" : "", 
             "tempnam;" : "", 
             "tmpfile;" : "", 
             "touch;" : "", 
             "umask;" : "", 
             "unlink;" : "", 
             }