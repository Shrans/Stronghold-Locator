import numpy as np


# 点斜式估算法输出模块
def Estimate_Print(x, z):
    return (str(round(x)),str(round(z)))
    

# 点斜式交点法计算模块
def Calculate(xyt_1=None,xyt_2=None,active_1=True, active_2=True, player_1=None, active_back=True, player_2=None, command_1=None):
    while active_1:
        command_1 = str(xyt_1)
        if '/execute in minecraft:overworld run tp @s' in command_1:
            player_1 = command_1[command_1.index('@s') + 3:].split()
            # noinspection PyBroadException
            try:
                for add in range(0, 5):
                    test = float(player_1[add])
                    test += 1
            except Exception:
                return "▲请确保你正确使用了F3+C来获取玩家位置信息，且无任何修改"
            else:
                active_1 = False
        else:
            return "▲请输入正确的玩家位置信息"
    while active_2:
        command_2 = str(xyt_2)
        if '/execute in minecraft:overworld run tp @s' in command_2:
            if command_2 == command_1:
                return "▲请勿输入相同的的玩家位置信息"
            else:
                player_2 = command_2[command_2.index('@s') + 3:].split()
                # noinspection PyBroadException
                try:
                    for add in range(0, 5):
                        test = float(player_1[add])
                        test += 1
                except Exception:
                    return "▲请确保你正确使用了F3+C来获取玩家位置信息，且无任何修改"
                else:
                    active_2 = False
        else:
            return "▲请输入正确的玩家位置信息"
    # 处理数据
    x1 = float(player_1[0])
    z1 = float(player_1[2])
    k1 = -np.tan(np.deg2rad(float(player_1[3])))
    x2 = float(player_2[0])
    z2 = float(player_2[2])
    k2 = -np.tan(np.deg2rad(float(player_2[3])))
    if k1 == k2:
        return "▲两点的朝向平行无交点，意味着末影之眼指向不同要塞，无解" 
    # 该算法所用公式通过 微软数学 获得:https://mathsolver.microsoft.com/zh/solve-problem/@1cb6uy4rp?ref=r
    z_position = -(((z1 * k1) - (z2 * k2) - x1 + x2) / (k2 - k1))
    x_position = -(((z1 * k1 * k2) - (z2 * k1 * k2) - (x1 * k2) + (x2 * k1)) / (k2 - k1))
    out_x = str(round(x_position))
    out_z = str(round(z_position))
    return (out_x,out_z)



# 点斜式估算法计算模块
def Estimate(xyt_1=None,active_1=True, active_back=True, player_1=None):
    while active_1:
        command_1 = str(xyt_1)
        if '/execute in minecraft:overworld run tp @s' in command_1:
            player_1 = command_1[command_1.index('@s') + 3:].split()
            # noinspection PyBroadException
            try:
                for add in range(0, 5):
                    test = float(player_1[add])
                    test += 1
            except Exception:
                return "▲请确保你正确使用了F3+C来获取玩家位置信息，且无任何修改"
            else:
                active_1 = False
        else:
            return "▲请输入正确的玩家位置信息"
    # 处理数据
    x = float(player_1[0])
    z = float(player_1[2])
    theta = float(player_1[3])
    k = -np.tan(np.deg2rad(float(player_1[3])))
    distance = np.sqrt((x ** 2) + (z ** 2))
    # 判断玩家是否处在主世界原点1728格以内的范围中
    if distance < 1728:
        # 该算法所用公式通过 微软数学 获得:https://mathsolver.microsoft.com/zh/solve-problem/@1038wxzim?ref=r
        delta = np.sqrt(abs((1728 ** 2) - ((z * k) ** 2) + ((1728 ** 2) * (k ** 2)) + (2 * x * z * k) - (x ** 2)))
        divisor = (k ** 2) + 1
        z_position_1 = ((z * k * k) - delta - (x * k)) / divisor
        z_position_2 = ((z * k * k) + delta - (x * k)) / divisor
        x_position_1 = (-k * delta - (z * k) + x) / divisor
        x_position_2 = (k * delta - (z * k) + x) / divisor
        """
        由于使用F3+C获得的角度是玩家累计旋转的角度之和，虽然对点斜式交点法影响不大，但不能直接用于判断点斜式估算法中朝向正确的一项坐标。
        因此需要先把角度转换到-180°到180°之间，也就是转化为F3中显示的朝向角度
        """
        while theta > 180:
            theta -= 360
        while theta < -180:
            theta += 360
        # 通过玩家视角进行坐标的取舍，并输出结果
        if 0 < theta < 90:
            if x_position_1 < x and z_position_1 > z:
                return Estimate_Print(x_position_1, z_position_1)
            else:
                return Estimate_Print(x_position_2, z_position_2)
        elif 90 < theta < 180:
            if x_position_1 < x and z_position_1 < z:
                return Estimate_Print(x_position_1, z_position_1)
            else:
                return Estimate_Print(x_position_2, z_position_2)
        elif -90 < theta < 0:
            if x_position_1 > x and z_position_1 > z:
                return Estimate_Print(x_position_1, z_position_1)
            else:
                return Estimate_Print(x_position_2, z_position_2)
        elif -180 < theta < -90:
            if x_position_1 > x and z_position_1 < z:
                return Estimate_Print(x_position_1, z_position_1)
            else:
                return Estimate_Print(x_position_2, z_position_2)
        elif abs(theta) == 90:
            if x_position_1 > x > x_position_2:
                return Estimate_Print(x_position_1, z_position_1)
            else:
                Estimate_Print(x_position_2, z_position_2)
    else:
        return '▲请在距离主世界原点1728格以内的范围中进行估算\n'

def CalculateT(xyt1=None,xyt2=None,xyt3=None,xzmax=32):
    lot = [
        Calculate(xyt1,xyt2),
        Calculate(xyt1,xyt3),
        Calculate(xyt2,xyt3)
    ]

    if type(lot[0]) == str:
        return lot[0]
    elif type(lot[1]) == str:
        return lot[1]
    elif type(lot[2]) == str:
        return lot[2]
    
    xx=max(int(lot[0][0]),int(lot[1][0]),int(lot[2][0]))-min(int(lot[0][0]),int(lot[1][0]),int(lot[2][0]))
    zz=max(int(lot[0][1]),int(lot[1][1]),int(lot[2][1]))-min(int(lot[0][1]),int(lot[1][1]),int(lot[2][1]))

    if xx > xzmax or zz > xzmax:
        return "▲误差过大，请修正数值"
    
    return (str(int(sum((int(lot[0][0]),int(lot[1][0]),int(lot[2][0]))) / 3)), str(int(sum((int(lot[0][1]),int(lot[1][1]),int(lot[2][1]))) / 3)))
