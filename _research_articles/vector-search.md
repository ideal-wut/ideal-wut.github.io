---
layout: research_article
title: 向量数据库
description: 高维向量存储、索引与检索系统，支持大规模向量数据管理与相似度搜索
permalink: /research/articles/vector-database/
---



## 向量数据库关键技术
向量数据库能够增强大模型的推理能力，是大模型不可或缺的技术基座。本研究方向围绕向量数据库的索引技术，涵盖索引构建、存储、更新、查询的全流程。



### 索引构建
针对海量向量场景下索引构建效率低的问题，实现索引的高效构建。GLIDE[1]利用GPU的并行能力加速图索引的构建，将索引构建的过程划分为子图构建与子图合并两步，并在划分子图时考虑数据局部性，使得子图中的边尽可能多地复用在合并后的图中，从而大量减少子图合并阶段的冗余计算和显存占用。

### 索引存储
针对现有索引依赖内存存储导致的存储瓶颈，实现基于磁盘的索引存储。MARGO[2]创新性地将图索引在磁盘上的布局优化问题从边集选取的角度进行了阐释，通过理论证明设计了边的重要性权重，在布局优化时优先考虑重要的边。同时，MARGO证明该问题是NP难的，并提出了一种高效解决方案。

### 索引更新
现有索引仅支持静态场景，亟待对动态场景下的向量更新操作提供支持。Wolverine[3]创新性地指出，图索引在更新中性能衰退的原因是单调路径的破坏，并通过为被删除点的出邻居补边修复单调路径。此外，Wolverine指出了用于修复单调路径的候选点需要满足的性质，限制了候选点数量，保证修复有效且高效。

### 索引查询
旨在提升向量相似性查询的效率与精度。PM-LSH[4,5]针对局部敏感哈希索引存在的距离估计不准确和不必要的候选点探测问题，在理论上证明了向量在投影空间中的距离与在原始空间中距离的关系，通过投影距离准确估计原始距离。同时采用中枢测度树索引投影空间中的点，使用增量式搜索的方法探测必要候选点。PCE-IVFPQ[6]针对倒排索引中效率与精度的矛盾，提出一种基于深度学习的分区探测基数估计模型，综合考虑查询向量特征、查询数量特征和索引结构特征，准确估计必要的分区探测数量，在避免“漏探”的同时减少“误探”，兼顾效率与精度。FARGO[7]聚焦于最大内积查询，提出了基于局部敏感哈希的全局多桶探测策略，为所有哈希表生成全局探测序列，以便在所有哈希表中检测最有希望的候选点，同时通过量化距离估计原始距离，提升候选点质量。


## 研究成果与应用

本方向的研究成果发表在SIGMOD、VLDB、ICDE、TKDE等重要学术期刊和会议上，获得VLDB 2020最佳论文奖，申请/获得6项国家发明专利与1项美国专利。团队在此方向与Zilliz等知名企业展开合作，并实现相关技术的应用落地。

![分区探测基数估计模型](/assets/images/research/向量数据库3.png)

![](/assets/images/research/向量数据库1.png)

![](/assets/images/research/向量数据库2.png)

![](/assets/images/research/向量数据库4.png)

## 参考文献

[1]Fuhao Ruan, Bolong Zheng, Ling Xu, Ziyang Yue, Dawei Liu, Kanru Xu, Xiaofang Zhou, Christian S. Jensen. GLIDE: GPU-Accelerated ANN Graph Index Construction via Data Locality.

[2]Ziyang Yue, Bolong Zheng, Ling Xu, Kanru Xu, Shuhao Zhang, Yajuan Du, Yunjun Gao, Xiaofang Zhou, Christian S. Jensen. Select Edges Wisely: Monotonic Path Aware Graph Layout Optimization for Disk-Based ANN Search. PVLDB 2025: 4337-4349.

[3]Dawei Liu, Bolong Zheng, Ziyang Yue, Fuhao Ruan, Xiaofang Zhou, Christian S. Jensen: Wolverine: Highly Efficient Monotonic Search Path Repair for Graph-based ANN Index Updates. PVLDB 2025: 2268-2280.

[4]Bolong Zheng, Xi Zhao, Lianggui Weng, Nguyen Quoc Viet Hung, Hang Liu, Christian S. Jensen. PM-LSH: A Fast and Accurate LSH Framework for High-Dimensional Approximate NN Search. PVLDB 2020: 643-655.

[5]Bolong Zheng, Xi Zhao, Lianggui Weng, Quoc Viet Hung Nguyen, Hang Liu, Christian S. Jensen. PM-LSH: A Fast and Accurate In-memory Framework for High-dimensional Approximate NN and Closest Pair Search. VLDBJ. 31(6): 1339-1363 (2022).

[6]Bolong Zheng, Ziyang Yue, Qi Hu, Xiaomeng Yi, Xiaofan Luan, Charles Xie, Xiaofang Zhou, Christian S. Jensen. Learned Probing Cardinality Estimation for High-Dimensional Approximate NN Search. ICDE 2023: 3209-3221.

[7]Xi Zhao, Bolong Zheng, Xiaomeng Yi, Xiaofan Luan, Charles Xie, Xiaofang Zhou, Christian S. Jensen. FARGO: Fast Maximum Inner Product Search via Global Multi-Probing. PVLDB 2023: 1100-1112.
