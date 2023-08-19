## 一、微积分

### 1.导数（一元情况）

**1.1  一元最优化**

最小二乘法（最小化问题），最大似然估计（最大化问题）

无约束条件下最值问题必要条件：一阶导为0，最大值二阶导数<=0，最小值二阶导>=0

一般假设二阶条件成立，只关注一阶导

### 2.偏导数（多元情况）

**2.1 多元最优化**


<img src="https://www.zhihu.com/equation?tex=X_{1}，X_{2}，....X_n$$），要求所有偏导数都为0

### 3.积分

定积分，不定积分

## 二、线性代数

### 1.矩阵

m×n：m行n列，$ <img src="https://www.zhihu.com/equation?tex=A_{m \times n}" alt="X_{1}，X_{2}，....X_n" alt="A_{m \times n}" alt="X_{1}，X_{2}，....X_n" class="ee_img tr_noresize" eeimg="1"> $），要求所有偏导数都为0

### 3.积分

定积分，不定积分

## 二、线性代数

### 1.矩阵

m×n：m行n列，$$A_{m \times n}" class="ee_img tr_noresize" eeimg="1">


<img src="https://www.zhihu.com/equation?tex=a_{ij}$$：表示矩阵A第i行第j列元素

零矩阵：相当于0的作用

### 2.方阵

m=n，有主对角线，$ <img src="https://www.zhihu.com/equation?tex=a_{11}，a_{22}，a_{33}" alt="a_{11}，a_{22}，a_{33}" class="ee_img tr_noresize" eeimg="1"> $....为主对角线上的元素，其他元素为非主对角线元素

如果 $ <img src="https://www.zhihu.com/equation?tex=A_{ij}=A_{ji}" alt="A_{ij}=A_{ji}" class="ee_img tr_noresize" eeimg="1"> $ ，则矩阵A为对称矩阵

如果非主对角线元素全为0，则称为对角矩阵

如果对角矩阵主对角线元素全为1，则为单位矩阵

方阵>对称矩阵>对角矩阵>单位矩阵

### 3.矩阵的转置

转置矩阵A'，$ <img src="https://www.zhihu.com/equation?tex=A_{n×m}" alt="A_{n×m}" class="ee_img tr_noresize" eeimg="1">  <img src="https://www.zhihu.com/equation?tex=， " alt="， " class="ee_img tr_noresize" eeimg="1">  <img src="https://www.zhihu.com/equation?tex=(A')_{ij}=A_{ji}" alt="a_{ij}" alt="(A')_{ij}=A_{ji}" alt="a_{ij}" class="ee_img tr_noresize" eeimg="1"> $：表示矩阵A第i行第j列元素

零矩阵：相当于0的作用

### 2.方阵

m=n，有主对角线，$ <img src="https://www.zhihu.com/equation?tex=a_{11}，a_{22}，a_{33}" alt="a_{11}，a_{22}，a_{33}" class="ee_img tr_noresize" eeimg="1"> $....为主对角线上的元素，其他元素为非主对角线元素

如果 $ <img src="https://www.zhihu.com/equation?tex=A_{ij}=A_{ji}" alt="A_{ij}=A_{ji}" class="ee_img tr_noresize" eeimg="1"> $ ，则矩阵A为对称矩阵

如果非主对角线元素全为0，则称为对角矩阵

如果对角矩阵主对角线元素全为1，则为单位矩阵

方阵>对称矩阵>对角矩阵>单位矩阵

### 3.矩阵的转置

转置矩阵A'，$ <img src="https://www.zhihu.com/equation?tex=A_{n×m}" alt="A_{n×m}" class="ee_img tr_noresize" eeimg="1">  <img src="https://www.zhihu.com/equation?tex=， " alt="， " class="ee_img tr_noresize" eeimg="1"> $(A')_{ij}=A_{ji}" class="ee_img tr_noresize" eeimg="1">

对称矩阵转置后还是本身

