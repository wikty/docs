## 关闭后台进程

### Method #1 - ps

You can use the `ps` command to find the process ID for this process and then use the PID to kill the process.

### Example

```
$ ps -eaf | grep [w]get 
saml      1713  1709  0 Dec10 pts/0    00:00:00 wget ...

$ kill 1713

```

### Method #2 - pgrep

You can also find the process ID using `pgrep`.

### Example

```
$ pgrep wget
1234

$ kill 1234

```

### Method #3 - pkill

If you're sure it's the only `wget` you've run you can use the command `pkill` to kill the job by name.

### Example

```
$ pkill wget

```

### Method #4 - jobs

If you're in the same shell from where you ran the job that's now backgrounded. You can check if it's running still using the `jobs` command, and also kill it by its job number.

### Example

My fake job, `sleep`.

```
$ sleep 100 &
[1] 4542

```

Find it's job number. **NOTE:** the number 4542 is the process ID.

```
$ jobs
[1]+  Running                 sleep 100 &

$ kill %1
[1]+  Terminated              sleep 100

```

### Method #5 - fg

You can bring a backgrounded job back to the foreground using the `fg` command.

### Example

Fake job, `sleep`.

```
$ sleep 100 &
[1] 4650

```

Get the job's number.

```
$ jobs
[1]+  Running                 sleep 100 &

```

Bring job #1 back to the foreground, and then use Ctrl+C.

```
$ fg 1
sleep 100
^C
$
```