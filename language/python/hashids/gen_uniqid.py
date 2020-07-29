import os
import socket
import threading
import ipaddress
import random
from datetime import datetime
from hashids import Hashids


class SimpleUniqueIdGenerator:
    """
    Simple Unique id generator for transaction unique id using hashids lib

    https://hashids.org/

    Features
    * Create short unique ids from numbers (positive numbers & zero).
    * Allow custom alphabet as well as salt — so ids are unique only to you.
    * Incremental input is mangled to stay unguessable.
    * Code is tiny (~350 lines), fast and does not depend on external libraries.

    Collision
    * There are no collisions because the method is based on integer to hex conversion.
    * As long as you don't change constructor arguments midway,
      the generated output will stay unique to your salt.

    Avoid collisions for distributed systems
    * counter (if you have one) + timestamp (even better if in milliseconds) +
      some system value (either an IP address or some machine id) + a random integer.

    Fixed length output
    * eaRP9qmXBxX1mN4pakw46V6z95
    * w0dEn0Yk6eL4WmvAP1VArnJZ8o
    """
    counter_min = 1000
    counter_max = 9999

    def __init__(self, salt='some-salt-key'):
        self.counter = self.counter_min

        process_id = str(os.getpid())
        thread_id = str(threading.get_ident())
        self.__init_random_seed(process_id, thread_id)

        self.hash_build_base = self.__get_hash_build_base(process_id, thread_id)
        self.hash_builder = Hashids(
                salt=salt,
                min_length=20,
                alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
                )

    def __init_random_seed(self, process_id, thread_id):
        timestamp = datetime.today().timestamp()
        timestamp = int(timestamp * 1000000)
        seed_str = f'{process_id}{thread_id}{timestamp}'
        random.seed(int(seed_str))

    def __get_hash_build_base(self, process_id, thread_id):
        """hash build base string for collision avoidance"""
        process_short_id = process_id[-3:] if len(process_id) >= 3 else process_id
        thread_short_id = thread_id[-4:] if len(thread_id) >= 4 else thread_id

        try:
            ip_addr_str = socket.gethostbyname(socket.getfqdn())
        except socket.gaierror:
            ip_addr_str = '127.0.0.1'

        ip_addr_int = int(ipaddress.ip_address(ip_addr_str))

        # Collision avoidance machine(or container)
        #  - IP Address + Process Id + Thread Id
        return f'{ip_addr_int}{process_short_id}{thread_short_id}'

    def __inc_counter(self):
        self.counter += 1
        if self.counter > self.counter_max:
            self.counter = self.counter_min

    def generate(self, prefix=None):
        timestamp = datetime.today().timestamp()
        timestamp = int(timestamp * 1000000)
        random_num = random.randint(10000, 99999)

        # Collision avoidance concurrency
        #  -  Counter + Timestamp + ...  + Random number
        text = f'{self.counter}{timestamp}{self.hash_build_base}{random_num}'
        key = self.hash_builder.encode(int(text))

        self.__inc_counter()

        if prefix:
            return f'{prefix}_{key}'
        return key


if __name__ == "__main__":
    uniqid = SimpleUniqueIdGenerator(salt='a1s2d3')
    tid = uniqid.generate()
    print(tid)

