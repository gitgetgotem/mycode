#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails

loginpass = 0 # counter for passes

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            print(line.split(" ")[-1])
        elif "-] Authorization failed" in line: # if this 'pass' appears..
            loginpass +=1 # same as loginfail

print("The number of failed log in attempts is", loginfail)
print(f"The number of succesful login attempts is {loginpass}")
