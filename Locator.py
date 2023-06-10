import numpy as np
import webbrowser
import sys


# 点斜式交点法计算模块
def Calculate(active_1=True, active_2=True, player_1=None, active_back=True, player_2=None, command_1=None):
    while active_1:
        command_1 = str(input("●请输入第一次定位点的玩家位置信息："))
        if '/execute in minecraft:overworld run tp @s' in command_1:
            player_1 = command_1[command_1.index('@s') + 3:].split()
            # noinspection PyBroadException
            try:
                for add in range(0, 5):
                    test = float(player_1[add])
                    test += 1
            except Exception:
                print("▲请确保你正确使用了F3+C来获取玩家位置信息，且无任何修改")
            else:
                active_1 = False
        else:
            print("▲请输入正确的玩家位置信息")
    while active_2:
        command_2 = str(input("●请输入第二次定位点的玩家位置信息："))
        if '/execute in minecraft:overworld run tp @s' in command_2:
            if command_2 == command_1:
                print("▲请勿输入相同的的玩家位置信息")
            else:
                player_2 = command_2[command_2.index('@s') + 3:].split()
                # noinspection PyBroadException
                try:
                    for add in range(0, 5):
                        test = float(player_1[add])
                        test += 1
                except Exception:
                    print("▲请确保你正确使用了F3+C来获取玩家位置信息，且无任何修改")
                else:
                    active_2 = False
        else:
            print("▲请输入正确的玩家位置信息")
    # 处理数据
    x1 = float(player_1[0])
    z1 = float(player_1[2])
    k1 = -np.tan(np.deg2rad(float(player_1[3])))
    x2 = float(player_2[0])
    z2 = float(player_2[2])
    k2 = -np.tan(np.deg2rad(float(player_2[3])))
    # 该算法所用公式通过 微软数学 获得:https://mathsolver.microsoft.com/zh/solve-problem/@1cb6uy4rp?ref=r
    z_position = -(((z1 * k1) - (z2 * k2) - x1 + x2) / (k2 - k1))
    x_position = -(((z1 * k1 * k2) - (z2 * k1 * k2) - (x1 * k2) + (x2 * k1)) / (k2 - k1))
    print('★预计坐标：x=' + str(round(x_position)) + ',z=' + str(round(z_position)) +
          '\n★传送指令：/tp ' + str(round(x_position)) + ' 100 ' + str(round(z_position)) + ' (y轴坐标可适当修改)\n')
    while active_back:
        cal_type = str(input("●请输入对应编号进行下一步操作操作：\nA.计算新坐标\nB.返回主菜单\nC.退出程序\n"))
        if cal_type == 'A':
            Calculate()
            active_back = False
        elif cal_type == 'B':
            Menu()
            active_back = False
        elif cal_type == 'C':
            sys.exit()
        else:
            print('▲未知指令，请重新输入')


# 点斜式估算法计算模块
def Estimate(active_1=True, active_back=True, player_1=None):
    while active_1:
        command_1 = str(input("●请输入定位点的玩家位置信息："))
        if '/execute in minecraft:overworld run tp @s' in command_1:
            player_1 = command_1[command_1.index('@s') + 3:].split()
            # noinspection PyBroadException
            try:
                for add in range(0, 5):
                    test = float(player_1[add])
                    test += 1
            except Exception:
                print("▲请确保你正确使用了F3+C来获取玩家位置信息，且无任何修改")
            else:
                active_1 = False
        else:
            print("▲请输入正确的玩家位置信息")
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
                Estimate_Print(x_position_1, z_position_1)
            else:
                Estimate_Print(x_position_2, z_position_2)
        elif 90 < theta < 180:
            if x_position_1 < x and z_position_1 < z:
                Estimate_Print(x_position_1, z_position_1)
            else:
                Estimate_Print(x_position_2, z_position_2)
        elif -90 < theta < 0:
            if x_position_1 > x and z_position_1 > z:
                Estimate_Print(x_position_1, z_position_1)
            else:
                Estimate_Print(x_position_2, z_position_2)
        elif -180 < theta < -90:
            if x_position_1 > x and z_position_1 < z:
                Estimate_Print(x_position_1, z_position_1)
            else:
                Estimate_Print(x_position_2, z_position_2)
        elif abs(theta) == 90:
            if x_position_1 > x > x_position_2:
                Estimate_Print(x_position_1, z_position_1)
            else:
                Estimate_Print(x_position_2, z_position_2)
    else:
        print('▲请在距离主世界原点1728格以内的范围中进行估算\n')
    while active_back:
        cal_type = str(input("●请输入对应编号进行下一步操作操作：\nA.计算新坐标\nB.返回主菜单\nC.退出程序\n"))
        if cal_type == 'A':
            Estimate()
            active_back = False
        elif cal_type == 'B':
            Menu()
            active_back = False
        elif cal_type == 'C':
            sys.exit()
        else:
            print('▲未知指令，请重新输入')


# 点斜式估算法输出模块
def Estimate_Print(x, z):
    print('★估算坐标：x=' + str(round(x)) + ',z=' + str(round(z)) +
          '\n★传送指令：/tp ' + str(round(x)) + ' 100 ' + str(round(z)) + ' (y轴坐标可适当修改)\n')


# 操作指南模块
def Help():
    print("●使用方法：\n"
          "①先在游戏中确定末影之眼的方向\n"
          "②按下F3+C复制当前玩家位置信息\n"
          "③将玩家位置信息粘贴到指定的输入框中\n"
          "④获取结果坐标\n"
          "▲注意：点斜式估算法暂不支持对超出距离主世界原点1728格的数据进行估算\n")
    Menu()


# 主菜单模块
def Menu(active=True):
    while active:
        cal_type = str(input(
            "●请输入对应编号进行下一步操作操作：\nA.点斜式交点法\nB.点斜式估算法\nC.操作指南\nD.关于/帮助/更新/GitHub页面\n"))
        if cal_type == 'A':
            Calculate()
            active = False
        elif cal_type == 'B':
            Estimate()
            active = False
        elif cal_type == 'C':
            Help()
            active = False
        elif cal_type == 'D':
            webbrowser.open('https://github.com/Shrans/Stronghold-Locator', new=0, autoraise=True)
        else:
            print('▲未知指令，请重新输入')


# 程序运行，进入主菜单模块
Menu()
