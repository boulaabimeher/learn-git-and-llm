We will learn the first steps to work with git : 

✅ 1. Check if Git is installed
git --version


If it’s not installed:

sudo apt install git        # Ubuntu/Debian
sudo dnf install git        # Fedora
sudo pacman -S git          # Arch

✅ 2. Set your Git identity (only once per system)

These details appear in your commits:

git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"

✅ 3. Go to your project directory

Example:

cd /path/to/your/project

✅ 4. Initialize Git in the project
git init


This creates a .git/ folder that tracks changes.

✅ 5. Add a remote GitHub repository
First, create an empty repo on GitHub (no README, no .gitignore).

Then copy the SSH URL, which looks like:

git@github.com:username/repository.git


Add it to your local project:

git remote add origin git@github.com:username/repository.git


Check it:

git remote -v

✅ 6. Add your project files and make the first commit
git add .
git commit -m "Initial commit"

✅ 7. Push your code to GitHub

For the first push:

git branch -M main   # rename branch to main (optional but recommended)
git push -u origin main


After this, you can simply do:

git push

🎉 Done! Your project is now on GitHub.