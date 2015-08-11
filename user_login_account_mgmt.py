import sys, os, time
from hashlib import sha512


class user_management():

    def __init__(self, database={}, choice=""):
      self.database = database
      self.choice = choice
      self.initial_check()
      
    def clear(self):
        if os.name in ['nt', 'win32', 'dos']:
            os.system('cls')
        else:
            os.system('clear')
    
    def menu(self):
        print '\n'
        print '-'*50
        print 'Please Select:\n'
        print '-'*50
        print '1) [Register New User]'
        print '2) [View Registered Accounts]'
        print '3) [Login]'
        print '4) [Exit]'
        print '='*50,'\n\n'
  
    def select(self):
        while True:
            self.menu()
            try:
                self.choice = raw_input ('You Entered: ').strip()
            except (KeyboardInterrupt, IOError):
                print '\nAborted! Exiting..'
                time.sleep(2)
                break
            if (self.choice in '1234'):
                if (self.choice == '1'):
                    self.clear()
                    self.register()
                elif (self.choice == '2'):
                    self.clear()
                    self.data_check()
                    self.clear()
                elif (self.choice == '3'):
                    self.clear()
                    self.error_chk()
                    self.clear()
                elif (self.choice == '4'):
                    self.roll_credits()
                    break
                elif (self.choice == ''):
                    self.clear()
                    print '[Invalid Input! Try Again..]\n'    
            else:
                self.clear()
                print '[Invalid Input! Try Again..]\n'


    def register(self):
        try:
            while True:
                print '^'*50
                print 'Welcome To User Registration!'
                print '*'*50
                print '\n\n'
                set_user = (raw_input ('Please Enter User Name: ')).strip()
                if (self.database.has_key(set_user) == True):
                    print '\n\n'
                    print '^'*50
                    print '\n\t\t[User Already Registered]\n'
                    print '='*50
                    time.sleep(2)
                    self.clear()
                    continue
                elif (set_user == ""):
                    print '\n\n'
                    print '^'*50
                    print '\n\t\t[Invalid Username]\n'
                    print '='*50
                    time.sleep(1)
                    self.clear()
                    continue
                else:       
                    set_pw = (raw_input ('\nPlease Enter Password %s: ' % (set_user))).strip()
                if (set_pw == ""):
                    print '\n\n'
                    print '^'*50
                    print '\n\t\t[Invalid Password]\n'
                    print '='*50
                    time.sleep(1)
                    self.clear()
                    continue
                self.data_entry(set_user, set_pw)
                self.clear()
                print '\n'
                print '*'*50
                print 'New User Successfully Registered!'
                print '^'*50
                break
        except (KeyboardInterrupt):
            self.clear()
            print '^'*50
            print '[Returning to Main Menu]'
            print '*'*50
            print '\n\n'
            time.sleep(2)
            self.clear()
            

    def pass_encryption(self, pw):
        p = sha512()
        p.update(pw)
        secure_pass = p.hexdigest()
        return secure_pass


  
    def data_entry(self, set_user, set_pw):
        user = set_user
        pw = set_pw
        sec_pass = self.pass_encryption(pw)
        f = open ('user_data.txt', 'a+')
        j = '%s=%s\n' % (user, sec_pass)
        f.write(j)
        f.close()
        temp_data = {user:sec_pass}
        self.database.update(temp_data)
        temp_data.clear()
        return self.database



    def initial_check(self):
        self.clear()
        print '\n\n'
        print '^'*50
        print '\t[Checking Local Data..]\n'        
        print '='*50
        time.sleep(2)
        db = {}
        a = open('user_data.txt', 'a+')
        c = [i.strip() for i in a.readlines()]
        for i in c:
            j = i.split('=')
            db[j[0]] = j[1]
        self.database.update(db)
        db.clear()
        self.clear()
        return self.database


    
    def data_check(self):
        print '^'*50
        print 'Welcome to Account Management!'
        print '*'*50, '\n'
        print 'Total %d Account(s) Registered' % len(self.database) 
        print '_'*50, '\n\n'
        print '[Checking Account Details..]\n'
        count = 0
        time.sleep(2)
        self.clear()
        if (len(self.database)>0):
            temp_list = self.database.keys()
            print '[Registered Users]'
            print '-'*50
            for junk_val in temp_list[:]:
                count +=1
                print '%d. %s' % (count, junk_val)
            junk_val2 = raw_input('\n\n\t\t<Print Any Key To Continue>')
        else:
            print '[No User Registered]\n'
            print '\n\n[Returning to Main Menu]\n'
            print '='*50
            time.sleep(2)
            


    def error_chk(self):
        try:
            name = raw_input('Enter Username: ').strip()
            password = raw_input('\nEnter Password: ').strip()
        
            while True:
                if (name in self.database.keys()):
                    print ('\n\n[Username Valid! Checking Password for %s..]' % (name))
                    time.sleep(2)
                    if (self.database[name] == self.pass_encryption(password)):
                        print '^'*50
                        print '[+] Access Granted!'
                        print '*'*50
                        time.sleep(1)
                        self.login()
                        break
                    else:
                        print '\n\n[Password Incorrect]\n'
                        print '[Returning to Main Menu]'
                        time.sleep(2)
                        self.clear()
                        break
                else:
                    print '\n\n[-] Acess Denied!\n'
                    time.sleep(1)
                    self.clear()
                    break
        except (KeyboardInterrupt):
            self.clear()
            print '^'*50
            print '[Returning to Main Menu]'
            print '*'*50
            print '\n\n'
            time.sleep(2)
            self.clear()
            


    def login(self):
        print '\n[Feature not implemented yet!]\n\n'
        print '[Returning to Main Menu]'
        time.sleep(3)
        


    def roll_credits(self):
        self.clear()
        print '\n\t', '^'*50, '\n\tQuitting...', '\n\t', '-'*50
        print '\n\tGot Suggestions? Bugs? Email me at : '
        print '\n\tirenicus_timberlake@yahoo.com \n'
        print '\t','*'*50
        time.sleep(3)

    

if __name__ == '__main__':
    global mng
    mng = user_management()
    mng.select()
