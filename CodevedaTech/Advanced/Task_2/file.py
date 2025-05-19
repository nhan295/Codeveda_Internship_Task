# import required module
from cryptography.fernet import Fernet


def encrypt(file_input,save_encrypt):
  
    key = Fernet.generate_key()
    # string the key in a file
    try: 
        with open('filekey.key','wb') as filekey:
            filekey.write(key)

        # open with the key
        with open("filekey.key",'rb') as filekey:
            key = filekey.read()

        fernet = Fernet(key)

        # read original file
        try:
            with open(file_input,'rb') as f:
                word = f.read()   
        except:
            print('File not found')

        encrypted  = fernet.encrypt(word)

        # save result into a new file
        with open( save_encrypt,'wb') as encrypt_file:
            encrypt_file.write(encrypted)
            print('Encrypt successfully')
        with open(file_input,'w+b') as clear_file:
            clear_file.write(b"")
            clear_file.seek(0) # turn back tu head of file
            content = clear_file.read()
            print('File input after encrypt'+ str(content.decode('utf-8')))
        
    except:
        print('Failed to encrypt')
        exit()

# DECRYPT
def decrypt(save_decrypt,file_result):
      # open with the key
    try:
        with open("filekey.key",'rb') as filekey:
            key = filekey.read()

            fernet = Fernet(key)
    
        with open(save_decrypt,'rb') as file:
            content = file.read()
        decrypted = fernet.decrypt(content)

        with open(file_result,'wb') as decrypted_file:
            decrypted_file.write(decrypted)

            print('Decrypt successfully, open file input to see')

    except:
        print('Failed to decrypt')

action = input('Enter e to encrypt and d to decrypt: ')

if(action=='e'):
    file_input = input('Enter a file name to encryption: ')
    save_encrypt = input('Enter a file to save your encrypt data: ')
    encrypt(file_input,save_encrypt)
elif(action=='d'):
    save_decrypt = input('Enter a file you want to decrypt data: ')
    file_result = input('Enter a file name save decrypt data: ')
    decrypt(save_decrypt,file_result)
else:
     print("Invalid option. Use 'e' for encrypt or 'd' for decrypt.")