# GECAS paper verification artifacts

Paper: *Exact Certificate-Aware Nonpreemptive Scheduling with General Availability Calendars and Additive-Frequency Bounds*.

This folder contains an independently reconstructed C++ exact finite verifier of Algorithm 3, the build command, captured output, and SHA-256 hashes. The source is a new independent implementation, not a recovered original verifier.

The finite verifier checks all coprime pairs 1 <= a <= b <= 196 using an integer boundary sweep. The analytic proof for larger frequencies remains in the manuscript.

Build:
```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic exact_1320.cpp -o exact_1320
./exact_1320 | tee exact_1320_output.txt
sha256sum -c SHA256SUMS
```

Compiler used for the recorded run: g++ (Debian 14.2.0-19) 14.2.0.