(A')'=A

### 4.向量

向量是矩阵的特例


<img src="https://www.zhihu.com/equation?tex=a'b=a_{1}b_{1}+a_{2}b_{2}+a_{3}b_{3}...." alt="a'b=a_{1}b_{1}+a_{2}b_{2}+a_{3}b_{3}...." class="ee_img tr_noresize" eeimg="1">

如果a'b=0，二者正交，在n维空间中垂直

$ <img src="https://www.zhihu.com/equation?tex=\sum a_{i}^2" alt="\sum a_{i}^2" class="ee_img tr_noresize" eeimg="1"> $=A'A

### 5.矩阵的加法

两个矩阵的维度完全相同则可以相加，新矩阵的元素为相应元素相加，其满足：

加上零矩阵不改变矩阵；加法交换律；加法结合律；(A+B)'=A'+B'

### 6.矩阵的数乘

$ <img src="https://www.zhihu.com/equation?tex=kA=(ka_{ij})_{m×n}" alt="kA=(ka_{ij})_{m×n}" class="ee_img tr_noresize" eeimg="1"> $，每一个元素都乘以这个数

### 7.矩阵的乘法

A×B，简记AB，要求矩阵A的列数与矩阵B的行数相同

一般来说不满足交换律，需要区分左乘和右乘

乘以单位矩阵不改变矩阵；满足乘法结合率 (AB)C=A(BC)；满足分配律A(B+C)=AB+AC

(AB)'=B'A', (ABC)'=C'B'A'

![img](https://urldefense.com/v3/__https://pic1.zhimg.com/80/v2-b12ae60012607a73387b4600e56e13ae_1440w.png?source=d16d100b__;!!Mih3wA!CBT_-NNJ1YLfbQHAhxSfgYdxtTk9lcTs3wXmgnLkuFzqEMhxuR3rsalrqHTKB_i8HmljqAV6Gjr04Bnc$ )

### 8.线性方程组

![img](https://urldefense.com/v3/__https://picx.zhimg.com/80/v2-6012f5a37dbe1d18ed4fe38da8975c7a_1440w.png?source=d16d100b__;!!Mih3wA!CBT_-NNJ1YLfbQHAhxSfgYdxtTk9lcTs3wXmgnLkuFzqEMhxuR3rsalrqHTKB_i8HmljqAV6GqoC3lBh$ )

Ax=b，A为系数矩阵

### 9.逆矩阵

AB=BA=I，A为可逆矩阵，B为A唯一的逆矩阵

A可逆的充分必要条件：|A|不等于0

逆矩阵满足规则：（A-1)'=(A')-1 转置和逆可以交换顺序；

$ <img src="https://www.zhihu.com/equation?tex=（AB)^{-1}=B^{-1}A^{-1};(ABC)^{-1}=C^{-1}B^{-1}A^{-1}" alt="（AB)^{-1}=B^{-1}A^{-1};(ABC)^{-1}=C^{-1}B^{-1}A^{-1}" class="ee_img tr_noresize" eeimg="1"> $，成绩求逆交换次序

### 10.矩阵的秩

**10.1 线性相关、线性无关**

**10.2 秩**

![img](https://urldefense.com/v3/__https://picx.zhimg.com/80/v2-21973c277a611a412e307e0f49b656b0_1440w.png?source=d16d100b__;!!Mih3wA!CBT_-NNJ1YLfbQHAhxSfgYdxtTk9lcTs3wXmgnLkuFzqEMhxuR3rsalrqHTKB_i8HmljqAV6Gtv3ymoI$ )

$ <img src="https://www.zhihu.com/equation?tex=A_{m×n}" alt="A_{m×n}" class="ee_img tr_noresize" eeimg="1"> $的列秩刚好等于n，则称矩阵A满列秩。矩阵的行秩和列秩一定相等，称为矩阵的秩

### 11. 二次型

二次齐次多项式函数

![img](https://urldefense.com/v3/__https://picx.zhimg.com/80/v2-66c0df0f89ca8f739c8a155fc625d701_1440w.png?source=d16d100b__;!!Mih3wA!CBT_-NNJ1YLfbQHAhxSfgYdxtTk9lcTs3wXmgnLkuFzqEMhxuR3rsalrqHTKB_i8HmljqAV6GoZhIHuv$ )

![img](https://urldefense.com/v3/__https://pica.zhimg.com/80/v2-986ac5fbca26a280c844ba07168c4c08_1440w.png?source=d16d100b__;!!Mih3wA!CBT_-NNJ1YLfbQHAhxSfgYdxtTk9lcTs3wXmgnLkuFzqEMhxuR3rsalrqHTKB_i8HmljqAV6GiAkwMNk$ )



![img](https://urldefense.com/v3/__https://picx.zhimg.com/80/v2-73a9ff47ccc51d4c3c65cfa92ae7d899_1440w.png?source=d16d100b__;!!Mih3wA!CBT_-NNJ1YLfbQHAhxSfgYdxtTk9lcTs3wXmgnLkuFzqEMhxuR3rsalrqHTKB_i8HmljqAV6GiH5ca6x$ )



一维情况下：当二次矩阵>0时，x为非0列向量时，f（x）>0，为正定矩阵；反之为负定矩阵

二维情况下：有正定，负定，不定，半正定（只能保证非负），半负定

正定矩阵可以通过线性变化转变为主对角线元素全为正数的对角矩阵，这些主对角线元素为矩阵A的特征值。故正定矩阵A一定可逆。

![img](https://urldefense.com/v3/__https://picx.zhimg.com/80/v2-b44b4ec1d4314cac7a5e3f500e3e9823_1440w.png?source=d16d100b__;!!Mih3wA!CBT_-NNJ1YLfbQHAhxSfgYdxtTk9lcTs3wXmgnLkuFzqEMhxuR3rsalrqHTKB_i8HmljqAV6GhV6kumF$ )

![img](https://urldefense.com/v3/__https://pic1.zhimg.com/80/v2-b281428f567beab95a5f44affe70b3e8_1440w.png?source=d16d100b__;!!Mih3wA!CBT_-NNJ1YLfbQHAhxSfgYdxtTk9lcTs3wXmgnLkuFzqEMhxuR3rsalrqHTKB_i8HmljqAV6GrWAU3e2$ )

## 三、概率统计

### 1.概率，条件概率，独立事件

### 2.全概率公式

![img](https://urldefense.com/v3/__https://picx.zhimg.com/80/v2-e4c2c9388bac924ee811c187cdc3ae66_1440w.png?source=d16d100b__;!!Mih3wA!CBT_-NNJ1YLfbQHAhxSfgYdxtTk9lcTs3wXmgnLkuFzqEMhxuR3rsalrqHTKB_i8HmljqAV6GgeZ2C2s$ )



## 3.分布与条件分布

**3.1 离散型概率分布**

两点分布（Bernoulli）、二项分布（binomial）、泊松分布

**3.2 连续型概率分布**

概率密度函数（pdf, probability density function)

累计分布函数（cdf, cumulative distribution function)

**3.3 多维随机向量的概率分布**

联合密度函数

![image-20230818101134290](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20230818101134290.png)

**3.4 条件分布**

![image-20230818101319853](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20230818101319853.png)

## 4.随机变量的数据特征

**4.1 期望**

![image-20230818101541139](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20230818101541139.png)

**4.2 方差**

![image-20230818101634252](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20230818101634252.png)

**4.3 协方差**

![image-20230818101815349](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20230818101815349.png)

![image-20230818101923045](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20230818101923045.png)

**4.4 相关系数**

![image-20230818102058720](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20230818102058720.png)

上述积分（比如求期望、方差的积分）必须收敛，否则随机变量的数字特征可能不存在。

**4.5 矩**

![image-20230818102153768](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20230818102153768.png)

![image-20230818102301300](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20230818102301300.png)

![image-20230818102338812](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20230818102338812.png)

**4.6 条件期望**

相当于草帽竖着切一刀

![image-20230818104131371](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20230818104131371.png)

**4.7 条件方差**

![image-20230818104158735](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20230818104158735.png)

![image-20230818105811166](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20230818105811166.png)

好好想想这个示意图就理解了

**4.8 多维随机变量数字特征**（重要）

协方差矩阵

![image-20230818114430375](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20230818114430375.png)

![image-20230818115155636](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20230818115155636.png)

以上数字特征都为“总体矩”

在抽取随机样本后，可用样本数据计算相应的“样本矩”，作为总体矩的估计值

即用样本的平均值代替总体矩表达式的期望算子（如，用样本均值估计总体均值或期望）
