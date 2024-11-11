# CVPR2024 Event Camera-Related Works

#### Towards Robust Event-guided Low-Light Image Enhancement: A Large-Scale Real-World Event-Image Dataset and Novel Approach 

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240522212523772.png" alt="image-20240522212523772" style="zoom:30%;" />

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240522212545625.png" alt="image-20240522212545625" style="zoom:30%;" />

- 目标：低光照下基于Events的图片增强
- 用机械臂严格的采集了一个数据集
- 采用了信噪比引导的区域特征选择
- 有整体和局部特征的融合（Holistic-Regional Fusion Branch）
- 他们在采集弱光数据时候用的不是直接降低环境光照，而是给相机镜头前面安装一个滤光片（ND8 Filter）
- 有点好奇他们Holistic Feature Extraction (HFE)部分是怎么对3D的Feature Map做的Multi-Head Attn的。

#### Event Stream-based Visual Object Tracking: A High-Resolution Benchmark Dataset and A Novel Baseline

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240522212452864.png" alt="image-20240522212452864" style="zoom:40%;" />

- 目标：基于patch的tracking
- 采集了一个新的高分辨率数据集
- 使用了teacher-student network进行知识蒸馏，不过老师网络的输入不论是template还是target，都既有image的patch，又有events的patch；而student network则只有event patches。Student网络多了一个positional encoding。
- Teacher和Student都是Transformer。
- 他们的event Representation也是event voxel。

#### EventEgo3D: 3D Human Motion Capture from Egocentric Event Streams

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240522213801298.png" alt="image-20240522213801298" style="zoom:30%;" />

- 一个核心创新点是用前面的event frame中高度可能是来源于操作人的events一定程度上加到当前event frame上，相当于用前面帧中的human events来增强当前帧的human events，从而使得背景events fade out。这个说实话可能仅适用于event frame sliding window step比较小的情况，因为前后两帧的内容差别比较小。本质就是一个human mask，可能还不如human mask。
- Segmentation Decoder就是human mask predictor，之后过一个sigmoid就摇身一变成了confidence map，最后这个confidence map直接作用于前面缓存的event frames，然后加到当前event frame上。
- 比较有趣（可能是之前没看过太多Ego3D的paper）的点是先预测在xy平面上的各个joints的heatmap，然后通过把这个2D Heatmap作为输入，进一步输入到一个2D to 3D Block中得到3D pose的操作。

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240522213829197.png" alt="image-20240522213829197" style="zoom:30%;" />

#### Seeing Motion at Nighttime with an Event Camera

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240523153142102.png" alt="image-20240523153142102" style="zoom:30%;" />

- 目标是通过Events还原对应的Gray Scale Frame，但是限定在低光照条件下，强调事件相机在夜间场景的应用。

- 他们发现了一个现象：对于夜间或低环境光照的情况下，离人造光源越近，附近的事件产生的越多。同时，人工光照区和背景的亮度差越大，整体产生的事件越多。

  <img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240523161419658.png" alt="image-20240523161419658" style="zoom:25%;" />

- 他们还发现了另一个物理现象：当光照亮度提高时，光传感器的截止频率也会提高，即相机可以对更高频（紫色方向）的光保持敏感性；而低光照条件下，这个截止频率也会降低，即相机能捕捉到的光的频率上限降低。同时，更高的截止频率会导致相应时间降低，这又会进一步导致模糊程度（事件相机的话是拖尾事件量）降低，拥有更高的空间分辨率。

  <img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240523161352247.png" alt="image-20240523161352247" style="zoom:25%;" />

- Learnable Event Timestamps Calibration本质上是在event voxel generation步骤的一个操作。假设有K个time bin，这段时间内(x,y)处有N个events，他们的目标就是生成一个(N,K)的权重矩阵，计算每个events对每个time bin的贡献度。作为对比，之前这个贡献度的算法就是贡献给当前voxel和下一个voxel，按照(t%t_bin)的大小来分配。

- 如果是非Learnable的ETC，他们对拖尾事件的定义条件有三个：1. 相同极性 2. 间隔时间越来越长 3. 最大时间间隔小于一个阈值

