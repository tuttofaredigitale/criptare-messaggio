from cryptography.fernet import Fernet

def gen_key():
  key = Fernet.generate_key()
  with open('secret.key', 'wb') as kfile:
    kfile.write(key)

def read_key():
  return open('secret.key', 'rb').read()

def c_mes(mes):
  key = read_key()
  m_encoded = mes.encode()
  f = Fernet(key)
  encrypted_message = f.encrypt(m_encoded)
  print(encrypted_message)

def dec_mes(mes):
  key = read_key()
  f = Fernet(key)
  dec_mes = f.decrypt(mes)
  print(dec_mes.decode())  

with open('secret.key') as f:
  if f.read() == '':
    gen_key()

c_mes('Questo è un messaggio segreto!')
dec_mes(b'gAAAAABfs6jh4DQ00Z0YjseJy1ktNAUTLUYIT-k-Iz5M2QcdEYK5TJtUHX67iuewZ1DEEPoex1z9eOpunl9bGcd9Dc9Xl6GR2g_vtoD_o2LcycW2LB5O7VQ=') 
