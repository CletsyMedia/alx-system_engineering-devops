# The CMD Line for Win Challenge

![CMD Challenge](https://static-assets.codecademy.com/assets/course-landing-page/meta/16x9/learn-the-command-line.jpg)

## Welcome to the CMD CHALLENGE

Embark on a thrilling journey through the [CMD CHALLENGE](https://cmdchallenge.com/#/count_string_in_line), an immersive game meticulously crafted to elevate your Bash scripting prowess. This captivating experience invites you to explore the depths of command line wizardry, offering a series of tasks that will not only challenge but refine your skills in the art of Bash.

## Requirements 📚✨

**General:**

- **README.md File:** Mandatory at the project root.
- **Manual Review:** Each completed task turns green.
- **Screenshots:** PNG or JPEG format for each task pushed to GitHub.

**Specific:**

- **SFTP Demonstration:** Use SFTP for file transfer to the sandbox environment.

## Useful Links for the Challenge 🖇️🔗

- [CMD Challenge](https://cmdchallenge.com/#/count_string_in_line)
- [How to use SFTP](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server)
- [Solve the Challenge](https://systemweakness.com/command-line-challenge-javad-solves-b591febae230)

## SFTP File Transfer Steps 🚌🚇

1. **Capture Screenshots:**
   - After you have taken the screenshots from the completed levels of the challenge, `cd` into `root/alx-system_engineering-devops/command_line_for_the_win/`. Adjust the path accordingly if not using the sandbox.

2. **Open the Terminal (Preferred CLI):**
   - Launch a terminal or command prompt on your local machine.

3. **Connect via SFTP:**
   - Use SFTP to connect to the sandbox environment using the provided hostname, username, and password. Copy them respectively to your preferred CLI (Command Line Interface).

4. **Navigate to Destination:**
   - Move to the desired directory in the sandbox environment. Example:

     ```bash
     cd root/alx-system_engineering-devops/command_line_for_the_win/.
     ```

5. **Upload the Screenshots:**
   - Employ the SFTP `put` command to transfer screenshots from your local machine. Copy the file location from your machine's GUI, then use the `put` command to transfer it remotely to your sandbox. Example for those using WSL and GitBash:

     ```bash
     # WSL
     sftp put /mnt/c/Users/Admin/Downloads/2-next_9_tasks.png

     # GitBash
     sftp put c/Users/Admin/Downloads/2-next_9_tasks.png
     ```

6. **Confirm Transfer:**
   - Verify the successful transfer by checking the sandbox directory.

7. **Push to GitHub:**
   - Push the transferred screenshots to GitHub as per the initial requirements.

With these steps above, you have successfully completed the **Command Line For Win Challenge**👌👌👌.

## Feedback 📢🚀

Feel free to reach out to [CletsyMedia](https://github.com/CletsyMedia) for any challenges you may encounter.

Thanks 🙏🙏🙏🙏🙏

## Author 🖋️

&copy;2023 All Rights Reserved [CletsyMedia](https://cletsymedia.github.io/Prof-Portfolio/)
