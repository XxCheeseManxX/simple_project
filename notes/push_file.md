## Pushing to a git repo for the first time!

# Create the file

In Linux, a file can be created with the `touch` command:

`touch test.txt`

To open the file for editing in VS Code:

`code test.txt`

# Git workflow

1. `git add test.txt`
2. `git commit -m "My first commit!`
3. `git push`

# Creating SSH keys

1. `ssh-keygen -t rsa -b 4096`
2. `cat location_to_key/.ssh/id_rsa.pub`
3. Copy the public key
4. In git: `settings -> ssh keys -> new ssh keys`
5. Paste public ssh key, save

# Set remote repo

1. On your repository page, click on: `code -> ssh`
2. Copy the url
3. In your command line: `git remote set-url origin <paste_url>`


