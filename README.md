[README.md](https://github.com/user-attachments/files/34687901/README.md)
# Shipment Tracker (Python prototype)

A small Python prototype that tracks shipments by ID and compares the delivery cities of two regions.
I built it while learning Python to practise **dictionaries** and **sets** on a logistics-style problem.

> This is a learning project, not a production system. Data is kept in memory only, so it resets every time the program runs.

## What it does

| Feature | Python tool |
|---|---|
| Store each shipment's status by its unique ID | dictionary (`{id: status}`) |
| Look up a status, with a friendly message for unknown IDs | `get(key, default)` |
| Update a status, add a shipment, remove a completed one | `d[key] = value`, `pop(key, None)` |
| Daily report of every ID and status | `items()` |
| All cities served, cities in both regions, cities in one region only | set `|`, `&`, `-` |
| Compare list search with dictionary lookup | `time.perf_counter()` |

## Run it

Requires Python 3.8 or later. No extra packages.

```
python shipment_tracker.py
```

## Example output

```
Status of SHP103: Pending
Unknown ID: Shipment not found

--- Daily report ---
SHP102: Delivered
SHP103: Pending
SHP104: In Transit

--- Region comparison ---
All cities served: ['Atlanta', 'Dallas', 'Miami', 'New York']
Served by both:    ['Dallas', 'Miami']
North only:        ['New York']
South only:        ['Atlanta']
```

The speed test prints different timings on every computer. In my runs, 1,000 lookups among 100,000 shipment IDs took roughly half a second with a list and a tiny fraction of a millisecond with a dictionary.

## What I learned

- A dictionary finds a record through a hash table instead of checking items one by one, so lookups stay fast as the data grows.
- `dict.get()` and `dict.pop(key, None)` avoid crashes on missing IDs.
- Sets remove duplicates automatically, and `north - south` is not the same as `south - north`.
- Sets only remove exact duplicates, so text such as "Miami" and "miami " should be cleaned first.

## Ideas for next steps

- Save shipments to a CSV or JSON file so data survives between runs
- Turn the shipment and region logic into classes
- Add input checks and error handling for bad shipment IDs
