#!/usr/bin/env python3
'''
    passwords.py
    Robbie Young, 9th May 2022
'''

import hashlib
import binascii
from re import L

def load(file):
    hash_dict = {}
    for line in open(file):
        split_line = line.strip().lower().split(":")
        hash_dict[split_line[1]] = split_line[0]

    return hash_dict

def passwords1(hash_dict):
    user_list = hash_dict.values()
    word_list = [line.strip().lower() for line in open('words.txt')]
    write_file = open('cracked1.txt', 'w')

    for this_word in word_list:
        encoded_password = this_word.encode('utf-8')
        hasher = hashlib.sha256(encoded_password)
        digest = hasher.digest()
        digest_as_hex = binascii.hexlify(digest)
        digest_as_hex_string = digest_as_hex.decode('utf-8')
        for this_user in user_list:
            if digest_as_hex_string in hash_dict:
                if hash_dict[digest_as_hex_string] == this_user:
                    write_file.write(this_user + ":" + this_word + "\n")

    write_file.close()

def passwords2(hash_dict):
    count = 0
    iteration_count = 0
    hit_count = 0

    user_list = hash_dict.values()
    word_list = [line.strip().lower() for line in open('words.txt')]
    write_file = open('cracked2.txt', 'w')

    for this_word in word_list:
        iteration_count = iteration_count + 1
        for other_word in word_list:
            concatenated_word = this_word + other_word
            encoded_password = concatenated_word.encode('utf-8')
            hasher = hashlib.sha256(encoded_password)
            digest = hasher.digest()
            digest_as_hex = binascii.hexlify(digest)
            digest_as_hex_string = digest_as_hex.decode('utf-8')
            for this_user in user_list:
                if digest_as_hex_string in hash_dict:
                    if hash_dict[digest_as_hex_string] == this_user:
                        hit_count = hit_count + 1
                        write_file.write(this_user + ":" + concatenated_word + "\n")
            
            length = len(word_list)
            if (count % 100000 == 0):
                print("passwords2:" + str(hit_count) + ":" + str(100*iteration_count/length) + "%")
            
            count = count + 1

    write_file.close()

def passwords3(file):
    count = 0
    iteration_count = 0
    hit_count = 0

    salt_list = []
    hash_dict = {}
    for line in open(file):
        split_line = line.strip().lower().split(":")
        salt_hash = split_line[1].split("$")
        salt_list.append(salt_hash[2])
        hash_dict[salt_hash[3]] = split_line[0]
    
    user_list = hash_dict.values()
    word_list = [line.strip().lower() for line in open('words.txt')]
    write_file = open('cracked3.txt', 'w')

    for this_word in word_list:
        iteration_count = iteration_count + 1
        for this_salt in salt_list:
            salt_word = this_salt + this_word
            encoded_password = salt_word.encode('utf-8')
            hasher = hashlib.sha256(encoded_password)
            digest = hasher.digest()
            digest_as_hex = binascii.hexlify(digest)
            digest_as_hex_string = digest_as_hex.decode('utf-8')
            for this_user in user_list:
                if digest_as_hex_string in hash_dict:
                    if hash_dict[digest_as_hex_string] == this_user:
                        hit_count = hit_count + 1
                        write_file.write(this_user + ":" + this_word + "\n")
            
            length = len(word_list)
            if (count % 100000 == 0):
                print("passwords3:" + str(hit_count) + ":" + str(100*iteration_count/length) + "%")
            
            count = count + 1


def main():
    # hash_dict = load("passwords1.txt")
    # passwords1(hash_dict)
    # count = 0

    # hash_dict = load("passwords2.txt")
    # passwords2(hash_dict)
    # count = 0

    # passwords3("passwords3.txt")
    # count = 0

    pass

if __name__ == "__main__":
    main()