# Xcode & GitHub Setup Guide
### 1. Generating a GitHub Personal Access Token
   
#### Xcode requires a Personal Access Token (PAT) rather than your standard password to securely link with your GitHub account.
- Navigate to Developer Settings: In your GitHub account, go to Settings > Developer settings (at the bottom of the left sidebar).
- Select Token Type: Click on Personal access tokens and specifically choose Tokens (classic). Xcode's integration relies on classic tokens.
- Generate Token: Click Generate new token and select Generate new token (classic).
- Configure Scopes: Add a note to identify the token, then check the following mandatory boxes:
  - `repo` (grants access to repositories)
  - `admin:public_key` (grants access to manage public keys)
  - `user` (grants access to profile and email data)
- Unnecessary Scopes: For a standard setup, you do not need to check `delete_repo` or any of the `GitHub Copilot scopes`.
- Save the Token: Click Generate token at the bottom. Crucial: Copy this token immediately and store it in a secure password manager. GitHub will never display it again.
- 
### 2. Signing In to Xcode
- Open the GitHub sign-in dialog in Xcode.
- Enter your GitHub Account username.
- Paste your generated Personal Access Token into the Token field.
- Click the Sign In button to complete the link.
  
### 3. Configuring Git Author Settings
#### Before you can commit any work, Xcode needs to know who is making the changes.
- Access the Settings: Open a project file and look right above the commit message area. Click the Git Author Settings... button (where it says "No Author"). This opens the Source Control Preferences.
- Set Identity: In the Source Control window, locate the Author name and Author email fields (they will initially say "Not Set"). Click them and enter your details.
- Advanced Settings: * You can safely ignore the advanced workflow checkboxes (like rebasing instead of merging) for a basic setup. • You can also ignore the Ignored Files tab, which is just used to tell Git to ignore certain local build files or directories.
  
### 🛠️ Troubleshooting Checklist
- Authentication Failing? Ensure you generated a classic token, not a fine-grained token, and verify that the `repo`, `admin:public_key`, and `user` scopes are all checked.
- Lost Token? If Xcode prompts you for a token and you no longer have it saved in your password manager, you cannot recover the old one. You must go back to GitHub, delete the old token, and generate a new one using the steps above.
- Commits Not Showing on GitHub? Double-check that the "Author email" you entered in Xcode's Source Control settings exactly matches the primary email address associated with your GitHub account.
