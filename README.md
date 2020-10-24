# notes
A easy and secure way to take diary/notes.

### What is this?
This is a command-line taking diary software with encryption supported. And its name is **notes**!  
It is based on bash, shell and python.  

You can use it take notes, and save resources(like images, videos or docs).  

The most exciting part is this software supports encryption and decryption.  
Also, it has many convenient options to help you organize your diaries.

### How to setup it?
1. Make sure you install the dependencies(nano, bash, python3, pycryptodome).
2. Make a new folder to contain setup info in home.

    ```bash
    cd ~
    mkdir .notes
    nano .notes/path
    ```
    And then **type** the path of the `notes` in the `nano` editor.  
    For example, `/home/$USER/Documents/notes` when you put the `notes` app in `/home/$USER/Documents/`.

3. Go to the path of `notes`.

    ```bash
    cd /home/$USER/Documents/notes
    sudo ln -s new_command /usr/bin/write_diary
    ```

### How to use it?
Type `write_diary --help` in your terminal.
Then you will see those options.
```
--help                          output help infos.
--date                          specify a date to write.
--make-list <start> <end>       make a list containing diarys between <start> and <end>.
--get-list <start> <end>        make a list info about diarys between <start> and <end>.
--remove-list                   remove list file.
--protect                       protect diarys from deleting accidently.
--unprotect                     unprotect diarys from deleting accidently.
--set-mode safe>/unsafe         set edit mode between safe and unsafe. mode is relevant to "--protect" or "--unprotect".
--get-mode                      get current mode.
--update-path <current path>    update path which contains "new" file. Suggest: get <current path> with "$(pwd)" command in the "new" file path.
--get-path                      get the current path of "new" file.
--encrypt <date>		encrypt diarys.
--decrypt <date>		decrypt diarys.
```
`write_diary` without any options means write today's diary.
