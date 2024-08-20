from hdwallet import BIP84HDWallet
from hdwallet.cryptocurrencies import BitcoinMainnet
from concurrent.futures import ProcessPoolExecutor, as_completed
import itertools
import string
import time

def проверка_на_мнемоник(passphrase):
    try:
        wallet = BIP84HDWallet(cryptocurrency=BitcoinMainnet)
        wallet.from_mnemonic(
            mnemonic='blossom educate state course sick fresh color divide number soap please pull glide weather join grit depart dynamic tenant leopard alter piano slight room',
            passphrase=passphrase
        )
        address = wallet.address()
        return passphrase, address
    except Exception as e:
        return passphrase, None

def парола_генератор(min_length=1, max_length=5):
    characters = string.ascii_lowercase + string.digits
    for length in range(min_length, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            yield ''.join(combination)

def main():
    print("Започва обработката на паролите...")

    num_workers = 61
    print_interval = 1000  # Print every 1000 combinations for progress

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        future_to_passphrase = {}
        completed = 0
        total_combinations = sum(len(string.ascii_lowercase + string.digits) ** i for i in range(1, 8))

        start_time = time.time()

        for passphrase in парола_генератор(min_length=1, max_length=5):
            future = executor.submit(проверка_на_мнемоник, passphrase)
            future_to_passphrase[future] = passphrase

            for future in as_completed(future_to_passphrase):
                passphrase = future_to_passphrase[future]
                try:
                    резултат_passphrase, address = future.result()
                    if address == 'bc1qcyrndzgy036f6ax370g8zyvlw86ulawgt0246r':
                        print(f"\nУспех! Открита парола: {passphrase}")
                        return
                except Exception as e:
                    pass

                completed += 1
                if completed % print_interval == 0 or completed == total_combinations:
                    elapsed_time = time.time() - start_time
                    progress = (completed / total_combinations) * 100
                    print(f"\rНапредък: {progress:.2f}% ({completed}/{total_combinations}), Време: {elapsed_time:.2f}s", end='')

        print("\nОбработката завърши без успех.")

if __name__ == "__main__":
    main()
