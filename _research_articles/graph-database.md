---
layout: research_article
title: 图数据库
description: 图数据存储、查询优化与图计算技术，支持复杂关系数据的高效管理与分析
permalink: /research/articles/graph-database/
---



## 图计算关键技术

在数据跃升为数字经济时代核心生产要素的背景下，图数据以其对复杂关系的深度刻画能力，正成为释放数据要素价值的关键载体。通过节点与边构建结构拓扑，图数据不仅突破了传统关系型数据线性结构局限，更能揭示隐藏在数据中的深层次模式和间接联系，为解决复杂问题提供了强有力的工具。

  随着图数据分析在各行各业的深度渗透与持续赋能，图数据“规模海量化”(百亿级边)、“高频动态化”(秒级拓扑变化)、“关联复杂化”(价值密度低)三大特征日益明显，致使现有图分析技术处理能力弱(单机内存/算力限制)、更新效率低(全图重计算耗时)与洞察层次浅(高阶模式挖掘欠缺，难以挖掘蕴含价值)等短板急剧放大。为此，本方向围绕着“如何突破单机内存与算力瓶颈、设计高效可扩展图分析算法”，“如何捕获动态图数据演化特征，构建实时增量图分析理论与方法”，“如何建模高维异构关联语义模式，实现图数据深度价值挖掘”等三大核心科学问题展开，形成了一套大图数据分析理论和方法体系。

### 1）大图数据外存与分布式计算优化算法  
  通过设计轻量级索引构建机制 [1]、分布式动态负载均衡优化策略 [2] 及分层剪枝框架 [3][4][5]，突破传统单机模型在内存容量与计算能力的瓶颈，实现海量规模图数据高效可扩展分析。

### 2）动态图分析有界理论与实时更新方法  
  从局部计算视角切入，通过数学建模严格界定动态操作的影响域，构建基于传播机制（颜色传播 [6]、权重依赖传播 [7]、标签约束子树重构 [8]）的增量式更新框架，在严格保证结果准确性的前提下，将计算复杂度从传统方法的全局规模压缩至可证明的影响域有界级别 [9][10]。

### 3）复杂图数据高阶建模与高效计算方法  
  针对符号网络 [11][12]、异构信息网络 [13] 和属性图 [14][15] 等复杂关联图数据展开研究，解决了包括平衡团挖掘、结构聚类、最短路径等核心分析任务的建模和高效计算问题。

## 研究成果与应用

本方向的研究成果发表在 SIGMOD、VLDB、ICDE、TKDE 等重要学术期刊和会议上，发表 CCF A 类论文 40 余篇，申请/授权 14 项国家发明专利。团队在此方向与 阿里、国家电网 等知名企业展开合作，并实现相关技术的应用落地。

![图计算关键技术](/assets/images/research/图计算1.png)

## 参考文献

[1]Long Yuan, Lu Qin, Xuemin Lin, Lijun Chang, Wenjie Zhang: Diversified Top-k Clique Search, VLDBJ, 25(2): 171196, 2016

[2] Long Yuan, Lu Qin, Xuemin Lin, Lijun Chang, Wenjie Zhang, I/O Efficient ECC Graph Decomposition via Graph Reduction, PVLDB, 9(7): 516-527, 2016 

[3]Long Yuan, Lu Qin, Xuemin Lin, Lijun Chang, Wenjie Zhang, Diversified Top-k Clique Search, ICDE, 387-398，2016

[4]Long Yuan, Lu Qin, Xuemin Lin, Lijun Chang, Wenjie Zhang: I/O efficient ECC Graph Decomposition via Graph Reduction, VLDBJ, 26(2): 275-300, 2017 

[5]Kongzhang Hao, Long Yuan, Wenjie Zhang: Distributed HopConstrained st Simple Path Enumeration at Billion Scale. PVLDB, 15(2): 169-182, 2022 

[6]Lingkai Meng, Yu Shao, Long Yuan, Longbin Lai, Peng Cheng, Xue Li, Wenyuan Yu, Wenjie Zhang, Xuemin Lin, Jingren Zhou, A Survey of Distributed Graph Algorithms on Massive Graphs, ACM Computing Surveys 57(2): 27:127:39, 2025

[7]Long Yuan, Lu Qin, Xuemin Lin, Lijun Chang, Wenjie Zhang: Effective and Efficient Dynamic Graph Coloring, PVLDB, 11(3): 338-351, 2018

[8]Dian Ouyang, Long Yuan, Lu Qin, Lijun Chang, Ying Zhang, Xuemin Lin: Efficient Shortest Path Index Maintenance on Dynamic Road Networks with Theoretical Guarantees, PVLDB, 13(5): 602-615, 2020

[9]Boge Liu, Long Yuan, Xuemin Lin, Lu Qin, Wenjie Zhang, Jingren Zhou: Efficient (α, β)-core computation in bipartite graphs, VLDBJ, 29(5): 1075-1099, 2020 

[10]Boge Liu, Long Yuan, Xuemin Lin, Lu Qin, Wenjie Zhang, Jingren Zhou: Efficient (α, β)-core Computation: an Indexbased Approach. WWW, 1130-1140, 2019

[11]Zi Chen, Long Yuan, Xuemin Lin, Lu Qin, Wenjie Zhang: Balanced Clique Computation in Signed Networks: Concepts and Algorithms. TKDE, 35(11): 11079-11092, 2023 

[12]Zi Chen, Long Yuan, Xuemin Lin, Lu Qin, Jianye Yang: Efficient Maximal Balanced Clique Enumeration in Signed Networks. WWW, 339-349, 2020 

[13]Long Yuan, Xiaotong Sun, Zi Chen, Peng Cheng, Longbin Lai, Xuemin Lin, HINSCAN: Efficient Structural Graph Clustering over Heterogeneous Information Networks, ICDE, 2025. 

[14]Junhua Zhang, Long Yuan, Wentao Li, Lu Qin, Ying Zhang: Efficient LabelConstrained Shortest Path Queries on Road Networks: A Tree Decomposition Approach, PVLDB, 15(3): 686-698, 2022 

[15]Junhua Zhang, Long Yuan, Wentao Li, Lu Qin, Ying Zhang, Wenjie Zhang: Labelconstrained shortest path query processing on road networks. VLDBJ, 33(3):569-593, 2024