- 至于另一个模型上的贡献，则是所谓的Non-Uniform Illumination Aware Module，它的本质就是一个ConvLSTM，但是做了一些modification，让每个cell能更好地得到相对远程的信息，而不是随着经过的cell数增加而逐渐遗忘。同时，还增加了hierarchical的空间信息传导。这个模块说实话有点凑数，纯粹为了加创新点而加的。十分怀疑这么需要长程依赖为什么不用Transformer。

- 他们采集了一个大的夜间paired RGB-Events数据集，光照条件式非均的（即存在人造点光源），并在多种不同的环境光照度下采集了数据。

- 他们使用了ND Filter（Neutral Density Filter，减光镜）来让event camera得到的光照更少。RGB不用减光镜是为了生成所谓的pseudo-GT，即夜晚条件下通过events reconstruction得到的gray scale frame的GT。

- 他们使用的RGB与Events以及光照强度的同步数据采集平台：

  <img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240523153014803.png" alt="image-20240523153014803" style="zoom:25%;" />

- 这篇文章很难得的点是它不仅仅是采集了一个新的数据集，或是构建了一个random的新模型，而是针对性的对之前造成问题（事件相机在时域上的拖尾问题）的原理进行了深入的分析，并提出了相对应的解决方案。

#### OpenESS: Event-based Semantic Scene Understanding with Open Vocabularies

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240523174022715.png" alt="image-20240523174022715" style="zoom:33%;" />

- 本文试图做的事情是把CLIP中蕴含的Image-Text pair的knowledge给distill 给event这个模态。具体的task是scene semantic segmentation。
- 他的一个重要claim是不需要给event这个模态提供额外的标签。
- 图中第二行是superpixel-driven contrastive learning（基于超级像素的对比学习），这种方法常用于点云理解、remote sensing，医疗图像处理等等。从图中不难发现，本文中真正和evnet做对比loss的其实是这个superpixel的feature（以及text feature）。
- 只用Superpixel-based contrastive loss也不行，因为这个superpixel本来就比较粗糙，存在属于同一个语义类别的superpixel有的被分类为正样本有的被分类为负样本的情况。
- Event的输入Representation也是event voxel。
- Event的Encoder  <img src="https://www.zhihu.com/equation?tex=F_{\theta_e}^{evt}" alt="F_{\theta_e}^{evt}" class="ee_img tr_noresize" eeimg="1"> 是从头开始训练的。
- 他们是如何做event-to-frame reconstruction的？
  - 默认的CLIP是做不到这点的，只能输出global的label。能做到pixel-level分类的方案主要分为两类：
    1. 更改模型结构：直接重构CLIP Image encoder中的value-embedding layer
    2. 使用fine tune：使用语义标签逐步让预训练权重适应于生成密集prediction
  - 文中这两种方法他们都试了一遍。
  - 这步被他们称为densification。

#### Complementing Event Streams and RGB Frames for Hand Mesh Reconstruction

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240523191916864.png" alt="image-20240523191916864" style="zoom:30%;" />

- 这篇文章的思路很简单：输入events+RGB，输出手部mesh建模。

- 做法也不复杂：

  1. 数据方面，有一个所谓的EvRGB Degrader，用来数据增强，本质是把RGB置于各种极端条件下显得DVS很好用。

  2. 然后是Spatial Alignment模块，输入的是RGB和DVS的Feature，输出的是DVS相对于这个RGB的在DeformConv中的offsets，然后作用到DVS的feature上。本质是想弥补RGB和DVS特征的misalignment，但说实话这样做是否真的有用我存疑。毕竟misalignment是全局的参数问题，而deform conv作用范围是局部。

     <img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240523191842841.png" alt="image-20240523191842841" style="zoom:25%;" />

  3. 接着就是平平无奇的Events-RGB Fusion，Transformer，Temporal Attention，以及最后的Mesh Decoder。

     <img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240523192549793.png" alt="image-20240523192549793" style="zoom:25%;" />

  4. 这个Complementary Fusion的内核就是提取公共信息+Channel Attention。

#### State Space Models for Event Cameras

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240524165313757.png" alt="image-20240524165313757" style="zoom:50%;" />

**背景：DVS Object Detection**

