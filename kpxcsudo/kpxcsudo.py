import pykeepass, getpass, platform

def main():
    password = getpass.getpass("Your KeepassXC Password: ")
    kp = pykeepass.PyKeePass('/home/jradley/.keepassxc/db.kdbx', password=password)

    hostname = platform.node()
    username = getpass.getuser()

    #Find an entry by its title, where that is the hostname
    entry = kp.find_entries(title=hostname, username=username, first=True)
    print(entry.password)

if __name__ == '__main__':
    main()
