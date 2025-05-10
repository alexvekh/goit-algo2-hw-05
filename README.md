# 📂 Unique Value Counting & Password Checking with Hashing

## 🔐 Script: check_password.py
This script implements a Bloom Filter data structure that efficiently checks whether a given password has already been added before.

### Features:
- Efficient membership testing without storing all values exactly.
- Possibility of false positives.
- Uses hash functions (mmh3) to set and check bits.

---

## 🌐 Script: uniq_ips.py
This script performs log file analysis on lms-stage-access.log to count the number of unique IP addresses using two approaches:

- Exact count — using Python’s built-in set data structure.
- Approximate count — using the HyperLogLog algorithm.

### 📊 Method Comparison:

| Metric                   | Точний підрахунок  | HyperLogLog        |
|--------------------------|--------------------|--------------------|
| Unique elements	         |   28	              |   28.0240          |
|  Execution time (sec)	   |   0.001761	        |   0.022105         |

We observe that HyperLogLog takes noticeably more time in this case due to extra computations for statistics:
- It hashes each element.
- Determines the position of the first leading zero in the binary representation.
- Updates registers (array of leading zero lengths) — which adds computational overhead.
- After all elements are processed, it merges stats from all registers for the final estimate.


These steps add overhead that isn't justified when there are only 28 elements.

HyperLogLog becomes more efficient in terms of memory and time when:
- There is a large volume of data: millions of entries or more.
- An approximate count of unique values is sufficient.
- Memory (RAM) is limited — as in large-scale streaming systems or IoT scenarios.

### Conclusions:
**Exact method** gives a 100% accurate result but consumes more memory with large datasets.

**HyperLogLog** offers fast, memory-efficient counting with less than 1% error, which is ideal for large-scale logs or data streams.

For small datasets: the **Exact count** using set is faster and more accurate (as observed here).

For large datasets: **HyperLogLog** is more memory- and time-efficient, though it provides approximate results.

## 📁 Project Structure

    ├── check_password.py     # Bloom Filter for password checking
    ├── uniq_ips.py           # Log analysis: exact and approximate IP counting
    ├── hyperloglog.py        # HyperLogLog algorithm implementation
    ├── lms-stage-access.log  # Example log file with IP addresses
    └── README.md             # Project documentation

## 🛠️ Requirements
- Python 3.8+
- mmh3 library for the Bloom Filter:
    
      pip install mmh3