---
layout: research_article
title: 数据库新技术
description: AI4DB、新型存储数据管理等前沿数据库技术研究与创新
permalink: /research/articles/new-database-technologies/
---


## Text-to-SQL关键技术

Text-to-SQL 通过自然语言交互方式降低结构化数据访问门槛，提升数据资产的可用性与普惠性，可直接支撑 BI（Business Intelligence） 报表、数据分析、客服问答、运营监控、教育科研、政务民生等场景，有助于充分释放数据要素的产业价值。

Text-to-SQL 需将用户自然语言形式的查询语句映射为可执行的SQL，但实践中面临不完整提问、跨域模式关联稀疏、长尾实体与未见词（OOD，Out of Distribution）、重复生成与可执行性保障等挑战。课题组围绕“关系与语义联合建模、抽取-生成一体化解码、历史知识与动态上下文增强、语音模板化理解到结构化检索、大模型赋能SQL生成”的技术主线，构建面向真实系统的端到端方法体系，兼顾精度、速度与可落地性。

1） 场景模板化Text2SQL。针对驾驶、出行等手眼受限场景，提出语音路径描述语言理解框架SpeakNav，首次把“途经POI+距离”的口语化表达转化为可执行的路径模板，设计RT-BERT联合模型一次性完成意图识别与POI-距离槽位填充，并给出混合标签索引+PB-tree驱动的分支限界搜索，实现自然语言到空间路径的秒级生成，为Text2SQL走出数据库、嵌入物理世界提供了范例。

2） 不完整查询自动补全。面向“用户只输入片段即期望完整SQL”的真实痛点，提出RHB-Net关系-历史双桥接网络：在编码端通过“问题-模式”互注意与“历史-当前”影响因子联合建模，消歧用户意图；在解码端引入动态上下文向量，实时抑制已生成元素的重复出现；辅以课程学习由“高完整性”到“低完整性”渐进训练，使模型在Spider等基准上RECALL@5、MRR@5、SAVE@5全面领先，首次把Text2SQL从“完整问句”推向“任意前缀”的实用阶段。

3）随着大模型时代到来，课题组积极研究大模型驱动的 Text2SQL。提出动态置信度SQL生成框架DC-SQL，通过在大模型推理阶段引入 Test-time Scaling，对多条推理生成SQL路径进行置信度评估与排序，选择最优路径；同时融入动态剪枝，实时淘汰低置信度分支，兼顾精度与吞吐，显著提升端到端生成速度与稳定的可执行率。进一步结合模式约束与执行反馈闭环，面向复杂、多步推理与跨域模式的工业级落地场景，强化推理质量控制与时延优化的协同，为企业数据智能提供高效稳定的自然语言查询能力。
本方向的研究成果发表在VLDB、SIGIR等重要学术期刊和会议上，团队正在积极探索大模型时代的Text-to-SQL新模式，并实现关键技术突破及相关应用落地。

![SpeakNav系统架构图](/assets/images/research/AI4DB-Text2SQL1.jpg)


![RHB-Net网络结构图](/assets/images/research/AI4DB-Text2SQL2.jpg)



![DC-SQL框架图](/assets/images/research/AI4DB-Text2SQL3.jpg)


已发表成果
[1] Bolong Zheng, Lei Bi, Juan Cao, Hua Chai, Jun Fang, Lu Chen, Yunjun Gao, Xiaofang Zhou, Christian S. Jensen: SpeakNav: Voice-based Route Description Language Understanding for Template Driven Path Search. Proc. VLDB Endow. 14(12): 3056-3068 (2021)

[2] Bolong Zheng, Lei Bi, Ruijie Xi, Lu Chen, Yunjun Gao, Xiaofang Zhou, Christian S. Jensen: RHB-Net: A Relation-aware Historical Bridging Network for Text2SQL Auto-Completion. SIGIR 2023: 1458-1467

## AI4DB关键技术
 本研究方向围绕AI4DB技术展开，涵盖数据查询资源推荐、AI4DB中间件部署、资源感知成本建模、查询优化器退化消除，形成覆盖查询优化与向量数据管理的关键技术体系。

1）数据查询资源推荐：针对云平台大数据查询中传统优化忽视资源成本、资源与性能映射复杂的问题，LORE[1]整合SQL查询语句与查询执行计划双信息源，通过图神经网络建模学习资源分配与性能收益关系，实现了查询最优资源的高效精准估计。

