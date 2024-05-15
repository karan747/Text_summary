import os
from Text_summary.logging import logger
from Text_summary.entity import ModelTrainerConfig


from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig) -> None:
        self.config = config

    def train(self):

        logger.info("Setting device")
        device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Using device: {device}")

        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)

        sequence_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

        logger.info("Loading dataset...")
        dataset = load_from_disk(self.config.data_path)

        

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_eval_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=float(self.config.save_steps),
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        )


        trainer = Trainer(
            model=model,
            args=trainer_args,
            data_collator=sequence_collator,
            train_dataset=dataset["train"],
            eval_dataset=dataset["validation"],
            tokenizer=tokenizer
        )

        logger.info("Training model...")
        trainer.train()

        logger.info("Saving model...")
        model.save_pretrained(os.path.join(self.config.root_dir, "pegasus_dailymail_cnn"))

        logger.info("Saving tokenizer...")
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
