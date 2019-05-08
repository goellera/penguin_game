import subprocess
push_git = 0

while True:
	if push_git == 1:
		more_git = input("Would you like to make another update to git? (Y/N): ")
		while more_git != "n" and more_git != "y":
			print("Enter 'Y' for Yes and 'N' for No")
			more_git = input("Would you like to make another update to git? (Y/N): ")
		if more_git == "n":
			break
		
	subprocess.Popen('powershell.exe git add -u; git status')
	
	add_file = input("Would you like to track any additional files? (Y/N): ").lower()
	while add_file != "n" and add_file != "y":
		print("Enter 'Y' for Yes and 'N' for No")
		add_file = input("Would you like to track any additional files? (Y/N): ").lower()
	
	while add_file == "y":
		file_name = input("Enter the name of the file you would like to start tracking: ")
		subprocess.Popen('powershell.exe git add ' + str(file_name) + '; git status')
		end = input("Would you like to add another file? (Y/N): ").lower()
		if end == "n":
			break
		while end != "n" and end != "y":
			print("Enter 'Y' for Yes and 'N' for No")
			end = input("Would you like to add another file? (Y/N): ").lower()
	
	comment = input("Enter a comment: ")
	Verify = input("Would you like to commit and push? (Y/N): ").lower()
	while Verify != "n" and Verify != "y":
		print("Enter 'Y' for Yes and 'N' for No")
		Verify = input("Would you like to commit and push? (Y/N): ").lower()
	if Verify == "y":
		subprocess.Popen('powershell.exe git commit -m "' + str(comment) + '"; git push')
		push_git = 1
		
