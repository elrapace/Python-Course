from argon2 import PasswordHasher
import time

# CREAZIONE OGGETTO HASCHER
g_ph = PasswordHasher()

# HASHING
g_otp = 'password12345'
g_start_time = time.time()
g_hashed_otp = g_ph.hash(g_otp)
g_end_time = time.time()

print(f'HASHED OPT: {g_hashed_otp}')
print(f"TIME: {g_end_time-g_start_time:.6f} SECONDS")

try:
    g_ph.verify(g_hashed_otp,g_otp)
    print(f"HASH CHECK: {g_ph.check_needs_rehash(g_hashed_otp)}")
    print(f"OK")
except:
    print("NOT OK")