## COSMIC: COmmonSense knowledge for eMotion Identification in Conversations

[_COSMIC_](https://github.com/declare-lab/conv-emotion) addresses the task of utterance level emotion recognition in conversations using commonsense knowledge. It is a new framework that incorporates different elements of commonsense such as mental states, events, and causal relations, and build upon them to learn interactions between interlocutors participating in a conversation. Current state-of-the-art methods often encounter difficulties in context propagation, emotion shift detection, and differentiating between related emotion classes. By learning distinct commonsense representations, COSMIC addresses these challenges and achieves new state-of-the-art results for emotion recognition on four different benchmark conversational datasets. 

### Execution

First download the RoBERTa and COMET features [here](https://drive.google.com/file/d/1TQYQYCoPtdXN2rQ1mR2jisjUztmOzfZr/view?usp=sharing) and keep them in appropriate directories in `COSMIC/erc-training`. Then training and evaluation on the four datasets are to be done as follows:

1. IEMOCAP: `python train_iemocap.py --active-listener`
2. DailyDialog: `python train_dailydialog.py --active-listener --class-weight --residual`
3. MELD Emotion: `python train_meld.py --active-listener --attention simple --dropout 0.5 --rec_dropout 0.3 --lr 0.0001 --mode1 2 --classify emotion --mu 0 --l2 0.00003 --epochs 60`
4. MELD Sentiment: `python train_meld.py --active-listener --class-weight --residual --classify sentiment`
5. EmoryNLP Emotion: `python train_emorynlp.py --active-listener --class-weight --residual`
6. EmoryNLP Sentiment: `python train_emorynlp.py --active-listener --class-weight --residual --classify sentiment`


### Citation

Please cite the following [paper](https://arxiv.org/pdf/2010.02795.pdf) if you find this code useful in your work.

```bash
COSMIC: COmmonSense knowledge for eMotion Identification in Conversations. D. Ghosal, N. Majumder, A. Gelbukh, R. Mihalcea, & S. Poria.  Findings of EMNLP 2020.
```
