import numpy as np
import matplotlib.pyplot as plt

def random_walk_finals(num_steps, num_walks):
    """生成多个二维随机游走的终点位置
    
    通过模拟多次随机游走，每次在x和y方向上随机选择±1移动，
    计算所有随机游走的终点坐标。每个随机游走都从原点(0,0)开始。

    参数:
        num_steps (int): 每次随机游走的步数
        num_walks (int): 随机游走的次数
        
    返回:
        tuple: 包含两个numpy数组的元组 (x_finals, y_finals)
            - x_finals: 所有随机游走终点的x坐标数组，长度为num_walks
            - y_finals: 所有随机游走终点的y坐标数组，长度为num_walks
            
    示例:
        >>> x_finals, y_finals = random_walk_finals(1000, 100)
        >>> print(f"第一个终点坐标: ({x_finals[0]}, {y_finals[0]})")
    """
    # TODO: 实现随机游走算法
    # 提示：
    # 1. 使用np.zeros初始化坐标数组
    # 2. 对每次游走使用np.random.choice生成±1的随机步长
    # 3. 使用np.sum计算总位移
    pass

def plot_endpoints_distribution(endpoints):
    """绘制二维随机游走终点的空间分布散点图
    
    将多次随机游走的终点在二维平面上可视化，观察其空间分布特征。
    图形包含所有终点的散点图，并保持x和y轴的比例相同。

    参数:
        endpoints: 包含x和y坐标的元组 (x_coords, y_coords)
            - x_coords: numpy数组，所有终点的x坐标
            - y_coords: numpy数组，所有终点的y坐标
            
    示例:
        >>> endpoints = random_walk_finals(1000, 1000)
        >>> plot_endpoints_distribution(endpoints)
        >>> plt.show()
    """
    # TODO: 实现散点图绘制
    # 提示：
    # 1. 使用endpoints解包获取x和y坐标
    # 2. 使用plt.scatter绘制散点图
    # 3. 设置坐标轴比例、标题和标签
    pass

def analyze_x_distribution(endpoints):
    """分析二维随机游走终点x坐标的统计特性
    
    对随机游走终点的x坐标进行统计分析，计算样本均值和样本方差，
    并通过直方图和理论正态分布曲线可视化其分布特征。理论上，
    大量随机游走的终点x坐标应该服从正态分布。

    参数:
        endpoints: 包含x和y坐标的元组 (x_coords, y_coords)
            - x_coords: numpy数组，所有终点的x坐标
            - y_coords: numpy数组，所有终点的y坐标
    
    返回:
        tuple: (mean, variance)
            - mean (float): x坐标的样本均值
            - variance (float): x坐标的样本方差（使用n-1作为分母）
            
    示例:
        >>> endpoints = random_walk_finals(1000, 1000)
        >>> mean, var = analyze_x_distribution(endpoints)
        >>> print(f"均值: {mean:.2f}, 方差: {var:.2f}")
    """
    # TODO: 实现统计分析和可视化
    # 提示：
    # 1. 提取x坐标数据
    # 2. 使用numpy计算均值和方差
    # 3. 绘制直方图
    # 4. 添加理论正态分布曲线
    # 5. 设置图形属性并打印统计结果
    pass

if __name__ == "__main__":
    np.random.seed(42)  # 设置随机种子以保证可重复性
    
    # 生成数据
    endpoints = random_walk_finals(1000, 1000)

    # 创建图形
    plt.figure(figsize=(12, 5))
    
    # 绘制终点分布
    plt.subplot(121)
    plot_endpoints_distribution(endpoints)
    
    # 分析x坐标分布
    plt.subplot(122)
    analyze_x_distribution(endpoints)
    
    plt.tight_layout()
    plt.show()
    import numpy as np
import matplotlib.pyplot as plt
from math import factorial, exp

# 定义泊松分布的概率质量函数
def poisson_pmf(l, lam):
    return (lam**l * exp(-lam)) / factorial(l)

# 模拟抛硬币实验
def coin_toss_simulation(N):
    results = []
    for _ in range(N):
        tosses = np.random.choice([1, 0], size=100, p=[0.08, 0.92])
        heads_count = np.sum(tosses)
        results.append(heads_count)
    return results

# 绘制理论分布和实验结果
def plot_results(N):
    lam = 8
    l_values = np.arange(0, 20)
    theoretical_pmf = [poisson_pmf(l, lam) for l in l_values]

    # 进行数值模拟
    experimental_results = coin_toss_simulation(N)

    # 绘制实验结果的直方图
    plt.hist(experimental_results, bins=20, range=(0, 20), density=False, alpha=0.7, label='实验结果')

    # 绘制理论泊松分布曲线
    plt.plot(l_values, np.array(theoretical_pmf) * N, 'r-', label='理论泊松分布')

    plt.xlabel('正面朝上的次数')
    plt.ylabel('频数')
    plt.title('抛硬币实验的理论与实验分布')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    N = 1000  # 实验组数
    plot_results(N)    
