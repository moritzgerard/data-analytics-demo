# How to Git with Kitt

## 🎯 Goal

The goal is to push a python file called `demo.py` to our GitHub.

## 🧠 What you’ll learn

- How to use Kitt for challenges with tests
- The basics of interacting with files in VS Code
- How to push a repository to GitHub

## 🔧 Troubleshooting

<details>
<summary markdown="span">❓ I'm not in the right directory</summary>

Run `pwd` in your terminal to check your current directory. It should end with:

```bash
~/code/<user.github_nickname>/{{ local_path_to("03-Data-Transformation/08-Intro-To-Git-And-Versioning/01-Demo") }}/
```

The `~` sign ("tilde") at the start of the line will be replaced by either `/Users/{YOUR_COMPUTER_USERNAME}` (macOS) or `/home/{YOUR_COMPUTER_USERNAME}` (Windows / Linux). The `~` is a terminal shorthand for your personal home folder on your machine.

If it doesn't match, use `cd` to navigate to the correct directory. You can also run the first line of the setup commands from Kitt again (the line starting with `mkdir`).

</details>

<details>
<summary markdown="span">❓ My test is still failing</summary>

- Make sure you've saved the `demo.py` file after making changes (Cmd+S or Ctrl+S).
- Check that your function exactly matches the solution:

```python
def hello_world():
    """Returns the string 'Hello World!'"""
    return "Hello World!"
```

- Make sure there are no extra spaces or typos.
- Run `make` again to re-run the test.

If it's still failing, consult a TA!

</details>

<details>
<summary markdown="span">❓ I can't push to GitHub</summary>

- Check that you've run `git add demo.py` to stage your changes.
- Check that you've run `git commit` with a message.
- Make sure you have an internet connection.
- If you see an authentication error, make sure your GitHub credentials are set up correctly.
- Try running `git status` to see what state your repository is in.

If you're still stuck, consult a TA!

</details>

<details>
<summary markdown="span">❓ `make` command not found</summary>

Make sure you're in the correct directory (see "I'm not in the right directory" above).

</details>

<details>
<summary markdown="span">❓ I see files I didn't create (like `.git` or `.gitignore`)</summary>

These are hidden configuration files that Git and other tools use. You don't need to modify them. They're normal and expected!

- `.git` — Stores all of your repository's version history. **Never delete or modify it manually!**
- `.gitignore` — Tells Git which files to ignore (not track).

</details>

## 📁 Setup

To make challenge completion simpler, we have added terminal instructions to challenges that have test suites.

If you haven't already, **copy the terminal instructions at the top of this page and run them in your terminal**.

This will:

- Create and navigate to a directory (folder) for this challenge in your terminal
- Download all of the files for this challenge
- Set up a new repository locally and on GitHub
- Open the challenge in VS Code
- Run the test suite for this challenge

At this point the tests will fail with a lot of red, that is expected. Keep on reading.

Run the following command in the terminal to check you are in the right directory:

```bash
pwd
```

Your result should look like this:

```bash
~/code/<user.github_nickname>/{{ local_path_to("03-Data-Transformation/08-Intro-To-Git-And-Versioning/01-Demo") }}/
```

The `~` sign ("tilde") at the start of the line will be replaced by either `/Users/{YOUR_COMPUTER_USERNAME}` (macOS) or `/home/{YOUR_COMPUTER_USERNAME}` (Windows / Linux). The `~` is a terminal shorthand for your personal home folder on your machine.

❌ If it doesn't, consult a TA!

✅ If it does, then you are ready to take on this demo challenge!

## Practicing in the Terminal

We can take a look at what is inside this directory (what you probably call a folder) directly from the terminal, by using the following command:

```bash
tree
```

You should see something that looks like this:

```bash
.
├── autotest.sh
├── demo.py
├── Makefile
├── README.md
└── tests
    ├── __init__.py
    └── test_demo.py

2 directories, 6 files
```

We can create a new directory inside of this directory using the following code:

```bash
mkdir temporary_folder
```

Now run `tree` again and you should see your new directory appearing. It should look like this:

