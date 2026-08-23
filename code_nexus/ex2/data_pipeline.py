from typing import List, Tuple, Protocol
from ex0.data_processor import NumericProcessor, TextProcessor, LogProcessor
from ex1.data_stream import DataStream


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        csv_string = ",".join(item[1] for item in data)
        print("CSV Output:")
        print(csv_string)


class JSONExportPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        json_parts = []
        for item in data:
            clean_val = item[1].replace("\\", "\\\\").replace('"', '\\"')
            json_parts.append(f'"item_{item[0]}": "{clean_val}"')
        json_string = "{" + ", ".join(json_parts) + "}"
        print("JSON Output:")
        print(json_string)


class PipelineDataStream(DataStream):

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            extracted_data: List[Tuple[int, str]] = []
            for _ in range(nb):
                if proc.storage_size > 0:
                    extracted_data.append(proc.output())
                else:
                    break
            if extracted_data:
                plugin.process_output(extracted_data)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("\nInitialize Data Stream...")
    pipeline = PipelineDataStream()
    pipeline.print_processors_stats()

    print("\nRegistering Processors")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    pipeline.register_processor(num_proc)
    pipeline.register_processor(text_proc)
    pipeline.register_processor(log_proc)

    batch1 = [
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
    print(f"\nSend first batch of data on stream:{batch1}")

    pipeline.process_stream(batch1)
    pipeline.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    pipeline.output_pipeline(3, csv_plugin)
    pipeline.print_processors_stats()

    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {
                'log_level': 'ERROR',
                'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"\nSend another batch of data:{batch2}")
    pipeline.process_stream(batch2)
    pipeline.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    pipeline.output_pipeline(5, json_plugin)
    pipeline.print_processors_stats()
