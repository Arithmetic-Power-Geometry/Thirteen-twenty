# Build and verification

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic exact_1320.cpp -o exact_1320
./exact_1320 | tee exact_1320_output.txt
sha256sum -c SHA256SUMS
```

Expected: 11698 primitive pairs, 0 violations, one equality at (1,14). GCC 14.2.0 was used for the recorded run.
