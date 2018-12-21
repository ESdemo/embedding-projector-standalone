# embedding visualization



## 持久化，格式

- Mikolov的bin、text
    - 被广泛采用，包括gensim
    - 与tensorflow的bin格式不兼容，不能直接用tensorboard可视化，需要[转换格式]
(https://radimrehurek.com/gensim/scripts/word2vec2tensor.html)
- tensorflow的格式
    -tensor格式，无header

关于bytes格式
- bytes(mystring, 'utf-8')，按照string方式存储的byte，并不节省空间。而且打开能直接看
- tensorflow的bytes格式打开是乱码。 哪里的不对？tf是按float的byte存储的？是采用的[numpy.ndarray.tobytes](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.ndarray.tobytes.html)?

## 词典分析
- [ ] https://ai.tencent.com/ailab/nlp/embedding.html
    - 精度: 
- [ ] https://github.com/Kyubyong/wordvectors
    - 精度: 9位有效数字
    - 格式不规范 
- [fastText](https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md)
    - dim=300, vocab_size=332647.  由于词典太大，可视化只取top 30k
    - 精度: 5位有效数字
    - 👎 : 空格也在词典中，有必要吗？对应utf8编码`127行`: `b'\xe3\x80\x80'`, `2281行`:`b'\xc2\xa0'`
    - `<s>`也在词典，作用是什么？ 

## 可视化分析

### fastText

 整体质量觉得还可以啊

**降维**
- PCA后分组很明显，是因为数据的原因吗？
- TSNE则没那么明显。why？

**nearby**
- 繁体的nearby也是繁体 
- 英文的nearby也是英文
    - fate最近的是stay night。晕，不愧是维基百科的数据。
    - 舌的nearby

**analogy**

用google的测试集跑一下看看

## 压缩

- quant  to int8
- 仅用作可视化，可以先pca到低维
    - 影响可视化较小
    - 严重影响相似度的计算 -- 😭 
- 保存类型：
    - string类型
    - float类型？怎样保存？
## extra API

- [analogy](https://github.com/tensorflow/models/blob/v1.11/tutorials/embedding/word2vec.py#L478): w0,w1,w2 

