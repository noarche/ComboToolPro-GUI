# ComboToolPro-GUI
Manipulate Email:Pass combo, All in one tool. 
![screenshot](https://github.com/noarche/ComboToolPro-GUI/blob/main/September%2024%202023%200352%20AM.jpg?raw=true)
![screenshot](https://github.com/noarche/ComboToolPro-GUI/blob/main/September%2023%202023%200158%20PM.jpg?raw=true)
![screenshot](https://github.com/noarche/ComboToolPro-GUI/blob/main/September%2023%202023%200158%20PM%20(1).jpg?raw=true)
![screenshot](https://github.com/noarche/ComboToolPro-GUI/blob/main/September%2023%202023%200159%20PM.jpg?raw=true)

# Updates: 
Added Email2user.py script. Convert email:pass to User:pass. 
# Updates: 
v1.1.1 - ignores case on for domain when extracting and analysis

# About
This is a GUI for the CLI tool https://github.com/noarche/ComboScriptPro. The functionality is the same however it works with text boxes instead of input and output text files. 




# Help: What the options are: (options have been changed to buttons in the GUI but perform the same task)

        Option 1; To extract all lines for earthlink.net enter @earthlink.net | If you want to extract all .net domains enter .net | This will create text documents named what you enter | When extracting lines are appended and never overwrite.
       
				Option 2; Remove duplicate lines from input.txt & saves to output.txt | Output.txt gets overwritten so always move it or rename it. 
        
				Option 3; Splits Email from Password, saves to extracted_emails.txt(is Overwrite each time you run task) | Good for mailing list or if you need to split for dehashing passwords.
        
				Option 4; Same as option 3 but with passwords, extracted_passwords.txt(is Overwrite each time you run task).
        
				Option 5; Extract URLs from input.txt | Append save to extracted_URL.txt  
        
				Option 6; Organize input.txt A-Z | Overwrite output.txt
        
				Option 7; Use lines from input.txt to name new directorys | Do not use this option unless you have a reason!
        
				Option 8; Extract lines from input.txt if the password is MD5 hashed | Append save to extracted_hashed.txt | Use to create your own private combo that has not been cracked yet | A popular dehashing script is HASHCAT OCL. 
        
				Option 9; Drop files in the directory toCombine that you need to combine | Good idea to remove duplicates after | Overwrite output.txt
        
				Option 10; Enter the number of lines you want to split combo by then name your splits | creates directory to save your splits in.
        
				Option 11; After dehashing your hashed passwords use this to rejoin back with email addresses | The files it looks for to join are extracted_emails.txt and extracted_passwords.txt | overwrite JoinedOutput.txt
        
				Option 12; Strip capture results from combo | append save cleanedOutput.txt
        
				Option 13; Extract all domains by domain to seperate text files | append save
        
				Option 14; Analyze input.txt and display Top Domains, Number of lines, and the % of combo | Only .net domains
        
				Option 15; Analyze input.txt and display Top Domains, Number of lines, and the % of combo | All domains
        
				Option 0; Exit



## Support

Drop a tip

    (BTC) address bc1qnpjpacyl9sff6r4kfmn7c227ty9g50suhr0y9j
    
    (ETH) address 0x94FcBab18E4c0b2FAf5050c0c11E056893134266
    
    (LTC) address ltc1qu7ze2hlnkh440k37nrm4nhpv2dre7fl8xu0egx



![noarche's GitHub stats](https://github-readme-stats.vercel.app/api?username=noarche&show_icons=true&theme=transparent)


# Need Proxylist?

Check out my proxylist repo for free API links. 

https://github.com/noarche/proxylist-socks5-sock4-exported-updates

# Looking for a great dork generator? 

Check out my Dork Generator, inspired by The n3r0x

https://github.com/noarche/dorkGen

