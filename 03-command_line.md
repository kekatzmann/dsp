# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > rm -iR    - Removes all directories and files at a specified location recursively (R), but also allows you to examine each directory before removal (i). Be careful when using rm -R, there is no undo.

> > pushd     - Allows you to go to a place further into your file system, while saving the location you last were.

> > popd      - Brings you back to the saved location after using the pushd command.

> > cd ..     - Brings the current working directory up one level.

> > pwd       - Reveals the current working directory.

> > " > "       - Takes output from the command on the left and writes it into the file on the right.

> > " >> "      - Takes output from command on left and appends it to file on right.

> > " | "       - Pipes output from one command (on left) and to use as input for another command (on right).

> > " * "       - Matches anything in a wildcard. ex: ls * (Displays a list of all items in a directory, and the items in directories below), rm * .txt (removes all files of the .txt format).

> > find . -name "name" -print     - used to find files/directories based on name. Can also find based on size (-size n), date accessed (-atime n).

> > grep -i     - Searches inside specified files. -i included to ignore case.

> > man         - "manual" / help

> > clear       - clears screen






---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 'ls' returns a short list of files and directories of the current directory you are in. What you see in the graphical file browser.

> > 'ls -a' also includes 'hidden files' (those staring with . or ..)

> > 'ls -l' returns items in the current directory in a long listing format (shows who created the item, time it was last modified, etc.)

> > 'ls -lh' returns items in long listing and human readable format. It displays units of file sizes.

> > 'ls -lah' returns items in long listing, human readable format, and includes hidden files.

> > 'ls -t' returns items, sorted by time of last modification.

> > 'ls -Glp' returns items in a long listing format, with directories highlighted (-G) and '/' to them (-p).

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 

