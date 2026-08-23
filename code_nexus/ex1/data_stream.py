from typing import List, Any
from ex0.data_processor import (
    DataProcessor,
    NumericProcessor,
    TextProcessor,
    LogProcessor
)


class DataStream:

    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []
        self._total_processed: dict[DataProcessor, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        if proc not in self._processors:
            self._processors.append(proc)
            if proc not in self._total_processed:
                self._total_processed[proc] = 0

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            routed = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    count = len(element) if isinstance(element, list) else 1
                    self._total_processed[proc] += count
                    routed = True
                    break
            if not routed:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            name = proc.__class__.__name__
            formatted_name = name.replace("Processor", " Processor")
            total = self._total_processed[proc]
            remaining = proc.storage_size
            print(
                f"{formatted_name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    stream_eng = DataStream()
    stream_eng.print_processors_stats()

    print("\nRegistering Numeric Processor")
    num_proc = NumericProcessor()
    stream_eng.register_processor(num_proc)

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]

    print(f"\nSend first batch of data on stream: {batch}")
    stream_eng.process_stream(batch)
    stream_eng.print_processors_stats()

    print("\nRegistering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream_eng.register_processor(text_proc)
    stream_eng.register_processor(log_proc)

    print("Send the same batch again")
    stream_eng.process_stream(batch)
    stream_eng.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()

    stream_eng.print_processors_stats()
