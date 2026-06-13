"""
benchmark.py

Performance benchmarking utilities
for Real-Time Object Detection on PYNQ-Z2.
"""

import numpy as np


class Benchmark:
    """
    Performance Measurement Class
    """

    def __init__(self):
        self.latencies = []

    def add_latency(self, latency):
        """
        Store latency value.
        """
        self.latencies.append(latency)

    def get_results(self, total_time):

        latencies = np.array(self.latencies)

        if len(latencies) == 0:
            return None

        avg_latency = latencies.mean()
        min_latency = latencies.min()
        max_latency = latencies.max()
        fps = 1.0 / avg_latency

        return {
            "images_processed": len(latencies),
            "avg_latency_ms": avg_latency * 1000,
            "min_latency_ms": min_latency * 1000,
            "max_latency_ms": max_latency * 1000,
            "fps": fps,
            "total_time": total_time
        }

    def print_results(self, results):

        print("\n===== CPU-ONLY PERFORMANCE (PYNQ-Z2) =====")

        print(
            f"Total images processed : {results['images_processed']}"
        )

        print(
            f"Average latency        : {results['avg_latency_ms']:.2f} ms"
        )

        print(
            f"Min latency            : {results['min_latency_ms']:.2f} ms"
        )

        print(
            f"Max latency            : {results['max_latency_ms']:.2f} ms"
        )

        print(
            f"Throughput (FPS)       : {results['fps']:.2f}"
        )

        print(
            f"Total execution time   : {results['total_time']:.2f} s"
        )
