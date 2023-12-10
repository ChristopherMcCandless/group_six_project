from transformers import AutoModelForSeq2SeqLM, T5TokenizerFast
import torch

class Summarizer:

    def setup(self, use_gpu=0):
        #TODO надо выбрать другую модель, эта очень плохая 
        model_name = 'UrukHan/t5-russian-summarization'
        self.use_gpu = use_gpu
        self.tokenizer = T5TokenizerFast.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def summarize(self, input_sequences: list):
        print(f'Summarize unput: {input_sequences}')

        task_prefix = 'Spell correct: '
        encoded = self.tokenizer(
            [task_prefix + sequence for sequence in input_sequences],
            padding='longest',
            #max_length=256,
            truncation=True,
            return_tensors='pt',
        )

        if torch.cuda.is_available():
            if self.use_gpu == 0:
                device = torch.device('cuda')
            else:
                device = torch.device('cuda:' + self.use_gpu)
        else:
            device = torch.device('cpu')

        predicts = self.model.generate(**encoded.to(device))
        rslt = self.tokenizer.batch_decode(predicts, skip_special_tokens=True)
        return rslt