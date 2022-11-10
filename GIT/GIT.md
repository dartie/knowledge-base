# GIT


## Original Help 
```bash
# Command line instructions
Git global setup
git config --global user.name "Dario Necco"
git config --global user.email "dario_necco@programmingresearch.com"

# Create a new repository
git clone http://mist.programmingresearch.com/csgtools/SMGenerator.git
cd SMGenerator
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master

# Existing folder
cd existing_folder
git init
git remote add origin http://mist.programmingresearch.com/csgtools/SMGenerator.git
git add .
git commit
git push -u origin master

# Existing Git repository
cd existing_repo
git remote add origin http://mist.programmingresearch.com/csgtools/SMGenerator.git
git push -u origin --all
git push -u origin --tags
```


## Add a file and push automatically to GIT
```bash
git add "file" && git commit -m " " && git push -u origin master
```


## Revert a file which has changes not committed
```bash
git checkout filename
```

## Store credentials permanently 
```
bash
git config credential.helper store
git push http://example.com/repo.git
```

## see commit history
```bash
git log 
```
or in a single line

```bash
git log --oneline
```

## Branches

### List the branches on your repository

```bash
git branch 
* master
```
    
### Create a new feature branch in the repository
```bash
$ git branch <feature_branch>    
```
    
### Switch to the feature branch to work on it.
```bash
$ git checkout <feature_branch>    
```
    
### Commit the change to the feature branch:
```bash
$ git add . 
$ git commit -m "adding a change from the feature branch"
```

### Switch back to the master branch.
```bash
$ git checkout master
```
    
### Push the feature branch to Bitbucket:
```bash
$ git push origin <feature_branch>
```


### diff with coloured exported
```bash
wget "http://www.pixelbeat.org/scripts/ansi2html.sh" -O /tmp/ansi2html.sh
chmod +x /tmp/ansi2html.sh
git diff --color-words --no-index orig.txt edited.txt | \\
/tmp/ansi2html.sh > 2beshared.html
```
> `--color` or `--color-words` are required

