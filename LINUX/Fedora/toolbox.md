# TOOLBOX
## THIS IS THE NATIVE FOR FEDORA.
The best practice is to create toolbox before installed the program you will need to work. This is to contain the software and organizes them as well.
We will install [ChatGPT](https://learn.chatgpt.com/docs/linux/linux-app) in Fedora Kinote using the `.rpm` in the downloads folder.
### FRIST CREATE THE TOOLBOX
Create the toolbox by writing
```bach
toolbox create -c chatgpt.env
```
then let enter with in the tool box by entering
```bach
toolbox enter -c chatgpt.emv
```
Once enter type file to download by entering.
```bach
sudo dnf install ~/Downloads/chatgpt.x86_64.rpm
```
Then once enter yes and fully install the the program enter `chatgpt` and it will open and ready to be use.
