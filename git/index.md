主要是客户端的用法

## 配置

After you [install Git](https://linode.com/docs/development/version-control/how-to-install-git-on-mac-and-windows), configure it for first time use using `git config`, a built-in tool that obtains and sets configuration variables. These configuration variables are located in three different places on a GNU/Linux system:

- `/etc/gitconfig` - stores the configuration information for all system users and their respective repositories.
- `~/.gitconfig` - stores user-specific configuration files on the system.
- `.git/config` - this is the configuration file of your current working repository.

For a Windows system, the `.gitconfig` file is located in the `$HOME` directory of the user’s profile. The full path is `C:\Document and Settings\$USER` or `C:\Users\$USER`

After installing Git make sure your username and email address are set correctly. To verify, use the command:

```
git config --list
```

If your name and email are not listed in the output, use the following commands to set them manually, replacing `examplename` and `user@example.com`:

```
git config --global user.name examplename
git config --global user.email user@example.com
```



## 常用命令

| `git add`    | Add a file to a repository.              | `git add filename`         |
| ------------ | ---------------------------------------- | -------------------------- |
| `git rm`     | Remove a file from a repository.         | `git rm filename`          |
| `git mv`     | Move or rename a tracked file, directory, or symlink. | `git mv file_from file_to` |
| `git branch` | List all the local and remote branches.  | `git branch branchname`    |
| `git commit` | Commit all staged objects.               | `git commit -m "updates"`  |
| `git pull`   | Download all changes from the remote repo and merge them in a specified repo file. | `git pull repo refspec`    |
| `git push`   | Publish the changes to the remote repo.  | `git push repo`            |



## 分支



Branches are used for editing files without disturbing the working portions of a project. The main branch is normally named `master`, it’s customary to name the branch after an issue being fixed or a feature being implemented. Because Git keep tracks of file changes, you can jump from branch to branch without overwriting or interfering with other branches in the repo.

The basic options used with the `git branch` command are:

| Option | Description                         |
| ------ | ----------------------------------- |
| -r     | List the remote branches            |
| -a     | Show both local and remote branches |
| -m     | Rename an old branch                |
| -d     | Delete a branch                     |
| -r -d  | Delete a remote branch              |



## 远程仓库

Remote repositories are hosted on a network or another location on the Internet.

| `git remote add [remote-name] [url]`     | Add a new remote repository.             |
| ---------------------------------------- | ---------------------------------------- |
| `git fetch [repository [refspec]]`       | Gather all the data from a remote project that you do not have yet. |
| `git pull`                               | Obtain and merge a remote branch into your current branch. |
| `git push [remote-name] [branch-name]`   | Move your data from your branch to your server. |
| `git remote show [remote-name]`          | Display information about the remote you specified. |
| `git remote rename [old-name] [new-name]` | Rename a remote.                         |
| `git remote rm [name]`                   | Remove the remote you specified.         |



## Hooks

https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks

Like many other Version Control Systems, Git has a way to fire off custom scripts when certain important actions occur. There are two groups of these hooks: client-side and server-side. Client-side hooks are triggered by operations such as committing and merging, while server-side hooks run on network operations such as receiving pushed commits. You can use these hooks for all sorts of reasons.

### Installing a Hook

The hooks are all stored in the `hooks` subdirectory of the Git directory. In most projects, that’s `.git/hooks`. When you initialize a new repository with `git init`, Git populates the hooks directory with a bunch of example scripts, many of which are useful by themselves; but they also document the input values of each script. All the examples are written as shell scripts, with some Perl thrown in, but any properly named executable scripts will work fine – you can write them in Ruby or Python or whatever language you are familiar with. If you want to use the bundled hook scripts, you’ll have to rename them; their file names all end with `.sample`.

To enable a hook script, put a file in the `hooks` subdirectory of your .git directory that is named appropriately (without any extension) and is executable. From that point forward, it should be called. We’ll cover most of the major hook filenames here.

### Client-Side Hooks

There are a lot of client-side hooks. This section splits them into committing-workflow hooks, email-workflow scripts, and everything else.

| Note | It’s important to note that client-side hooks are **not** copied when you clone a repository. If your intent with these scripts is to enforce a policy, you’ll probably want to do that on the server side; see the example in [An Example Git-Enforced Policy](https://git-scm.com/book/en/v2/ch00/_an_example_git_enforced_policy). |
| ---- | ---------------------------------------- |
|      |                                          |

#### Committing-Workflow Hooks

The first four hooks have to do with the committing process.

The `pre-commit` hook is run first, before you even type in a commit message. It’s used to inspect the snapshot that’s about to be committed, to see if you’ve forgotten something, to make sure tests run, or to examine whatever you need to inspect in the code. Exiting non-zero from this hook aborts the commit, although you can bypass it with `git commit --no-verify`. You can do things like check for code style (run `lint` or something equivalent), check for trailing whitespace (the default hook does exactly this), or check for appropriate documentation on new methods.

The `prepare-commit-msg` hook is run before the commit message editor is fired up but after the default message is created. It lets you edit the default message before the commit author sees it. This hook takes a few parameters: the path to the file that holds the commit message so far, the type of commit, and the commit SHA-1 if this is an amended commit. This hook generally isn’t useful for normal commits; rather, it’s good for commits where the default message is auto-generated, such as templated commit messages, merge commits, squashed commits, and amended commits. You may use it in conjunction with a commit template to programmatically insert information.

The `commit-msg` hook takes one parameter, which again is the path to a temporary file that contains the commit message written by the developer. If this script exits non-zero, Git aborts the commit process, so you can use it to validate your project state or commit message before allowing a commit to go through. In the last section of this chapter, We’ll demonstrate using this hook to check that your commit message is conformant to a required pattern.

After the entire commit process is completed, the `post-commit` hook runs. It doesn’t take any parameters, but you can easily get the last commit by running `git log -1 HEAD`. Generally, this script is used for notification or something similar.

#### Email Workflow Hooks

You can set up three client-side hooks for an email-based workflow. They’re all invoked by the `git am` command, so if you aren’t using that command in your workflow, you can safely skip to the next section. If you’re taking patches over email prepared by `git format-patch`, then some of these may be helpful to you.

The first hook that is run is `applypatch-msg`. It takes a single argument: the name of the temporary file that contains the proposed commit message. Git aborts the patch if this script exits non-zero. You can use this to make sure a commit message is properly formatted, or to normalize the message by having the script edit it in place.

The next hook to run when applying patches via `git am` is `pre-applypatch`. Somewhat confusingly, it is run *after* the patch is applied but before a commit is made, so you can use it to inspect the snapshot before making the commit. You can run tests or otherwise inspect the working tree with this script. If something is missing or the tests don’t pass, exiting non-zero aborts the `git am`script without committing the patch.

The last hook to run during a `git am` operation is `post-applypatch`, which runs after the commit is made. You can use it to notify a group or the author of the patch you pulled in that you’ve done so. You can’t stop the patching process with this script.

#### Other Client Hooks

The `pre-rebase` hook runs before you rebase anything and can halt the process by exiting non-zero. You can use this hook to disallow rebasing any commits that have already been pushed. The example `pre-rebase` hook that Git installs does this, although it makes some assumptions that may not match with your workflow.

The `post-rewrite` hook is run by commands that replace commits, such as `git commit --amend`and `git rebase` (though not by `git filter-branch`). Its single argument is which command triggered the rewrite, and it receives a list of rewrites on `stdin`. This hook has many of the same uses as the `post-checkout` and `post-merge` hooks.

After you run a successful `git checkout`, the `post-checkout` hook runs; you can use it to set up your working directory properly for your project environment. This may mean moving in large binary files that you don’t want source controlled, auto-generating documentation, or something along those lines.

The `post-merge` hook runs after a successful `merge` command. You can use it to restore data in the working tree that Git can’t track, such as permissions data. This hook can likewise validate the presence of files external to Git control that you may want copied in when the working tree changes.

The `pre-push` hook runs during `git push`, after the remote refs have been updated but before any objects have been transferred. It receives the name and location of the remote as parameters, and a list of to-be-updated refs through `stdin`. You can use it to validate a set of ref updates before a push occurs (a non-zero exit code will abort the push).

Git occasionally does garbage collection as part of its normal operation, by invoking `git gc --auto`. The `pre-auto-gc` hook is invoked just before the garbage collection takes place, and can be used to notify you that this is happening, or to abort the collection if now isn’t a good time.

### Server-Side Hooks

In addition to the client-side hooks, you can use a couple of important server-side hooks as a system administrator to enforce nearly any kind of policy for your project. These scripts run before and after pushes to the server. The pre hooks can exit non-zero at any time to reject the push as well as print an error message back to the client; you can set up a push policy that’s as complex as you wish.

#### `pre-receive`

The first script to run when handling a push from a client is `pre-receive`. It takes a list of references that are being pushed from stdin; if it exits non-zero, none of them are accepted. You can use this hook to do things like make sure none of the updated references are non-fast-forwards, or to do access control for all the refs and files they’re modifying with the push.

#### `update`

The `update` script is very similar to the `pre-receive` script, except that it’s run once for each branch the pusher is trying to update. If the pusher is trying to push to multiple branches, `pre-receive` runs only once, whereas update runs once per branch they’re pushing to. Instead of reading from stdin, this script takes three arguments: the name of the reference (branch), the SHA-1 that reference pointed to before the push, and the SHA-1 the user is trying to push. If the update script exits non-zero, only that reference is rejected; other references can still be updated.

#### `post-receive`

The `post-receive` hook runs after the entire process is completed and can be used to update other services or notify users. It takes the same stdin data as the `pre-receive` hook. Examples include emailing a list, notifying a continuous integration server, or updating a ticket-tracking system – you can even parse the commit messages to see if any tickets need to be opened, modified, or closed. This script can’t stop the push process, but the client doesn’t disconnect until it has completed, so be careful if you try to do anything that may take a long time.



利用 Git Hooks 完成本地测试环境的启动以及生成环境的部署

https://www.digitalocean.com/community/tutorials/how-to-use-git-hooks-to-automate-development-and-deployment-tasks



## submodule

不重复的引用公共资源 gti submodule

当项目越来越庞大之后，不可避免的要拆分成多个子模块，我们希望各个子模块有独立的版本管理，并且由专门的人去维护，这时候我们就要用到git的submodule功能