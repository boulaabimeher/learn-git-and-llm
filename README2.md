# Git Branching Guide

This document explains how to create, switch, and manage branches in Git.

---

## 1️⃣ Check current branch

```bash
git branch
The * indicates the branch you are currently on.

2️⃣ Create a new branch
bash
Copy code
git branch feature-login
This creates a new branch called feature-login.

3️⃣ Switch to the new branch
bash
Copy code
git switch feature-login
Or using the older command:

bash
Copy code
git checkout feature-login
Now all changes you make will be on this branch only.

4️⃣ Make changes and commit
bash
Copy code
# Edit your files
git add .
git commit -m "Add login functionality"
These commits exist only on the feature-login branch.

5️⃣ Push the branch to GitHub
bash
Copy code
git push -u origin feature-login
This uploads your branch to GitHub.

6️⃣ Switch back to main
bash
Copy code
git switch main
Your changes on feature-login won’t affect main until merged.

7️⃣ Merge a branch into main
bash
Copy code
git switch main
git merge feature-login
Merges the changes from feature-login into main.

8️⃣ Delete a branch (optional cleanup)
bash
Copy code
git branch -d feature-login
Deletes the branch locally after merging. Use -D to force delete without merging.

💡 Tips
Keep commits small and descriptive.

Branches are perfect for features, bug fixes, or experiments.

Use git branch to see all local branches, and git branch -r for remote branches.