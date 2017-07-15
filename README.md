# time-cli

### this script is a tool for analyzing the computational time of other scripts

```
$ ./run.py <command_file> <num_trials> [<wait_list>]
```

- ```command_file``` specifies the name of a file with a one-line command in it. supports output pipelines!

- ```num_trials``` specifies the number of trials you like to run your command for.

- ```wait_list``` is optional, and is essentially a list of 0s or 1s specifying which commands in your pipeline should or shouldn't be waited on by the other commands. defaults to 1s, meaning all commands are waited on sequentially.

see the other files to see how these examples match up. feel free to modify the cleanup function.

```
$ ./run.py <command> 10
$ ./run.py commands/toucher 50
$ ./run.py commands/clone 10
$ ./run.py commands/archive 4 0 1
```
