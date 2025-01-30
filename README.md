# Masters_Thesis
Step	Command
Install WSL	wsl --install -d Ubuntu
Check WSL Version	wsl -l -v
Move ZORRO to WSL	mv /mnt/c/Users/YOUR_WINDOWS_USERNAME/Downloads/zorro_linux_x86_64 ~/
Give Execute Permission	chmod +x ~/zorro_linux_x86_64
Move to /usr/local/bin	sudo mv ~/zorro_linux_x86_64 /usr/local/bin/zorro
Add ZORRO to PATH	echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc && source ~/.bashrc
Verify ZORRO Installation	zorro -h
