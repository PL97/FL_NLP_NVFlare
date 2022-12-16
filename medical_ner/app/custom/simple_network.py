
from transformers import BertForTokenClassification
import torch.nn as nn

class BertModel(nn.Module):

    def __init__(self):

        super(BertModel, self).__init__()
        num_labels=19
        self.model_name='bert-base-uncased'
        self.bert = BertForTokenClassification.from_pretrained(self.model_name, num_labels=num_labels, \
                    output_attentions = False, \
                    output_hidden_states = False)
        
    def forward(self, input_id, mask, label):

        output = self.bert(input_ids=input_id, attention_mask=mask, labels=label, return_dict=False)

        return output