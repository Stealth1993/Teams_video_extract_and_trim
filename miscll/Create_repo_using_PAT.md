# **How to Create & Upload a GitHub Repository Using Git Bash (Without gh Command)**

## **Step 1: Navigate to Your Project Folder**
Open Git Bash and move to your project folder:
```bash
cd /path/to/Teams_video_extract_and_trim
```
For example, if your folder is in `C:\Users\YourName`, use:
```bash
cd /c/Users/YourName/Teams_video_extract_and_trim
```

---

## **Step 2: Initialize Git in the Folder**
If the folder is not already a Git repository, initialize it:
```bash
git init
```

---

## **Step 3: Generate a GitHub Personal Access Token (PAT)**
Since GitHub no longer supports password authentication, follow these steps to generate a PAT:
1. Go to **[GitHub Developer Settings](https://github.com/settings/tokens)**.
2. Click **"Generate new token (classic)"**.
3. Give it a **descriptive name** (e.g., "Git CLI Access").
4. Select the following scopes:
   - ✅ `repo` → Full control of private repositories.
   - ✅ `admin:repo_hook` (optional).
   - ✅ `workflow` (optional, if using GitHub Actions).
5. Click **"Generate Token"** and **copy** it (you won't see it again!).

---

## **Step 4: Create a New GitHub Repository Using CLI**
Run the following command, replacing `your_personal_access_token` with the token you copied:
```bash
curl -u "your_git_user_name:your_personal_access_token" https://api.github.com/user/repos -d '{"name":"Teams_video_extract_and_trim", "private":false}'
```
- If you want the repository to be **private**, change `"private":false` to `"private":true`.
- If you receive a `401 Unauthorized` error, ensure you copied the **entire token** and selected the correct permissions.

---

## **Step 5: Add the Remote Repository**
Now, connect your local repository to GitHub:
```bash
git remote add origin https://github.com/your_git_user_name/Teams_video_extract_and_trim.git
git remote -v
```
This ensures your local project is linked to the GitHub repository.

---

## **Step 6: Add and Commit Your Code**
```bash
git add .
git commit -m "Initial commit"
```

---

## **Step 7: Push Code to GitHub**
```bash
git branch -M main  # Rename to main if not already
git push -u origin main
```

---

## **Step 8: Verify on GitHub**
Go to:  
🔗 **https://github.com/your_git_user_name/Teams_video_extract_and_trim**  
and check if your files are uploaded.

---

## **Optional: Secure Your Token Using an Environment Variable**
Instead of pasting the token directly in the `curl` command, store it securely:
1. Run this command (replace with your actual token):
   ```bash
   export GITHUB_TOKEN="your_personal_access_token"
   ```
2. Then, use this modified `curl` command:
   ```bash
   curl -u "your_git_user_name:$GITHUB_TOKEN" https://api.github.com/user/repos -d '{"name":"Teams_video_extract_and_trim", "private":false}'
   ```
This prevents your token from being saved in your command history.

---

## **Done! 🎉**
Your repository is now created and uploaded using only Git Bash. 🚀

