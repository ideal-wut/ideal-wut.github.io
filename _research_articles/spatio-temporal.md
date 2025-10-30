---
layout: research_article
title: 时空数据库
description: 时序数据、时空数据管理与分析技术，支持复杂时空关系的高效存储与查询
permalink: /research/articles/spatio-temporal-database/
---

## 时空数据库关键技术

本研究方向旨在利用数据库与智能数据分析技术有效解决大规模时空场景下复杂查询问题并支撑相应的应用（路径规划、众包查询以及轨迹查询），具体包括：1）大规模时空路径规划，研究时空路网下的高效最短路径规划与查询问题，在高并发、高变化场景下降低索引开销提高查询效率；2）大规模时空众包调度，研究时空众包场景下的配送调度问题，通过精准的需求预测，提高整个交通系统的运行效率；3）大规模时空轨迹查询，研究复杂轨迹数据下的高效查询与分析方法，通过构建适配轨迹数据的高效索引与分布式处理机制，实现对海量轨迹数据的实时响应和精准分析。本方向承担了国家自然科学基金（面上、中欧人才、青年），国家重点研发计划子课题等国家级重点项目。技术应用于华为、阿里巴巴、滴滴出行、国家电网、中船重工等多家知名企业。

相关研究成果发表于VLDB、ICDE、IEEE TKDE、VLDBJ、CIKM等顶级会议和期刊，获得多项国家发明专利，其中重要成果获得ACM SIGSPATIAL CUP算法竞赛2020年全球冠军等重要奖项。

![时空数据库相关技术图1](/assets/images/research/时空数据库1.jpg)
研究内容示例





### 大规模时空路径规划

在智慧交通与城市出行服务日益普及的背景下，路径规划已成为地图导航、应急救援及物流运输等核心环节。传统路径规划方法在静态或小规模路网下表现良好，但面对真实、随时间变化的时空路网时，常出现索引开销过大、查询响应缓慢的问题。尤其在高并发、高频变化的场景中，交通状态实时变动，对路径计算的效率和准确性提出了更高要求。为此，团队开展了以下研究，提出能够兼顾大规模处理与实时更新的高效路径规划技术。

#### FAHL: An Efficient Labeling Index for Flow-Aware Shortest Path Querying in Road Networks（ICDE 2025）
![时空数据库相关技术图3](/assets/images/research/时空数据库2.jpg)
FAHL索引结构示例

本成果提出一种名为 FAHL 的标签索引结构，用于在道路网络中高效处理考虑交通流量 因素的最短路径查询。FAHL 融合了交通流量信息与传统的最短路径查询需求，通过设计新的标签结构以及流量感知机制，使得查询不仅返回基于图结构的最小距离路径，还兼顾路径上交通流量的动态特性。该方法在索引构建与查询阶段都引入流量因素，以期能在流量高峰或拥堵情况下仍保持较高的查询性能与准确性。实验证明，FAHL 相较于尚未考虑流量影响的传统标签索引，在路径查询响应时间、索引大小和查询正确性方面都有显著提升，尤其在大规模、交通波动明显的道路网络上更具优势。


#### Reinforcement Learning based Tree Decomposition for Distance Querying in Road Networks （ICDE 2023）
![时空数据库相关技术图4](/assets/images/research/时空数据库3.jpg)
RL-TD框架示例


在道路网络中快速计算两点间最短路径距离是众多应用的基础操作。然而，现有方法要么查询快但预处理或索引开销大，要么空间消耗小但查询慢。为平衡空间与查询效率，本文提出一种基于强化学习的树分解方法RL-TD。RL-TD首先将道路网络分解为树结构，借助树的层次结构来组织顶点，从而将图分割成多个子问题；然后使用强化学习技术决定如何分解树，使得索引结构在保证查询效率的同时减少空间开销。具体地，团队定义状态空间与动作空间，用强化学习策略来选择分解方式，优化树的划分，以减少标签大小且避免查询时遍历大量非必要路径。实验表明，在多个大规模真实道路网络上，RL-TD 的查询时间与索引空间比传统树分解与标签方法显著改善，特别是在查询量大、网络规模大时，其综合性能优势更加明显。