- 最开始是用Dense Representation直接CNN做检测，但是问题是相对移动速度较慢的物体可能无法被检出。
- 后面用了RNN，解决了部分的上述问题，但还是无法解决相对较长时间内相对移速较慢物体无法检出的问题。且带来了新的训练缓慢以及无法被应用于不同sample频率的问题。
- 后面人们开始使用GNN：
  - 但GNN面临的问题是信息难以在大而空旷的XYT空间内有效传递，这在应对大目标和相对移速较慢的目标时候尤为重要。
  - 另外他们提到的一点也很有参考意义，即使用GNN时候需要以events为node构建图，而如果使用全部events图又会太大导致太慢，所以一般都会subsample（比如随机十取一）。然而，subsample可能会带来漏掉重要信息的风险。
- SNN也是一种新的探索方向：
  - 由于SNN的机制是只有当某个neuron的电势积累到了一个阈值之后才emit，所以由于这个不可微的操作会让其难以被训练。
  - 有些方案绕过了这个阈值限制，但是又引入了更深的网络。
  - 整体而言，基于SNN的研究方向尙不完善，需要更多关于基础SNN原理的研究，才能很好的被用于events。

**State Space Models**

- 核心思想：定义一个隐变量x(t)，输入是u(t)，输出是y(t)，那么**隐变量的变化率**是输入和隐变量的线性函数，**输出**也是输入和隐变量的线性函数，即：


<img src="https://www.zhihu.com/equation?tex=\frac{d\mathbf{x}(t)}{dt}=\mathbf{A}\mathbf{x}(t)+\mathbf{B}\mathbf{u}(t), \mathbf{y}(t)=\mathbf{C}\mathbf{x}(t)+\mathbf{D}\mathbf{u}(t)" alt="\frac{d\mathbf{x}(t)}{dt}=\mathbf{A}\mathbf{x}(t)+\mathbf{B}\mathbf{u}(t), \mathbf{y}(t)=\mathbf{C}\mathbf{x}(t)+\mathbf{D}\mathbf{u}(t)" class="ee_img tr_noresize" eeimg="1">
  ，其中， <img src="https://www.zhihu.com/equation?tex=\mathbf{x}(t)\in\mathbb{R}^{P}, \mathbf{u}(t)\in\mathbb{R}^{U}, \mathbf{y}(t)\in\mathbb{R}^{M}" alt="\mathbf{x}(t)\in\mathbb{R}^{P}, \mathbf{u}(t)\in\mathbb{R}^{U}, \mathbf{y}(t)\in\mathbb{R}^{M}" class="ee_img tr_noresize" eeimg="1"> ，  <img src="https://www.zhihu.com/equation?tex=\mathbf{A}\in\mathbb{R}^{P\times P}, \mathbf{B}\in\mathbb{R}^{P\times U}, \mathbf{C}\in\mathbb{R}^{M\times P}, \mathbf{D}\in\mathbb{R}^{M\times U}" alt="\mathbf{A}\in\mathbb{R}^{P\times P}, \mathbf{B}\in\mathbb{R}^{P\times U}, \mathbf{C}\in\mathbb{R}^{M\times P}, \mathbf{D}\in\mathbb{R}^{M\times U}" class="ee_img tr_noresize" eeimg="1"> 。

- SSM的本质是在假设时间序列的因果（输入输出）之间存在着一个用微分方程表征的联系，它很难直接被MLP建模，但可以通过直接提供微分方程模板的形式来辅助网络学习这种高阶的依赖关系。具体而言，就是给出一个hidden state，这个state与输入输出都存在关系，尤其是和输入的关系存在微分特性，然后我们的目标就是在更新这个state的同时学习四个转换矩阵。

