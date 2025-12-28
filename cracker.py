import hashlib
import time

def visualize_crack():
    print("""
    ██████╗  █████╗ ███████╗███████╗    ██████╗██████╗  █████╗  ██████╗██╗  ██╗
    ██╔══██╗██╔══██╗██╔════╝██╔════╝   ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
    ██████╔╝███████║███████╗███████╗   ██║     ██████╔╝███████║██║     █████╔╝ 
    ██╔═══╝ ██╔══██║╚════██║╚════██║   ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ 
    ██║     ██║  ██║███████║███████║   ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    ---------------------------------------------------------------------------
    🚨 AUTOMATED HASH CRACKING TOOL V1.0
    ---------------------------------------------------------------------------
    """)

def get_hash(password):
    """Converts a plaintext password into an MD5 hash."""
    return hashlib.md5(password.encode()).hexdigest()

def brute_force(target_hash, wordlist_file):
    """Tries every word in the file to see if it matches the target hash."""
    print(f"[*] Starting Brute Force Attack on hash: {target_hash}")
    print("[*] Loading wordlist...")
    
    attempts = 0
    start_time = time.time()
    
    try:
        with open(wordlist_file, 'r') as file:
            for line in file:
                word = line.strip()
                attempts += 1
                
                # Check if this word's hash matches the target
                word_hash = get_hash(word)
                
                if word_hash == target_hash:
                    end_time = time.time()
                    print(f"\n✅ PASSWORD CRACKED: {word}")
                    print(f"⚡ Time taken: {round(end_time - start_time, 2)} seconds")
                    print(f"🔢 Attempts: {attempts}")
                    return word
                
        print("\n❌ Password not found in dictionary.")
        return None

    except FileNotFoundError:
        print("❌ Error: Wordlist file not found!")

# --- MAIN PROGRAM ---
if __name__ == "__main__":
    visualize_crack()
    
    # 1. Ask the user for a target hash (simulating a stolen database)
    print("Select Mode:")
    print("1. Encrypt a password (Create Hash)")
    print("2. Crack a password (Brute Force)")
    
    choice = input("\nEnter choice (1/2): ")
    
    if choice == '1':
        pw = input("Enter password to encrypt: ")
        print(f"🔒 MD5 Hash: {get_hash(pw)}")
        
    elif choice == '2':
        target = input("Enter the MD5 Hash to crack: ")
        wordlist = "passwords.txt"
        brute_force(target, wordlist)
    
    else:
        print("Invalid choice.")