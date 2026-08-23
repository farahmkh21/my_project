from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Union, Dict


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._storage: List[Tuple[int, str]] = []
        self._counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    @property
    def storage_size(self) -> int:
        return len(self._storage)

    def output(self) -> Tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available to output.")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            if len(data) == 0:
                return False
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for x in data:
                self._storage.append((self._counter, str(x)))
                self._counter += 1
        else:
            self._storage.append((self._counter, str(data)))
            self._counter += 1


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            if len(data) == 0:
                return False
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for x in data:
                self._storage.append((self._counter, str(x)))
                self._counter += 1
        else:
            self._storage.append((self._counter, str(data)))
            self._counter += 1


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        def is_valid_log(d: Any) -> bool:
            if not isinstance(d, dict):
                return False
            return all(
                isinstance(k, str) and isinstance(v, str) for k, v in d.items()
            )

        if is_valid_log(data):
            return True
        if isinstance(data, list):
            if len(data) == 0:
                return False
            return all(is_valid_log(x) for x in data)
        return False

    def ingest(
        self,
        data: Union[Dict[str, str], List[Dict[str, str]]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(d: Dict[str, str]) -> str:
            level = d.get("log_level", "UNKNOWN")
            msg = d.get("log_message", "")
            return f"{level}: {msg}"

        if isinstance(data, list):
            for x in data:
                self._storage.append((self._counter, format_log(x)))
                self._counter += 1
        else:
            self._storage.append((self._counter, format_log(data)))
            self._counter += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")
    print(
        "Test invalid ingestion of string 'foo' "
        "without prior validation:"
    )
    try:
        num_proc.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")
    print("Processing data: [1, 2, 3, 4, 5]")
    num_proc.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        r, v = num_proc.output()
        print(f"Numeric value {r}:  {v}")

    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text_proc.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    r, v = text_proc.output()
    print(f"Text value {r}: {v}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    print("Processing data: [{’log_level’: ’NOTICE’, ’log_message’:")
    print("’Connection to server’}, {’log_level’: ’ERROR’, ’log_message’:")
    print("’Unauthorized access!!’}]")
    log_proc.ingest([
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
    ])
    print("Extracting 2 values...")
    for i in range(2):
        r, v = log_proc.output()
        print(f"Log entry {r}: {v}")
