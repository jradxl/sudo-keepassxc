import sys, pykeepass, getpass, platform

def main():
    password = getpass.getpass("Your KeepassXC Password: ")
    try:
        kp = pykeepass.PyKeePass('/home/jradley/.keepassxc/db.kdbx', password=password)
    except Exception as err:
        print("ERROR:", err)
        sys.exit(1)

    hostname = platform.node()
    username = getpass.getuser()

    #Find an entry by its title, where that is the hostname
    try:
        entry = kp.find_entries(title=hostname, username=username, first=True)
    except Exception as err:
        print("ERROR: ", err)
        sys.exit(1)

    if entry is None:
        print("ERROR: No entry found in database.")
        sys.exit(1)
    else:
        print(entry.password)

if __name__ == '__main__':
    main()