```bash
.
├── autotest.sh
├── demo.py
├── Makefile
├── README.md
├── temporary_folder
└── tests
    ├── __init__.py
    └── test_demo.py

3 directories, 6 files
```

If we want to make a text file in that directory, we can use the `touch` command:

```bash
touch temporary_folder/example_file.txt
```

Now run the `tree` command again to see the results:

<details>
<summary markdown="span"> 🌳 Results </summary>

```bash
.
├── autotest.sh
├── demo.py
├── Makefile
├── README.md
├── temporary_folder
│   └── example_file.txt
└── tests
    ├── __init__.py
    └── test_demo.py

3 directories, 7 files
```

</details>

We can also change our current directory by stepping into that directory:

```bash
cd temporary_folder
```

Now run `tree` again:

<details>
<summary markdown="span"> 🌳 Results </summary>

```bash
.
└── example_file.txt

1 directory, 1 file
```

</details>

We can create another file and now we don't have to specify which directory it belongs in, because it will default to our current directory.

```bash
touch another_file.txt
```

Check out the `tree`:

<details>
<summary markdown="span"> 🌳 Results </summary>

```bash
.
├── another_file.txt
└── example_file.txt

1 directory, 2 files
```

</details>

To delete this file we need to use the `rm` command. ⚠️ **Be careful with this command, it will delete things permanently and there is no undo command.**

```bash
rm another_file.txt
```

One more time, let's check out the `tree`:

<details>
<summary markdown="span"> 🌳 Results </summary>

```bash
.
└── example_file.txt

1 directory, 1 file
```

</details>

Now to move back to our challenge directory, we need to change directory again with `cd` but we can use a shortcut of `..` which tells the terminal to go up one level.

```bash
cd ..
```

💡 **Hint:** to go up by two levels we would use `../..`. To go up three `../../..` and so on. If you ever get fully lost in your terminal, you can always use `cd` or `cd ~` to go to your home directory and navigate from there.

Now run `tree` and you should find yourself in the directory we started in:

<details>
<summary markdown="span"> 🌳 Results </summary>

```bash
.
├── autotest.sh
├── demo.py
├── Makefile
├── README.md
├── temporary_folder
│   └── example_file.txt
└── tests
    ├── __init__.py
    └── test_demo.py

3 directories, 7 files
```

</details>

Ok, time to get rid of that temporary directory, but just `rm` isn't going to work, because we have files inside and the terminal needs to know what to do with those. [See here for more](https://www.maths.cam.ac.uk/computing/linux/unixinfo/rm). To let it know what to do with those files we're going to use an add on to the command `-rf`:

- `rm -i` will ask before deleting each file. (Use this if you want to be fully in control of what gets deleted)

- `rm -r` will recursively delete a directory and all its contents (normally `rm` will not delete directories, while `rmdir` will only delete empty directories).

- `rm -f` will forcibly delete files without asking.

We can combine r and f to recursively delete our folder and all of its contents by force.

```bash
rm -rf temporary_folder
```

⚠️ `rm -rf` is a dangerous combo, only use it if you are absolutely certain that you want to delete this directory and everything inside of it. When copying code from anywhere to run in your terminal always make sure you have checked for `rm -rf` as some bad actors will look to break your computer.

Let's run one last `tree` to check that the directory and the example file inside it are gone:

<details>
<summary markdown="span"> 🌳 Results </summary>

```bash
.
├── autotest.sh
├── demo.py
├── Makefile
├── README.md
└── tests
    ├── __init__.py
    └── test_demo.py

2 directories, 6 files
```

</details>

### Quick Reference

- `pwd` — Print working directory
- `tree` — Show directory structure
- `ls` — List all files in the current directory
- `ls -a` — List all files in the current directory, including hidden files
- `mkdir` — Make a new directory
- `touch` — Create a new file
- `cd` — Change directory
- `.` — Current directory
- `..` — Up one level
- `../..` — Up two levels
- `~` — Home directory
- `rm` — Remove file (use with caution!)
- `rm -rf` — Remove directory and contents (use with caution!)

## 🧩 Implementation

