#!/usr/bin/env bash


# 下载数据，取top30k，并修改header
# https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md
wget https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.zh.vec
cp wiki.zh.vec tmp
echo "remove the non line"  # 删除空的行，否则gensim转化后 可视化会报错
sed -i '' '30004,332648d' tmp
sed -i '' '2282d' tmp
sed -i '' '128d' tmp

sed '1s/332647/30000/' tmp > wiki.zh.vec.30000
rm tmp


# 转化为tensor格式
# https://radimrehurek.com/gensim/scripts/word2vec2tensor.html
# 源码是按照wb的方式写的，为什么写的文件是纯文本文件？
python -m gensim.scripts.word2vec2tensor -i wiki.zh.vec.30000 -o fasttext.zh.30000.300d
