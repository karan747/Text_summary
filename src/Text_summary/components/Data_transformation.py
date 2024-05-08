import os
from Text_summary.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from Text_summary.entity import DataTransformationConfig 

class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig):
        self.config = data_transformation_config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name, use_fast = False)

    def convert_text_to_feature(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length =  1024, truncation=True)
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation=True)
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def convert(self):
        logger.info('Loading dataset...')
        dataset = load_from_disk(self.config.data_path)
        logger.info('Converting dataset...')
        dataset = dataset.map(self.convert_text_to_feature, batched=True)
        logger.info('Saving dataset...')
        dataset.save_to_disk(os.path.join(self.config.root_dir, 'samsum'))
        logger.info('Done!')