#### Double Hierarchical Labeling Shortest Distance Querying in Time-dependent Road Networks （ICDE 2023）
![时空数据库相关技术图6](/assets/images/research/时空数据库4.jpg)
DHL索引结构示例

在时变道路网络中，最短距离查询是许多实时系统的核心需求。然而，由于时间依赖性，传统静态网络的标签方法往往不能直接使用，或者效率低下。本文提出双层次标签索引DHL来应对这一挑战。该方法建立两个层次的标签结构：内层处理道路网络在静态结构上的顶点与距离信息，外层捕捉时间变化对路径成本的影响。具体而言，它对道路网络构造静态标记，再基于时间变化调整这些标记，使得在查询时可以快速查到受时间影响最显著的道路段，并动态更新相关部分。DHL在查询精度与响应速度之间取得较好平衡，同时其预处理或索引构建成本与动态维护成本相比传统全时间敏感方法更低。团队通过在真实与合成的时变道路网络上做实验，结果显示双层次标签方法在查询速度上优于多个基准方法，在时间敏感情况下仍能保持良好性能。



#### Workload-Aware Shortest Path Distance Querying in Road Networks （ICDE 2022）
![时空数据库相关技术图7](/assets/images/research/时空数据库5.jpg)
WCF框架示例

该成果针对道路网络中的最短距离查询任务，关注查询负载的特点对查询效率与索引设计的影响。具体而言，我们提出一种叫 WCF的索引结构，它能利用查询空间分布的不均匀性来优化标签的分布与大小。具体来说，WCF 将网络划分为多个核心森林，对热点区域与冷区在索引标签上采用不同策略，以减少整体存储开销，同时加快常见路径的查询速度。论文中还设计了一系列启发式策略来决定标签构建和查询时的剪枝顺序，从而使得索引在真实世界的查询负载下表现更好。实验结果表明：相较于传统标签索引方法，在实际负载环境中，WCF 在查询响应时间和资源（内存或存储大小）利用上有明显优势。



#### SpeakNav: Voice-based Route Description Language Understanding for Template Driven Path Search （VLDB 2021）
![时空数据库相关技术图10](/assets/images/research/时空数据库6.jpg)
SpeakNav框架示例


本成果提出 SpeakNav 框架，让用户可以用语音描述期望路线（包括 POI 和距离线索等），系统理解这些自然语言描述并推荐合适路径。核心模型是RT-BERT，用于从语音转换的文本中识别关键地点关键词及相关距离信息，并分类意图与槽位填充。然后将这些信息形式化为一个模板驱动的路径查询。为高效处理此类查询，本文构建了混合标签索引用于计算 POI 间的网络距离，并提出一个算法结合 PB-tree 索引来加速搜索。实验证明，RT-BERT 在理解用户语音意图及提取线索方面精度高，而所提算法在真实与合成数据上的路径推荐性能优于多个基线方法。

### 大规模时空众包调度研究背景

- 随着共享出行、即时配送等新兴服务的兴起，时空众包调度在交通与物流系统中扮演越来越重要的角色。该场景下存在任务分布广泛、需求波动频繁和配送端动态变化等挑战。传统的调度方法难以兼顾任务分配的实时性与系统整体效率，常导致资源浪费和用户体验下降。因此，如何基于大规模时空数据进行精准需求预测，并利用算法实现任务与配送端的高效匹配，是提升众包平台运营效率与受益的关键研究问题。为此，团队开展了以下研究，在实现高效众包调度的基础上，保证配送受益。

#### SOUP: Spatial-Temporal Demand Forecasting and Competitive Supply in Transportation （TKDE）
![时空数据库相关技术图10](/assets/images/research/时空数据库7.jpg)
SOUP框架示例

本文研究交通运输系统中空间-时间需求预测与竞争性供给的问题。假设系统中存在不断产生的出行需求和多个能够响应这些需求的服务代理，目标是在满足需求的同时，使得代理的空闲时间最小。论文分两步展开：第一步通过构建精细模型预测各时段、各地块的出行请求，提出一种称为空间-时间图卷积序列学习的算法，用以预测需求在空间与时间上的分布；第二步提出一个路径规划算法 DROP，既考虑预测的需求，又考虑当前供给与需求的状态，以优化代理响应请求的路径分配，并减少代理之间的竞争。通过在真实与合成数据集上的广泛实验，SOUP 在减少代理空闲时间、提升响应效率、提升需求响应率等方面均超过现有方法，展现出良好的实用与推广价值。

