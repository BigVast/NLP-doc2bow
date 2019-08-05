l# NLP-doc2bow
Learning NLP
这是我在做实验中用到的两个py文件，供自己使用，如果大家有好的意见欢迎留言和follow，
我的csdn主页：[点击这里访问](https://blog.csdn.net/kele_imon).

# doc2bow
doc2bow是Gensim中封装的一个方法，主要的核心是Bow模型（词袋模型，特点==无语义==，下面主要说一下词袋模型的内容）

## bow模型

先给出两个简单的例子
> Do you like me?

> Do you love me?

首先根据上面的两个例子建立词典

>{"Do":1, "you":2, "love":3, "like":4, "me":5}

所以`Do you like me?`可以表示为`1, 1, 0, 1, 1`
因此`Do you love me?`可以表示为`1, 1, 1, 0, 1`

所以利用余弦计算相似度 sim=cos(α) = <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\vec{A}\cdot&space;\vec{B}}{\left&space;\|&space;A&space;\right&space;\|\cdot&space;\left&space;\|&space;B&space;\right&space;\|}=\frac{1\times&space;1&plus;1\times&space;1&plus;0\times&space;1&plus;0\times&space;1&plus;1\times&space;1}{\sqrt{1^{2}&plus;1^{2}&plus;0^{2}&plus;1^{2}&plus;1^{2}}\cdot\sqrt{1^{2}&plus;1^{2}&plus;1^{2}&plus;0^{2}&plus;1^{2}}}=\frac{3}{4}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\vec{A}\cdot&space;\vec{B}}{\left&space;\|&space;A&space;\right&space;\|\cdot&space;\left&space;\|&space;B&space;\right&space;\|}=\frac{1\times&space;1&plus;1\times&space;1&plus;0\times&space;1&plus;0\times&space;1&plus;1\times&space;1}{\sqrt{1^{2}&plus;1^{2}&plus;0^{2}&plus;1^{2}&plus;1^{2}}\cdot\sqrt{1^{2}&plus;1^{2}&plus;1^{2}&plus;0^{2}&plus;1^{2}}}=\frac{3}{4}" title="\frac{\vec{A}\cdot \vec{B}}{\left \| A \right \|\cdot \left \| B \right \|}=\frac{1\times 1+1\times 1+0\times 1+0\times 1+1\times 1}{\sqrt{1^{2}+1^{2}+0^{2}+1^{2}+1^{2}}\cdot\sqrt{1^{2}+1^{2}+1^{2}+0^{2}+1^{2}}}=\frac{3}{4}" /></a>

**从这里可以看出，bow模型和词语的先后顺序无关，和词语的语义无关，全看建立的字典匹配情况。
缺点：如果文本比较大的话，那么字典就会非常大，检索也会很麻烦。**
