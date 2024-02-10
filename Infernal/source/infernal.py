#signed by 4cc3s Шрек шарики
#4cc3sTools@protonmail.com

#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣦⣤⣴⣤⣤⣄⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣛⣻⣿⣦⣀⠀⢀⣀⣀⣏⣹⠀
#⢠⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠭⠭⠽⠽⠿⠿⠭⠭⠭⠽⠿⠿⠛ 
#⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⢻⣿⣿⣿⡟⠏⠉⠉⣿⢿⣿⣿⣿⣇⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠁⠀⠀⠀⢠⣿⣿⣿⠋⠑⠒⠒⠚⠙⠸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⣿⣿⡿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

import smtplib
import os
from termcolor import colored, cprint

def send_emails(sender, password, receiver, message, loop_count):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)

        for i in range(loop_count):
            server.sendmail(sender, receiver, message)
            print(f"Email {i+1} sent successfully!")

        server.quit()
        print("All emails sent successfully!")

    except Exception as e:
        print("Error:", e)

def run_inf():
    os.system('clear')
    cprint("""
                    ___                         ___           ___           ___           ___           ___ 
       ___        /  /\          ___          /  /\         /  /\         /  /\         /  /\         /  /
      /__/\      /  /::|        /  /\        /  /::\       /  /::\       /  /::|       /  /::\       /  /:/ 
      \__\:\    /  /:|:|       /  /::\      /  /:/\:\     /  /:/\:\     /  /:|:|      /  /:/\:\     /  /:/  
      /  /::\  /  /:/|:|__    /  /:/\:\    /  /::\ \:\   /  /::\ \:\   /  /:/|:|__   /  /::\ \:\   /  /:/   
   __/  /:/\/ /__/:/ |:| /\  /  /::\ \:\  /__/:/\:\ \:\ /__/:/\:\_\:\ /__/:/ |:| /\ /__/:/\:\_\:\ /__/:/    
  /__/\/:/    \__\/  |:|/:/ /__/:/\:\ \:\ \  \:\ \:\_\/ \__\/~|::\/:/ \__\/  |:|/:/ \__\/  \:\/:/ \  \:\    
  \  \::/         |  |:/:/  \__\/  \:\_\/  \  \:\ \:\      |  |:|::/      |  |:/:/       \__\::/   \  \:\   
   \  \:\         |__|::/        \  \:\     \  \:\_\/      |  |:|\/       |__|::/        /  /:/     \  \:\  
    \__\/         /__/:/          \__\/      \  \:\        |__|:|         /__/:/        /__/:/       \  \:\ 
                  \__\/                       \__\/         \__\|         \__\/         \__\/         \__\/ 
    """, 'red')
    print("")

    yn = input("(1. Run | 2. Exit) ")

    if yn == "1":
        while True:
            os.system('clear')
            cprint("""
                   ___                         ___           ___           ___           ___           ___ 
       ___        /  /\          ___          /  /\         /  /\         /  /\         /  /\         /  /
      /__/\      /  /::|        /  /\        /  /::\       /  /::\       /  /::|       /  /::\       /  /:/ 
      \__\:\    /  /:|:|       /  /::\      /  /:/\:\     /  /:/\:\     /  /:|:|      /  /:/\:\     /  /:/  
      /  /::\  /  /:/|:|__    /  /:/\:\    /  /::\ \:\   /  /::\ \:\   /  /:/|:|__   /  /::\ \:\   /  /:/   
   __/  /:/\/ /__/:/ |:| /\  /  /::\ \:\  /__/:/\:\ \:\ /__/:/\:\_\:\ /__/:/ |:| /\ /__/:/\:\_\:\ /__/:/    
  /__/\/:/    \__\/  |:|/:/ /__/:/\:\ \:\ \  \:\ \:\_\/ \__\/~|::\/:/ \__\/  |:|/:/ \__\/  \:\/:/ \  \:\    
  \  \::/         |  |:/:/  \__\/  \:\_\/  \  \:\ \:\      |  |:|::/      |  |:/:/       \__\::/   \  \:\   
   \  \:\         |__|::/        \  \:\     \  \:\_\/      |  |:|\/       |__|::/        /  /:/     \  \:\  
    \__\/         /__/:/          \__\/      \  \:\        |__|:|         /__/:/        /__/:/       \  \:\ 
                  \__\/                       \__\/         \__\|         \__\/         \__\/         \__\/ 
            """, 'red')
            print("")

            sel = input("""Select:
                [1]. Email Spammer
                [2]. Email Templates
                [3]. Exit
                """)

            if sel == "1":
                sender = input("Sender Email:(Gmail Account) ")
                password = input("Password: ")
                receiver = input("Target Email: ")
                message = input("Message: ")
                loop_count = int(input("Amount: "))

                send_emails(sender, password, receiver, message, loop_count)

                input("Press Enter to continue...")
                
            elif sel == "2":
                print("\nNo Templates :/")
                input("Press Enter to continue...")

            elif sel == "3":
                print("\nBye")
                break

            else:
                print("Invalid selection!")
                input("Press Enter to continue...")

    else:
        print("\nBye")

if __name__ == "__main__":
    run_inf()

