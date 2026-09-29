# ICA04 Reflection

## 1. Local and Remote Repositories

What is the difference between the local TaskTrack repository and the repository hosted on GitHub?

The github repository is stored on the cloud and can be accessed from the cloud on any device. The TaskTrack repository is stored locally on the decice

## 2. Connecting and Pushing

Why did adding `origin` not immediately place the project files on GitHub?

Adding the origin connects the local repository to the destination (remote repository on github). That doesn't transfer the files over because the project still has to be pushed. 

## 3. Cloning

How is cloning a repository different from downloading its files as a ZIP archive?

Cloning a repository clones not just the files but also the local git repository along with the commit history. This allows the user to view information about the git project and immediately start working using git version control and can commit and push changes to the remote repository on github.

## 4. Fetching and Pulling

What information did `git fetch` update, and what additional action did `git pull` perform?

Git fetch, fetched the latest version of the project from the remote repository on github. Git pull actually took the data and overrided the local user version of the project so the local and remote repositories are up to date with one another. 

## 5. Focused Commits

Why is it useful to commit the Python feature, sample task data, and README documentation separately?

Committing the three separately improves commit history readability. More importantly though, it makes it easier to find conflicts and undo a specific change without needing to scour through and debug the code. 