2）AI4DB中间件技术：针对AI驱动数据库部署难、ML与DB开发范式差异大、算法复用低的问题，PilotScope[2]采用“AI4DB驱动+DB交互器”分层架构，包含算法流程、模型及训练推理逻辑的 AI4DB 驱动，通过统一push/pull算子与数据库交互，让DB开发者以轻量级补丁实现DB交互器，屏蔽底层细节。

3）资源感知成本估计：针对Spark SQL传统成本模型依赖手工规则、未考虑资源动态变化的问题，RAAL[3]模型融合资源特征与统计信息，通过LSTM学习不同资源下的查询计划执行代价，实现了查询执行时间的精准预测，适配云环境资源动态变化场景。

4）查询优化器消除退化：针对学习型查询优化器因欠拟合、泛化差导致的性能退化问题，Eraser[4]以插件形式采用两阶段过滤策略：粗粒度过滤通过 “未预期计划探索器” 筛选模型预测精度低的计划子空间；细粒度评估通过 “分段模型” 对剩余计划聚类并关联可靠性区间，平衡退化风险与性能收益。Eraser实现了高风险计划的有效过滤，适配动态数据场景与多数据库。

本方向的研究成果发表在SIGMOD、VLDB、ICDE等重要学术期刊和会议上，申请/获得4项国家发明专利。团队在此方向与阿里云等知名企业展开合作，并实现相关技术的应用落地。
![最佳资源推荐学习框架](/assets/images/research/AI4DB1.png)



![资源感知的查询和计划表示学习框架](/assets/images/research/AI4DB2.png)



![AI和DB中间件](/assets/images/research/AI4DB3.png)



![性能衰退消除](/assets/images/research/AI4DB4.png)


已发表成果
[1] Li Y, Wang L, Wang S, Sun Y, Peng Z. A resource-aware deep cost model for big data query processing. In2022 IEEE 38th International Conference on Data Engineering (ICDE) 2022 May 9 (pp. 885-897). IEEE.

[2] Zhu R, Weng L, Wei W, Wu D, Peng J, Wang Y, Ding B, Lian D, Zheng B, Zhou J. Pilotscope: Steering databases with machine learning drivers. Proceedings of the VLDB Endowment. 2024 Jan 1;17(5):980-93.

[3] Li Y, Wang L, Zheng B, Peng Z. LORE: Learning-Based Resource Recommendation for Big Data Queries. In2025 IEEE 41st International Conference on Data Engineering (ICDE) 2025 May 19 (pp. 1732-1744). IEEE.

[4] Weng L, Zhu R, Di Wu BD, Zheng B, Zhou J. Eraser: Eliminating Performance Regression on Learned Query Optimizer. PVLDB 17, 5 (2024), 926–938 [Internet]. 2024


## 新型存储技术

存储是高效计算系统的基石。为应对数据密集型应用带来的性能与能效瓶颈，本研究聚焦于存储技术的全链路优化。我们致力于探索包括固态盘、新型非易失存储器（NVM）在内的硬件架构创新，以及贯穿固态盘与数据库的软硬件协同优化机制。

1）固态盘：在读重试延迟优化方面，PreLDPC [1,2] 引入了最终读取层级的预测机制与细粒度电压步进技术。该方案通过提前定位最优读取电压并精细化搜索过程，显著减少了不必要的读操作迭代，有效降低了系统读取延迟。面对3D闪存中层间误码率差异显著的新挑战，MG-LDPC [3] 设计了一种多粒度LDPC读取框架。其核心在于构建了多种不同粒度的解码引擎，并能动态适配，实现了对整体读取延迟的自适应优化。为缓解3D闪存因垂直堆叠引发的跨层级耐久度失衡，LA-Write [4] 提出了一种基于分层概率的写入跳过策略。该方案以概率方式调控不同层级的写入操作，有效均衡了层间磨损，延长固态盘的使用寿命。在垃圾回收导致的性能陡降问题上，PreGC [5] 采取了前瞻性的页面迁移思路，将传统GC过程中集中的页面迁移工作分散到前期空闲时段完成，最终以微小的写放大代价，大幅降低了高百分位尾延迟。