- 一个直观的例子，或者说SSM思路的一个可能来源就是高中物理里面常见的一个用力拉弹簧，在考虑摩擦力的情况下求解给定力的大小和时间时，物体运动距离的这样一个任务。其中，力u(t)是输入，位移量y(t)是输出，给定弹簧系数k和墙壁摩擦系数b。这时，一个可行的hidden state就是 <img src="https://www.zhihu.com/equation?tex=[y(t), y'(t)]" alt="[y(t), y'(t)]" class="ee_img tr_noresize" eeimg="1"> 。其公式会完美满足上述的两个式子。具体参见[链接](https://zhuanlan.zhihu.com/p/688831759)。

  <img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/v2-6f7536bcb976511d5c77e5ad3ae2266d_b.jpg" alt="img" style="zoom:33%;" />

**Points**

- 首先，核心backbone是S4, S4D, S5这几个模型，它们是作为CNN和Transformer的替代被提出的，用以提取长程依赖。这类模型被称为连续时间模型。也就是说，模型架构在本文中并非创新点，本文是一个典型的迁移创新样例。因为是第一次SSM被迁移到Events领域，所以他们第一次定义了相关的terms、notation之类，也算是一个contribution。

- 本文也有一些自己的模块创新，这里指的是attention mechanism，又是典型的生造novelty。且这个所谓的novelty还不是热乎的，是他们上一篇paper（Recurrent Vision Transformers for Object Detection with Event Cameras）里面现成的模块，相当于只是单纯把上一篇里面的LSTM换成了SSM直接又拿来卖了。下面是上篇paper的图：

  <img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240524180414421.png" alt="image-20240524180414421" style="zoom:33%;" />

- Events的输入格式是带有极性的event voxel ，形状（2, T, H, W），后面把2和T合并为2T。

#### Recurrent Vision Transformers for Object Detection with Event Cameras

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240524184901188.png" alt="image-20240524184901188" style="zoom:30%;" />

既然上面提到了这篇23年的CVPR论文，这里也展开一下。

- 主要是几个点，一个是Block-SA和Grid-SA，这两个其实实现上基本一样，都是先把feature map切分为一个个小格子。只不过前者是把纵横的格子数都展平放到Batch维度上，让每个格子内部的点去进行相互Attention；而后者则是把feature map切割后的每个格子中的所有像素的值都展平放到Batch维度上，让格子间进行相互Attention。在做这一切的同时，原先的Channel维度没有被动过，全程放在最后一个维度待命，用于作为后续Self Attention中每个cell的dimension。代码参见[Link](https://github.com/uzh-rpg/RVT/blob/master/models/layers/maxvit/maxvit.py#L185)。

  <img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240524190539164.png" alt="image-20240524190539164" style="zoom:25%;" />

- 考虑到上一点，其实做Global的SA（也就是这里的Grid-SA）时候，其实每个patch的( <img src="https://www.zhihu.com/equation?tex=x_0, y_0" alt="x_0, y_0" class="ee_img tr_noresize" eeimg="1"> )处只和其他patch的( <img src="https://www.zhihu.com/equation?tex=x_0,y_0" alt="x_0,y_0" class="ee_img tr_noresize" eeimg="1"> )处的值做了信息交换。但考虑到上一步的Block-SA中已经对每个patch内部做了充分的信息交换，倒是也可以理解为Grid-SA时候每个patch都和其他patch之间在做整体信息交换。

- 所谓的使用LSTM而不用ConvLSTM从而达到使用更少参数更高效的论点其实为真，但不全为真。虽然没有使用ConvLSTM，但是输入依然是二维的而不是一维的，且tensor输入之后也会先进行一个Conv2D。不过LSTM内部的输入门、遗忘门、输出门等并没有用Conv3x3操作实现，而是使用的Conv1x1实现的。相当于是Conv+LSTM（MLP->Conv1x1版），而不是真正意义上的ConvLSTM。参见[Link](https://github.com/uzh-rpg/RVT/blob/master/models/layers/rnn.py)。

  <img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240524190328687.png" alt="image-20240524190328687" style="zoom:25%;" />

#### Mitigating Motion Blur in Neural Radiance Fields with Events and Frames

- 是事件相机在防抖/去抖领域的又一个应用。这次的应用对象是NeRF，即结合运动模糊的RGB和events来生成清晰的NeRF。
- 涉及的NeRF细节比较多，后面再研究。

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240528131317066.png" alt="image-20240528131317066" style="zoom:30%;" />

#### EventDance: Unsupervised Source-free Cross-modal Adaptation for Event-based Object Recognition

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240528132734821.png" alt="image-20240528132734821" style="zoom:30%;" />

- 本文和之前做了半程的Event Domain Adaptation有很大的相似之处。

- 本文强调了只用events，不需要任何paired frame-based data。

- 本文的一个重要贡献点是我印象中首次把多种不同的Event Representation并行处理用于增强表达多样性，并让不同分支输出结果的平均值和source model的输出进行knowledge distillation。这个属于好久不见的Ensemble操作了。同时，不同event Representation 对应的branches的输出也有施加loss，试图让不同Representation经过其对应model得到的值最大可能相似。

- KL散度的两个Input Representation分先后，所以model consistency loss这里分别让frames和events得到的distribution作为第一个输入。

- 文中用到的一个对结果的Visualization方法我们可以学习，TSNE Visualization。

  <img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240528155658854.png" alt="image-20240528155658854" style="zoom:30%;" />

#### Bring Event into RGB and LiDAR: Hierarchical Visual-Motion Fusion for Scene Flow

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240529122118643.png" alt="image-20240529122118643" style="zoom:30%;" />

- 本文的目标是把event这个模态作为LiDar和RGB这两者之间的桥梁，最终目的是融合三者，预测scene flow。证明了这三者含有的信息在视觉空间和动作空间都是互补的。
- 他们这里的融合不仅仅指的是这几种模态的融合，本质上更是视觉信息和motion的融合。
- 本文强调了白天夜晚都能work。
- 本文在融合RGB和Events时候不是直接拿raw的RGB三channel图喂给网络，而是先转换成YUV通道，把明度通道独立和events进行融合，这点物理上合理，能在进行融合events信息的同时保留正确的颜色信息，值得借鉴。

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240529122058903.png" alt="image-20240529122058903" style="zoom:30%;" />

- 他们这张图画的很好，完美的展现了RGB，Events，以及LiDar的特性。其实RGBD可以一定程度上替换Lidar的位置，但RGBD的Spatial Density更高（但有效工作距离更短就是了）。

  <img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240529124255399.png" alt="image-20240529124255399" style="zoom:30%;" />

#### JSTR: Joint Spatio-Temporal Reasoning for Event-based Moving Object Detection

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/CVPR2024 Event Camera-Related Works/image-20240529151531731.png" alt="image-20240529151531731" style="zoom:53%;" />

- 本文提出了一种基于时间空间推理的框架，用在运动目标检测上。
- 本文主要基于一个他们观察到的现象：运动物体形成的事件流在xyt空间中有着明显的柱状结构。在此基础上，他们提出了一种RANSAC 点云结构提取模块。
- 本文采集了一个用于该任务的数据集。
- 本文不是直接就对原始事件流做运动目标检测，而是先根据对应的IMU进行了一个**运动补偿**，让相机自身运动造成的events尽可能地在空间位置上集中，变得更加锐利，然后再基于这个补偿后的events点云进行后续操作。这个补偿模块可以仔细研究下代码，我们也可以拿来用于各种后续task，毕竟DAVIS系列事件相机基本都自带IMU。
- 他们所谓的通过events得到的confidence map也是一个非常简单但也非常符合直觉的有趣操作。
  - 和平常我们常使用的event voxel不同，这里虽然也是把events在时间维度上拍扁了得到一张HxW的张量，但他们并不是直接count这段时间内每个pixel处发生的事件数量。
  - 而是以起始时间点为t=0，让每个pixel处发生的所有events的相对时间给加起来，最后再做一个normalization在每个pixel处得到一个[-1,1]范围内的值。
  - 由于越新的事件其相对时间越大，其占有的分量也就越大；而且由于运动物体在事件域上存在拖尾效应，其所在区域产生的事件数量要远大于背景不运动的区域，这样就自然而然地形成了一个用于检测运动目标当前所在位置的概率图了。
  - 这也是一个值得学习的有效模块化操作。
- 然而，想要从这个所谓的运动目标概率图中真的分割出目标，也并不容易，因为相机自身的运动会大幅影响背景产生事件的密度，所以需要一个方法来动态生成这么一个threshold，用于二分上面提到的概率图，得到运动目标和背景。
  - 本文的做法是再次利用IMU。由于IMU自身本来就含有相机的运动强度和方向信息，所以用一个MLP直接对相机的角速度向量进行几步inference就可以得到想要的threshold了。这也是一个非常有理有据的做法。
- 在这一步之后，还是无法直接得到干净连续的目标区域。他们的做法是使用一种形态学的filter。
  - 具体而言，就是先用Sobel算子对上一步初步得到的segmentation做一个边缘提取
  - 然后用一个固定尺寸的滑窗不断划过这些轮廓，用内积来衡量是否属于一个物体。
