"""
Checkpoint 1 — Plot the three transmission-time tests.
Generates plot_test1.png, plot_test2.png, plot_test3.png in the same folder.
"""

import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------------------------
# Test 1 — File size sweep (bandwidth = 10 Mbps, delay = 10 ms)
# ----------------------------------------------------------------------
test1_filesize_kb = [1, 5, 25, 100, 1024, 10240]   # KB
test1_filesize_bytes = [kb * 1024 for kb in test1_filesize_kb]
test1_avg_ms = [10.2, 14.4, 32.2, 102.2, 956.8, 9502.0]

# ----------------------------------------------------------------------
# Test 2 — Bandwidth sweep (file = 1 MB, delay = 10 ms)
# ----------------------------------------------------------------------
test2_bandwidth_mbps = [1, 5, 10, 20, 50, 100]
test2_avg_ms = [8764.6, 1773.4, 954.8, 648.8, 333.8, 276.8]

# ----------------------------------------------------------------------
# Test 3 — Delay sweep (file = 1 MB, bandwidth = 10 Mbps)
# ----------------------------------------------------------------------
test3_delay_ms = [0, 5, 10, 20, 50, 100]
test3_avg_ms = [915, 991, 989, 1014, 1075, 1305]

# ----------------------------------------------------------------------
# Shared plotting style
# ----------------------------------------------------------------------
plt.rcParams.update({
    "font.size": 12,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "figure.dpi": 120,
})

# ----------------------------------------------------------------------
# Plot 1 — File size sweep
# ----------------------------------------------------------------------
fig1, ax1 = plt.subplots(figsize=(8, 5))
ax1.plot(test1_filesize_bytes, test1_avg_ms, marker="o", linewidth=2, color="tab:blue")
ax1.set_xscale("log")
ax1.set_xlabel("File size (bytes, log scale)")
ax1.set_ylabel("Average transmission time (ms)")
ax1.set_title("Test 1 — Transmission time vs file size\n(10 Mbps, 10 ms delay, client-shaped)")
ax1.grid(True, which="both", alpha=0.3)
fig1.tight_layout()
fig1.savefig("plot_test1.png")

# ----------------------------------------------------------------------
# Plot 2 — Bandwidth sweep
# ----------------------------------------------------------------------
fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.plot(test2_bandwidth_mbps, test2_avg_ms, marker="s", linewidth=2, color="tab:green")
ax2.set_xlabel("Bandwidth (Mbps)")
ax2.set_ylabel("Average transmission time (ms)")
ax2.set_title("Test 2 — Transmission time vs bandwidth\n(1 MB file, 10 ms delay, client-shaped)")
fig2.tight_layout()
fig2.savefig("plot_test2.png")

# ----------------------------------------------------------------------
# Plot 3 — Delay sweep
# ----------------------------------------------------------------------
fig3, ax3 = plt.subplots(figsize=(8, 5))
ax3.plot(test3_delay_ms, test3_avg_ms, marker="^", linewidth=2, color="tab:red")
ax3.set_xlabel("One-way delay (ms)")
ax3.set_ylabel("Average transmission time (ms)")
ax3.set_title("Test 3 — Transmission time vs delay\n(1 MB file, 10 Mbps, client-shaped)")
fig3.tight_layout()
fig3.savefig("plot_test3.png")

print("Saved: plot_test1.png, plot_test2.png, plot_test3.png")