2）非易失存储器：针对非易失性内存（NVM）写入延迟高与寿命有限的核心挑战，DCom[6]采用自适应压缩方案，通过智能分析数据模式有效减少了写入量，从而在提升系统性能的同时延长了NVM使用寿命。针对数据压缩在节省NVM空间时，会因数据收缩引发块内磨损不均反而损害寿命的问题，SlidW[7]设计滑动写入方法，通过将压缩数据分散写入整个内存块，有效均衡了磨损，从而延长了NVM寿命。针对持久内存原子持久性实现方案因依赖易失性缓存而导致性能开销高的问题，LOAD[8]通过构建事务感知缓存与设备友好日志机制，在保证崩溃一致性的同时将性能开销降至1%以内，并在大写入集场景下实现显著性能提升。

3）数据库与存储器软硬件协同优化：旨在结合高性能固态盘和数据库数据存储特征协同软硬件共同优化系统性能。RemapCom [9] 通过识别并保留在压缩中内容未变的"未变更数据块"，直接从地址映射层面跳过了对这些数据块的物理重写，从而显著降低了写放大。NoLgn-FTL [10] 则利用闪存的多版本特性，通过FTL层保留数据的旧版本以实现即时回滚，从而免除了数据库写日志的开销。ADM[11]针对混合内存架构中内存容量有限且传统硬件管理策略未充分利用应用层数据访问特征的问题，提出面向应用的数据迁移方法，通过热度识别与迁移机制将高频访问数据动态分配至内存，最终在提升内存数据库性能的同时显著降低了系统能耗。针对LSM-tree键值存储系统中数据压缩操作引发的尾部延迟尖峰问题，[12]提出限制性压缩方法，通过随机选择或基于重叠范围选择部分SSTable参与压缩，在可控写入放大代价下有效降低了尾部延迟。

本方向的研究成果发表在TCAD、TODAES、DATE、JSA等重要学术期刊和会议上，申请/获得6项国家发明专利。

![LDPC 细粒度读取和预测模型](/assets/images/research/存储器方向1.png)


![细粒度LDPC动态解码引擎](/assets/images/research/存储器方向2.png)


![冗余更新数据处理框架](/assets/images/research/存储器方向3.png)


![数据库-NVM-固态盘软硬件协同优化架构](/assets/images/research/存储器方向4.png)


## 已发表成果
[1] Du, Yajuan，Gao, Yuan， Huang, Siyi，Li, Qiao.LDPC Level Prediction Toward Read Performance of High-Density Flash Memories.TCAD 2023:3264-3274

[2] Yajuan Du，Yuan Gao，Qiao Li.Work-in-Progress: Prediction-based Fine-Grained LDPC Reading to Enhance High-Density Flash Read Performance.CASES 2022.

[3] Du，Yajuan，Huang, Siyi，Zhou, Yao，Li, Qiao.Towards LDPC Read Performance of 3D Flash Memories with Layer-induced Error Characteristics.TODAES.28(3),1-25(2023)

[4] Huang, Siyi，Du, Yajuan，Fan, Yi，Ji, Cheng. Extending SSD Lifetime via Balancing Layer Endurance in 3D NAND Flash Memory.DATE 2024.

[5] Yajuan Du, Wei Liu, Yuan Gao, Rachata Ausavarungnirun.Observation and optimization on garbage collection of flash memories: The view in performance cliff.Micromachine 2021.

[6] Jialin Wang, Zhen Yang, Zhenghao Yin, Yajuan Du.Adaptive NVM Word Compression Based on Cache Line Dynamics on Micro-Architecture.Preprints 2025, 2025041172.

[7] Kailun Jin, Yajuan Du, Mingzhe Zhang, Zhenghao Yin, Rachata Ausavarungnirun.Relieving compression-induced local wear on non-volatile memory block via sliding writes.Micromachines 2023.

[8] Taiyu Zhou, Yajuan Du, Fan Yang, Xiaojian Liao, Youyou Lu.Efficient Atomic Durability on eADR-Enabled Persistent Memory.PACT 22:124-134.

[9] Fan, Yi，Du, Yajuan，Noh, Sam H.RemapCom: Optimizing Compaction Performance of LSM Trees via Data Block Remapping in SSDs.DATE 2025.

[10] Yin, Zhenghao,Du, Yajuan,Fan, Yi，Noh, Sam H.Eliminating duplicate writes of logging via no-logging flash translation layer in SSDs.JSA 2025.

[11] Wenze Zhao, Yajuan Du, Mingzhe Zhang, Mingyang Liu, Kailun Jin, Rachata Ausavarungnirun.Application-Oriented Data Migration to Accelerate In-Memory Database on Hybrid Memory.Micromachines 2021.

[12] Yongchao Hu, Yajuan Du.Reducing tail latency of LSM-tree based key-value store via limited compaction.SAC 2021.