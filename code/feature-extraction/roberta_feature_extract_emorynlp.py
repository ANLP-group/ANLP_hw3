import pickle, torch
from tqdm import tqdm
from fairseq.models.roberta import RobertaModel
from fairseq.data.data_utils import collate_tokens

speakers, labels, sentences, train_ids, test_ids, valid_ids = pickle.load(open('emorynlp/emorynlp.pkl', 'rb'))

roberta = RobertaModel.from_pretrained(
    'checkpoints/emorynlp/',
    checkpoint_file='checkpoint_best.pt',
    data_name_or_path='emorynlp-bin'
)
roberta.eval()

roberta1, roberta2, roberta3, roberta4 = {}, {}, {}, {}

all_ids = train_ids + valid_ids + test_ids

for i in tqdm(range(len(all_ids))):
    item = all_ids[i]
    sent = sentences[item]
    batch = collate_tokens([roberta.encode(s) for s in sent], pad_idx=1)
    feat = roberta.extract_features(batch, return_all_hiddens=True)
    roberta1[item] = [row for row in feat[-1][:, 0, :].detach().numpy()]
    roberta2[item] = [row for row in feat[-2][:, 0, :].detach().numpy()]
    roberta3[item] = [row for row in feat[-3][:, 0, :].detach().numpy()]
    roberta4[item] = [row for row in feat[-4][:, 0, :].detach().numpy()]

pickle.dump([speakers, labels, roberta1, roberta2, roberta3, roberta4, sentences, train_ids, test_ids, valid_ids], open('emorynlp/emorynlp_features_roberta.pkl', 'wb'))