Online Trichromatic Pickup and Delivery Scheduling in Spatial Crowdsourcing （ICDE 2020）
![时空数据库相关技术图10](/assets/images/research/时空数据库8.jpg)
系统示意图

本文研究一种新的在线取送调度问题，在空间众包场景中，不仅考虑任务数量与成本，还考虑“三重效用”，即同时综合考虑任务的物品质量、配送端的可靠性与任务本身的利润。此外，客户在提交任务时可以指定物品关键词，这样可能对应多个可选的取货点，从而进一步增加调度复杂度。我们将问题形式化为在线三重取送调度问题：目标是在任务流在线到达时，为配送端分配取送任务并调度路径，使总效用最大。为快速响应任务，提出三种方法：第一种为贪婪算法，按效用-成本比率选择任务；第二种为Skyline动态树方法，用于保留中间计算结果，提高结果质量；第三种为基于密度分组方法，把进入任务流的任务按空间或其他特征分组，再分配给配送端以获得较高总体效用。通过对真实与合成数据集的广泛实验，我们展示这些方法在效用、效率和资源利用率上都明显优于现有基线方法，特别是在任务在线到达、取货点多变以及工人质量与物品质量差异显著时，优势更加明显。

ByGCN: Spatial Temporal Byroad-Aware Graph Convolution Network for Traffic Flow Prediction in Road Networks （CIKM 2024）
![时空数据库相关技术图](/assets/images/research/时空数据库9.jpg)
ByGCN模型结构示例

本成果针对道路网络中交通流量预测的挑战，提出 ByGCN 模型，该模型由两个主要模块组成：即支路识别模块和时空学习模块。前者用来识别不同支路的结构特征并进行空间-时间解耦，以捕捉道路本身对交通流的差异影响；后者通过图扩散等技术学习道路网络中各节点随时间变化的交通流模式。ByGCN 能够更细致地建模道路之间的空间依赖关系以及时间动态性，对短期和长期的流量波动具有较强的响应能力。实验证明，在多个真实交通数据集上，ByGCN 比同类基线模型在预测精度上有明显改进，特别是在拥堵或交通模式突变时，其误差下降效果更为显著。

### 大规模时空轨迹查询研究背景

- 轨迹数据广泛来源于移动设备、交通工具和各类传感器，规模日益增长，成为智能交通与城市计算的重要基础。轨迹查询不仅涉及相似性检索、异常检测，还包括模式挖掘与预测分析。然而，传统方法在处理百万级以上轨迹数据时往往遭遇计算复杂度高、查询延迟大和存储压力大等问题。特别是在需要实时响应与多维分析的应用中，现有技术难以满足需求。因此，团队探索面向大规模轨迹数据的高效索引与分布式处理机制，提出相应解决方法，实现大规模时空轨迹的高效查询。

#### REPOSE: Distributed Top-k Trajectory Similarity Search with Local Reference Point Tries （ICDE 2021）
![时空数据库相关技术图](/assets/images/research/时空数据库10.jpg)
RP-trie树结构示例

随着轨迹数据的急剧增长，单机处理轨迹相似性查询已不能满足时效与规模需求。为此，提出一个分布式内存管理框架 REPOSE，用于在 Spark 平台上处理 Top-k 轨迹相似性查询。REPOSE 的关键包括：设计局部参考点字典树索引结构RP-trie，用于在分区内快速定位和比对轨迹；以及一种异构的全局分区策略来避免分布式环境中的负载不平衡问题。REPOSE在多个真实数据集上做了广泛实验，结果显示 REPOSE 在吞吐量、响应时间以及资源利用上均优于现有同类方法，能有效支持轨迹相似性度量的多样性并在分布式环境中扩展性好。

#### Answering Why-Not Group Spatial Keyword Queries （TKDE）
![时空数据库相关技术图](/assets/images/research/时空数据库11.jpg)
系统示意图

