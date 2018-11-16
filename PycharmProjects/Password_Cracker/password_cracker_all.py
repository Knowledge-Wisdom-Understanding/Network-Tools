#!/usr/bin/env python

# Doesnt work right now...

import hashlib

counter = 1
available_hashes = hashlib.algorithms_available

pass_in = raw_input("Please enter the Hash: ")
hash_type = raw_input("From the following list: " + '\n' + str([
    'md4',
    'md5',
    'sha1',
    'sha224',
    'sha384',
    'sha256',
    'sha512',
]).strip() + '\nPlease enter the Hash Type: ')
pwfile = raw_input("Please enter the password file name: ")

try:
    pwfile = open(pwfile, 'r')
except IOError:
    print('\nFile Not Found.')
    quit()

for password in pwfile:
    lowercase_hash_type = hash_type.lower()
    if lowercase_hash_type in available_hashes:
        if lowercase_hash_type == 'md5':
            file_hash = hashlib.md5(str(password).encode('utf-8')).hexdigest()
            print(
                'Trying password number %d: %s ' % (counter, password.strip()))
        elif lowercase_hash_type == 'sha1':
            file_hash = hashlib.sha1(str(password).encode('utf-8')).hexdigest()
            print(
                'Trying password number %d: %s ' % (counter, password.strip()))
        elif lowercase_hash_type == 'sha224':
            file_hash = hashlib.sha224(
                str(password).encode('utf-8')).hexdigest()
            print(
                'Trying password number %d: %s ' % (counter, password.strip()))
        elif lowercase_hash_type == 'sha256':
            file_hash = hashlib.sha256(
                str(password).encode('utf-8')).hexdigest()
            print(
                'Trying password number %d: %s ' % (counter, password.strip()))
        elif lowercase_hash_type == 'sha128':
            file_hash = hashlib.sha128(
                str(password).encode('utf-8')).hexdigest()
            print(
                'Trying password number %d: %s ' % (counter, password.strip()))
        elif lowercase_hash_type == 'sha384':
            file_hash = hashlib.sha384(
                str(password).encode('utf-8')).hexdigest()
            print(
                'Trying password number %d: %s ' % (counter, password.strip()))
        elif lowercase_hash_type == 'sha512':
            file_hash = hashlib.sha512(
                str(password).encode('utf-8')).hexdigest()
            print(
                'Trying password number %d: %s ' % (counter, password.strip()))

    counter += 1

    if pass_in == file_hash:
        print('\nMatch Found. \nPassword is: %s' % password)
        break

else:
    print('\nPassword Not Found.')
