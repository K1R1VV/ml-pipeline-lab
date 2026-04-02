def hello():
    return "Hello from Docker!"


def process_data(data: dict) -> int:
    return round(data["value"] * data["multiplier"], 3)


if __name__ == "__main__":
    print(hello())
    sample_data = {"value": 5, "multiplier": 3}
    result = process_data(sample_data)
    print(f"Processing result: {result}")