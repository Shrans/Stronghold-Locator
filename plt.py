import matplotlib.pyplot as plt

def plot_ray_t(point1, point2):
    # 计算射线的方向向量
    direction = [point2[0] - point1[0], point2[1] - point1[1]]

    # 设置延伸点坐标
    extension_point = [point1[0] + direction[0] * 1.5, point1[1] + direction[1] * 1.5]

    # 绘制射线
    plt.plot([point1[0], extension_point[0]], [point1[1], extension_point[1]], 'r--')  # 使用红色虚线绘制射线

def plot_points_t(point1, point2):
    plt.style.use('ggplot')
    # 创建图形和坐标轴
    fig, ax = plt.subplots()

    # 绘制射线
    plot_ray_t(point1, point2)

    # 绘制起点和终点
    ax.plot(point1[0], point1[1], 'bo')  # 绘制起点，使用蓝色圆点
    ax.plot(point2[0], point2[1], 'go')  # 绘制终点，使用蓝色圆点

    # 设置坐标轴范围
    #ax.set_xlim([min(point1[0], point2[0]) - 10, max(point1[0], point2[0]) + 10])
    #ax.set_ylim([min(point1[1], point2[1]) - 10, max(point1[1], point2[1]) + 10])

    # 显示图形
    plt.show()


def plot_ray_s(point1, point2, point3):
    # 计算射线的方向向量
    direction1 = [point3[0] - point1[0], point3[1] - point1[1]]
    direction2 = [point3[0] - point2[0], point3[1] - point2[1]]

    # 设置延伸点坐标
    extension_point1 = [point1[0] + direction1[0] * 1.5, point1[1] + direction1[1] * 1.5]
    extension_point2 = [point2[0] + direction2[0] * 1.5, point2[1] + direction2[1] * 1.5]

    # 绘制射线
    plt.plot([point1[0], extension_point1[0]], [point1[1], extension_point1[1]], 'r--')  # 使用红色虚线绘制一点到三点的射线
    plt.plot([point2[0], extension_point2[0]], [point2[1], extension_point2[1]], 'g--')  # 使用绿色虚线绘制二点到三点的射线

def plot_points_s(point1, point2, point3):
    plt.style.use('ggplot')
    # 创建图形和坐标轴
    fig, ax = plt.subplots()

    # 绘制射线
    plot_ray_s(point1, point2, point3)

    # 绘制三个点
    ax.plot(point1[0], point1[1], 'bo')  # 绘制一点，使用蓝色圆点
    ax.plot(point2[0], point2[1], 'bo')  # 绘制二点，使用蓝色圆点
    ax.plot(point3[0], point3[1], 'go')  # 绘制三点，使用蓝色圆点

    # 设置坐标轴范围
    #ax.set_xlim([min(point1[0], point2[0], point3[0]) - 10, max(point1[0], point2[0], point3[0]) + 10])
    #ax.set_ylim([min(point1[1], point2[1], point3[1]) - 10, max(point1[1], point2[1], point3[1]) + 10])

    # 显示图形
    plt.show()
