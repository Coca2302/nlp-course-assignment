class DatasetLoaders:
    def __init__(self,dataset_path: str):
        self.dataset_path = dataset_path
    def load_raw_text_data(self) -> str:
            try:
                with open(self.dataset_path, 'r', encoding='utf-8') as file:
                    data = file.read()
                return data
            except FileNotFoundError:
                print(f"File not found: {self.dataset_path}")
                return None
            except Exception as e:
                print(f"Error while reading file: {e}")
                return None