随着网络上地理-文本对象的广泛存在，人们越来越多地使用带关键词的 Top-k 空间查询来查找最近且包含关键词的对象。然而，当一组用户发起 Top-k 群体空间关键词查询时，他们有时会发现某些他们认为应该出现在结果中的对象并未返回，Why-not查询应运而生。本文在此背景下提出Why-not 群体空间关键词查询：既能解释为什么预期对象缺失，也能对原始查询做最小修改，以使这些对象能够出现在修改后的查询结果中。为此，团队设计了一个三阶段框架：第一阶段，通过有效检索可能影响排名的竞争对象来缩小搜索空间；第二阶段，采用增量采样算法生成候选偏好权重向量，以探索修改用户偏好（包括位置、关键词权重和用户之间的距离阈值等因素）的可能性；第三阶段，通过定义惩罚模型评估各个候选查询与原始查询的差异，并选取“修改最小”的结果作为推荐的修改版本。实验证明，在真实数据和合成数据集上，该方法在效率和修改幅度（即用户体验）上均优于基线方法，能够在保留用户原始偏好的前提下，最大限度地包含用户预期对象，同时控制查询修改带来的成本。

### 参考文献

[1] Tangpeng Dan, Xiao Pan, Bolong Zheng, Xiaofeng Meng: FAHL: An Efficient Labeling Index for Flow-Aware Shortest Path Querying in Road Networks. ICDE 2025: 836-849
[2] Tangpeng Dan, Xiao Pan, Bolong Zheng, Xiaofeng Meng: ByGCN: Spatial Temporal Byroad-Aware Graph Convolution Network for Traffic Flow Prediction in Road Networks. CIKM 2024: 415-424
[3] Bolong Zheng, Qi Hu, Lingfeng Ming, Jilin Hu, Lu Chen, Kai Zheng, Christian S. Jensen: SOUP: Spatial-Temporal Demand Forecasting and Competitive Supply in Transportation. IEEE Trans. Knowl. Data Eng. 35(2): 2034-2047 (2023)
[4] Bolong Zheng, Yong Ma, Jingyi Wan, Yongyong Gao, Kai Huang, Xiaofang Zhou, Christian S. Jensen: Reinforcement Learning based Tree Decomposition for Distance Querying in Road Networks. ICDE 2023: 1678-1690
[5] Tangpeng Dan, Xiao Pan, Bolong Zheng, Xiaofeng Meng: Double Hierarchical Labeling Shortest Distance Querying in Time-dependent Road Networks. ICDE 2023: 2077-2089
[6] Bolong Zheng, Jingyi Wan, Yongyong Gao, Yong Ma, Kai Huang, Xiaofang Zhou, Christian S. Jensen: Workload-Aware Shortest Path Distance Querying in Road Networks. ICDE 2022: 2372-2384
[7] Bolong Zheng, Lei Bi, Juan Cao, Hua Chai, Jun Fang, Lu Chen, Yunjun Gao, Xiaofang Zhou, Christian S. Jensen: SpeakNav: Voice-based Route Description Language Understanding for Template Driven Path Search. Proc. VLDB Endow. 14(12): 3056-3068 (2021)
[8] Bolong Zheng, Lianggui Weng, Xi Zhao, Kai Zeng, Xiaofang Zhou, Christian S. Jensen: REPOSE: Distributed Top-k Trajectory Similarity Search with Local Reference Point Tries. ICDE 2021: 708-719
[9] Bolong Zheng, Kai Zheng, Christian S. Jensen, Nguyen Quoc Viet Hung, Han Su, Guohui Li, Xiaofang Zhou: Answering Why-Not Group Spatial Keyword Queries. IEEE Trans. Knowl. Data Eng. 32(1): 26-39 (2020)
[10] Bolong Zheng, Chenze Huang, Christian S. Jensen, Lu Chen, Nguyen Quoc Viet Hung, Guanfeng Liu, GuoHui Li, Kai Zheng: Online Trichromatic Pickup and Delivery Scheduling in Spatial Crowdsourcing. ICDE 2020: 973-984



## 时间序列数据管理与分析

