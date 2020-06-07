import hashlib # common interface to many hashing functions
import uuid # universally unique identifier 
print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

# initialize using sha256
print('\nExample for SHA256')
m = hashlib.sha256()
# append string one after another in bytes
m.update(b"This is a")
m.update(b" demo of using hashlib SHA256.")
print('Output 1 :', m.digest()) # digest method

# use the whole string at once in bytes
x = hashlib.sha256(b"This is a demo of using hashlib SHA256.")
print('Output 2 :', x.digest())

# initialize using md5
print('\nExample for md5')
m = hashlib.md5()
# append string one after another in bytes
m.update(b"This is a")
m.update(b" demo of using hashlib md5.")
print('Output 1 :', m.digest())

# use the whole string at once in bytes
x = hashlib.md5(b"This is a demo of using hashlib md5.")
print('Output 2 :', x.digest())
"""
Output for the above hashlib functions.
{'shake_256', 'sha1', 'sha3_256', 'blake2s', 'sha224', 'sha3_224', 'sha3_512', 'sha384', 'sha3_384', 'shake_128', 'sha512', 'blake2b', 'md5', 'sha256'}
{'shake_256', 'sha1', 'sha3_256', 'blake2s', 'sha224', 'sha3_224', 'sha3_512', 'sha384', 'sha3_384', 'shake_128', 'sha512', 'blake2b', 'md5', 'sha256'}

Example for SHA256
Output 1 : b"!\xecu\xc1\xa8s%&\xb6`\xc2\x90\x1e\xd1G#\xb8|\x84JZ\xad\xb7iL\x9fF\x9flu'\xb3"
Output 2 : b"!\xecu\xc1\xa8s%&\xb6`\xc2\x90\x1e\xd1G#\xb8|\x84JZ\xad\xb7iL\x9fF\x9flu'\xb3"

Example for md5
Output 1 : b'\xb3\xbf\x97\xd2\n\xb7l u\xae\x8a\xbex\xd6\xe2e'
Output 2 : b'\xb3\xbf\x97\xd2\n\xb7l u\xae\x8a\xbex\xd6\xe2e'
"""

#how to create password using md5()
def PasswordCreate():
  inputVar = input(str("Please enter a Password : "))
  password = hashlib.md5()
  password.update(inputVar.encode("utf-8"))
  return password.hexdigest() # hexdigest method

# Create Variable for dipslaying encoded value.
displayPass = PasswordCreate()
print("User Password is: ",displayPass)
#Please enter a password : This is a demo of using hashlib md5
#User Password is:  44eddca98e8da84b710b7bb4a16552c4

print()

# Password create(using sha256) then check if password is correct
def hash_pwd(pwd):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + pwd.encode()).hexdigest() + ':' + salt
    
def check_pwd(hashed_pwd, user_pwd):
    pwd, salt = hashed_pwd.split(':')
    return pwd == hashlib.sha256(salt.encode() + user_pwd.encode()).hexdigest()
 
new_pass = input('Please enter password: ')
hashed_pwd = hash_pwd(new_pass)
print('The string to store in the db is: ' + hashed_pwd)
old_pass = input('Now please enter the password again to check: ')
if check_pwd(hashed_pwd, old_pass):
    print('You entered the right password,please proceed')
else:
    print('I am sorry but the password does not match')
