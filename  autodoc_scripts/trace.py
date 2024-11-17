import argparse
import pprint
import argparse
import pprint
import asyncio
import tracemalloc
import os

# parser = argparse.ArgumentParser(    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# parser.add_argument('--proto', help='protocol to fetch', choices=['inet', 'inet6'], default='inet')
# parser.add_argument('-a','--aaa', help='aaa', choices=['a', 'a2'], default='a')

# args = parser.parse_args()

# pprint.pprint(parser.__dict__['_action_groups'][1].__dict__)
import sys
import gc
import tracemalloc
import os
class RefCounter:
    def __init__(self):
        self.count = 0
    
    def __enter__(self):
        self.count += 1
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.count -= 1
        if self.count == 0:
            gc.collect()

class MultiTracker:
    def __init__(self):
        self.ref_counter = RefCounter()
        self.tracemalloc = tracemalloc
        self.process_id = os.getpid()
    def create_traffic(self,tracker):
        print(f"Prozess-ID: {tracker.get_process_id()}")
        with open("example.txt", "w") as f:
            for i in range(1000):
                print(self.tracemalloc.get_traced_memory())
                f.write(f"Zeile {i}\n")

        with open("example.txt", "r") as f:
            for line in f:
                print(self.tracemalloc.get_traced_memory())
                print(line.strip())

        with open("example2.txt", "w") as f:
            for i in range(1000):
                print(self.tracemalloc.get_traced_memory())
                f.write(f"Zeile {i}\n")
            return 1
    def track_object(self, obj):
        with self.ref_counter:
            self.tracemalloc.start()
            result = obj()
            current, peak = self.tracemalloc.get_traced_memory()
            print(f"Objekt erstellt: {result}")
            print(f"Speicherverbrauch: {current / 10**6:.1f} MB")
            print(f"Höhe des Speichers: {peak / 10**6:.1f} MB")
            return result
    
    def stop_tracking(self):
        self.tracemalloc.stop()
        print("\nSpeicherprofil:")
        for stat in self.tracemalloc.get_traced_memory():
            print(stat)
    
    def get_process_id(self):
        return self.process_id


# Beispiel für die Verwendung
async def create_object():
# result = object()
# print(f"Objekt erstellt: {result}")
# #await asyncio.sleep(5)  # Warte 5 Sekunden
    result = await create_object()
    result.create_traffic(result)
    result.stop_tracking()
    return  MultiTracker()

async def main():
   
    traffic= await create_object()
    

asyncio.run(main())