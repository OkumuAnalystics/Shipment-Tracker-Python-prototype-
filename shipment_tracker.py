"""Shipment Tracker: a small Python prototype for tracking shipments and delivery regions.

Built as a course project to practise dictionaries and sets.
Data lives in memory only, so it resets every time the program runs.
"""
import time


def update_status(shipments, shipment_id, new_status):
    """Change the status of an existing shipment (adds it if the ID is new)."""
    shipments[shipment_id] = new_status


def remove_shipment(shipments, shipment_id):
    """Remove a shipment safely: returns its last status, or None if it was not found."""
    return shipments.pop(shipment_id, None)


def get_status(shipments, shipment_id):
    """Look up a shipment by ID, with a friendly message for unknown IDs."""
    return shipments.get(shipment_id, "Shipment not found")


def print_report(shipments):
    """Print every shipment ID with its current status."""
    print("--- Daily report ---")
    for shipment_id, status in shipments.items():
        print(f"{shipment_id}: {status}")


def compare_regions(north, south):
    """Use set operations to compare the cities served by two regions."""
    print("All cities served:", sorted(north | south))    # union
    print("Served by both:   ", sorted(north & south))    # intersection
    print("North only:       ", sorted(north - south))    # difference
    print("South only:       ", sorted(south - north))    # difference (order matters)


def speed_test(size=100_000, repeats=1000):
    """Compare list search with dictionary lookup. Results vary from computer to computer."""
    ids = [f"SHP{n}" for n in range(size)]
    lookup = {shipment_id: "Pending" for shipment_id in ids}
    target = f"SHP{size - 1}"                  # worst case: the last item in the list

    start = time.perf_counter()
    for _ in range(repeats):
        target in ids                          # list: checks items one by one
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    for _ in range(repeats):
        lookup[target]                         # dictionary: hash table jump
    dict_time = time.perf_counter() - start

    print(f"List : {list_time:.3f} s for {repeats:,} lookups")
    print(f"Dict : {dict_time:.5f} s for {repeats:,} lookups")


if __name__ == "__main__":
    shipments = {"SHP101": "Delivered", "SHP102": "In Transit", "SHP103": "Pending"}

    update_status(shipments, "SHP102", "Delivered")     # update a status
    update_status(shipments, "SHP104", "In Transit")    # add a new shipment
    remove_shipment(shipments, "SHP101")                # remove a completed shipment

    print("Status of SHP103:", get_status(shipments, "SHP103"))
    print("Unknown ID:", get_status(shipments, "SHP999"))
    print()
    print_report(shipments)

    print("\n--- Region comparison ---")
    compare_regions({"New York", "Dallas", "Miami"}, {"Miami", "Atlanta", "Dallas"})

    print("\n--- Speed test ---")
    speed_test()
