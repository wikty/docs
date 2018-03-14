https://www.unix.com/man-page/centos/5/sysctl.d/

目录 `/etc/sysctl.d` 以及如下目录：

```
 /etc/sysctl.d/*.conf

       /run/sysctl.d/*.conf

       /usr/lib/sysctl.d/*.conf
```

Configure kernel parameters at boot，均用来在系统启动时配置内核参数

At boot, systemd-sysctl.service(8) reads configuration files from the above directories to   configure sysctl(8) kernel parameters.

```
Each configuration file shall be named in the style of program.conf. Files in /etc/
       override files with the same name in /usr/lib/ and /run/. Files in /run/ override files
       with the same name in /usr/lib/. Packages should install their configuration files in
       /usr/lib/. Files in /etc/ are reserved for the local administrator, who may use this logic
       to override the configuration files installed by vendor packages. All configuration files
       are sorted by their filename in lexicographic order, regardless of which of the
       directories they reside in. If multiple files specify the same variable name, the entry in
       the file with the lexicographically latest name will be applied. It is recommended to
       prefix all filenames with a two-digit number and a dash, to simplify the ordering of the
       files.

       If the administrator wants to disable a configuration file supplied by the vendor, the
       recommended way is to place a symlink to /dev/null in /etc/sysctl.d/ bearing the same
       filename.
```