1. Take a look at the files for the challenge in VS Code. You can open it from the terminal using:

   ```bash
   code .
   ```

    This will open the current directory (`.`) in VS Code.

    You should see the following file structure:

   ```markdown
    📂 .lewagon
          metadata.yml
    📂 tests
          __init__.py
          test_demo.py
    .gitignore
    autotest.sh
    demo.py
    Makefile
    README.md
    ```

    Don't worry, most of these files are not for you to look at, they make the challenge work. The only file you will need to open is `demo.py`.

    **Note:** Files starting with `.` (like `.gitignore`) are hidden by default. They contain configuration or metadata for your project.

1. Open the `demo.py` file and take a look at what is inside.

    You should see just the following:

   ```python
   """Demo module for the Git & Kitt challenge."""


   def hello_world():
       """Returns the string 'Hello World!'"""
       pass  # YOUR CODE HERE
   ```

    Note: `pass` is a placeholder in Python that does nothing. You'll replace it with actual code.

1. Test the files.

    There is a test in your test suite for this challenge, which you can run in the terminal to check that the file is there and contains what we expected.

    💡 This test will fail when we run it now, because the function required to pass is currently missing!

    To run this test easily from your terminal, you can run the following command in your terminal:

   ```bash
   make
   ```

    💡 For this to work, **you must be in the directory (folder) for this challenge in your terminal as shown in the setup for this challenge**. Otherwise the `make` command doesn't know which `Makefile` to implement.

    <details>
    <summary markdown="span">❓What is a Makefile?</summary>

    A Makefile is a special text file that helps you run tasks or commands automatically, so you don’t have to type them out each time.

    Think of it like a recipe book for your computer. Each “recipe” in the Makefile tells your computer what steps to follow to do something, like checking your code or running tests.

    You use a simple command (make) in your terminal, and the Makefile takes care of the rest.

    You don’t need to know how it works inside, just that it saves you time and makes sure you don’t forget any steps!

    </details>

    The output of the tests should look something like this:

    ![Test failures](https://wagon-public-datasets.s3.amazonaws.com/data-analytics/03-Data-Transformation/08-Intro-To-Git-And-Versioning/01-Demo/assertionerror.png)

    The key part of this error to understand is `AssertionError: 'Hello World!' != None`

    This assertion error is the problem we need to solve to get our tests to pass. We will cover this more in the python module, but this error tells us that the test expects the output of our function to be 'Hello World!' and it is currently `None`.

1. Adjust the files to meet the requirements by changing the `hello_world` python function in `demo.py` (the last line is the only line that changes):

   ```python
   def hello_world():
       """Returns the string 'Hello World!'"""
       return "Hello World!"
   ```

    This will change the function so it passes the tests.

1. Save the changes to `demo.py` and run the `make` command again.

    Make sure the test is green before moving to the next step! If it isn't, consult a TA!

    It should look like this:

    ![Test passing](https://wagon-public-datasets.s3.amazonaws.com/data-analytics/03-Data-Transformation/08-Intro-To-Git-And-Versioning/01-Demo/demo_test_pass.png)

## Pushing to Kitt

When `make` is 'happy' and all green, you are ready to push your work to GitHub!

1. Check the current status of your (local) git repository to see the current status of any new or updated files.

   ```bash
   git status
   ```

    If a file has been **changed** since your last commit, then it will be listed in `Changes not staged for commit:`.
    If a file has been **created** since your last commit, then it will be listed in `Untracked files:`, this means you haven't explicitly told git to track it yet.

1. "Stage the changes" by adding the file we updated to git.

   ```bash
   git add demo.py
   ```

1. Commit the changes you have made and add a message to tell everyone what they are.

   ```bash
   git commit --message "Solved the demo challenge of the bootcamp :)"
   ```

1. Push the changes we have committed on our local repository (saved on our computer) to our remote repository on GitHub (`origin`) on the branch (`master`)

   ```bash
   git push origin master
   ```

## 📤 Submission

Shortly after your push is completed, [GitHub will tell Kitt](https://sebastien.saunier.me/blog/2014/04/21/practical-example-of-using-git-in-a-school.html) about this push thanks to a [webhook](https://developer.github.com/webhooks/).

Kitt will then pull your code, run `make` and update your challenge status (completion + style score). You should also see how your buddy of the day is doing!