本方向的研究包括三个方面：1）异常检测，以数据库等工业系统的运维任务为研究背景，针对流式子序列、多变量时间序列等运行数据，实时定位处于异常状态的时间段及对应KPI；2）根因分析，在异常检测研究的基础上，针对已被判定为异常的目标时间戳样本，诊断故障类型及内因，并溯源故障软硬件设备；3）时序数据库优化，主要针对时序数据库的操作性能优化任务，结合非易失性内存等硬件，研究去中心化的日志系统设计。

在异常检测方面的研究中：1）针对现有方法仅依赖单一特征设计异常分数且难适应流式数据的问题，Sirloin[1]利用近邻查询和聚类提取流式数据中的局部和全局特征，增量维护索引结构，实现精度和效率的提升；2）为深入挖掘多变量时间序列中的特征间关联，并解决半监督训练过程中的过拟合现象，设计对抗图神经网络SGAT-AE[2]，提升异常检测过程的鲁棒性；3）为满足真实分布式场景下的数据条件和泛化性需求，提出基于多视角时空注意力机制的异常检测模型STAMP[3]和配套的可兼容无监督学习框架，实现基于无标签数据的模型训练及分布式节点间的统一部署；在根因分析方面的研究中：1）针对分布式云数据库中的异常表现跨集群不同的问题，设计孪生差异网络SDN[4]，基于时序监控指标的差异进行对比学习，实现异常诊断，并提升集群间的泛化性；2）整合异常检测和根因分析模型，构建端到端的智能运维系统MindDx，实现异常定位、故障诊断、告警管理等多种功能，覆盖运维任务的全生命周期；在时序数据库优化方面的研究中，针对现有时序数据库日志系统的吞吐量瓶颈与高同步开销问题，DecLog[5]提出数据驱动的LSN机制捕获事务依赖，结合日志队列流水线持久化和线程快照同步策略，在非易失性内存上实现并行、宽松排序的日志记录，显著提升系统吞吐与可扩展性，同时降低恢复延迟。

本方向的研究成果发表在VLDB、ICDE、TKDE等重要学术期刊和会议上，获得VLDB 2024的最佳论文奖,并申请／获得6项国家发明专利。本方向的研究工作得到了湖北省重点研究计划、国家自然科学面上基金等资助。本方向的研究成果已在华为云（GaussDB）、国家电网的实际生产场景中实现落地，为企业持续提升经济效益。

![时序](/assets/images/research/时序1.png)
图1：多变量时间序列异常检测模型STAMP

![时序](/assets/images/research/时序2.png)
图2：分布式数据库智能运维系统MindDx

![时序](/assets/images/research/时序3.jpeg)
图3：时间序列数据库的去中心化日志系统DecLog

## 参考文献

[1]Wenjing Wang, Ziyang Yue, Bolong Zheng. Streaming Time Series Subsequence Anomaly Detection: A Glance and Focus Approach. PVLDB 2025: 1892-1904.
[2]Bolong Zheng, Lingfeng Ming, Kai Zeng, Mengtao Zhou, Xinyong Zhang, Tao Ye, Bin Yang, Xiaofang Zhou, Christian S. Jensen. Adversarial Graph Neural Network for Multivariate Time Series Anomaly Detection. TKDE 36(12): 7612-7626 (2024).
[3] Tingyang Chen, Bolong Zheng, Shuncheng Liu, Zhujiong Fan, Zhi Xu, Lingsen Yan, Kai Zeng, Tao Ye, Xiaofang Zhou. Compatible Unsupervised Anomaly Detection with Multi-Perspective Spatio-Temporal Learning. ICDE 2025: 4066-4078.
[4] Lingsen Yan, Bolong Zheng, Junjie Qing, Wenlong You, Tingyang Chen, Zhi Xu, Shuncheng Liu, Kai Zeng, Tao Ye, Xiaofang Zhou. Anomaly Diagnosis with Siamese Discrepancy Networks in Distributed Cloud Databases. ICDE 2025: 4053-4065.
[5] Bolong Zheng, Yongyong Gao, Jingyi Wan, Lingsen Yan, Long Hu, Bo Liu, Yunjun Gao, Xiaofang Zhou, Christian S. Jensen. DecLog: Decentralized Logging in Non-Volatile Memory for Time Series Database Systems. PVLDB 2024: 1-14.