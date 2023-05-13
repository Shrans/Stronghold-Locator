import numpy as np
import webbrowser
import sys


# 点斜式交点法计算模块
def Calculate():
    active_1 = True
    active_2 = True
    player_1 = None
    player_2 = None
    command_1 = None
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
    active_back = True
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
def Estimate():
    active_1 = True
    player_1 = None
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
    x = float(player_1[0])
    z = float(player_1[2])
    theta = float(player_1[3])
    k = -np.tan(np.deg2rad(float(player_1[3])))
    # 该算法所用公式通过 微软数学 获得:https://mathsolver.microsoft.com/zh/solve-problem/@1038wxzim?ref=r
    delta = np.sqrt((1728 ** 2) - ((z * k) ** 2) + ((1728 ** 2) * (k ** 2)) + (2 * x * z * k) - (x ** 2))
    divisor = (k ** 2) + 1
    z_position_1 = ((z * k * k) - delta - (x * k)) / divisor
    z_position_2 = ((z * k * k) + delta - (x * k)) / divisor
    x_position_1 = (-k * delta - (z * k) + x) / divisor
    x_position_2 = (k * delta - (z * k) + x) / divisor
    """
    由于使用F3+C获得的角度是玩家累计旋转的角度之和，虽然对点斜式交点法影响不大，
    但不能直接用于判断点斜式估算法中朝向正确的一项坐标，因此需要进行转换
    """
    while theta > 180:
        theta -= 360
    while theta < -180:
        theta += 360
    # 通过玩家视角进行坐标的取舍，并输出结果
    if 0 < theta < 90:
        if x_position_1 < x and z_position_1 > z:
            print('★估算坐标：x=' + str(round(x_position_1)) + ',z=' + str(round(z_position_1)) +
                  '\n★传送指令：/tp ' + str(round(x_position_1)) + ' 100 ' + str(round(z_position_1)) +
                  ' (y轴坐标可适当修改)\n')
        elif x_position_2 < x and z_position_2 > z:
            print('★估算坐标：x=' + str(round(x_position_2)) + ',z=' + str(round(z_position_2)) +
                  '\n★传送指令：/tp ' + str(round(x_position_2)) + ' 100 ' + str(round(z_position_2)) +
                  ' (y轴坐标可适当修改)\n')
    elif 90 < theta < 180:
        if x_position_1 < x and z_position_1 < z:
            print('★估算坐标：x=' + str(round(x_position_1)) + ',z=' + str(round(z_position_1)) +
                  '\n★传送指令：/tp ' + str(round(x_position_1)) + ' 100 ' + str(round(z_position_1)) +
                  ' (y轴坐标可适当修改)\n')
        elif x_position_2 < x and z_position_2 < z:
            print('★估算坐标：x=' + str(round(x_position_2)) + ',z=' + str(round(z_position_2)) +
                  '\n★传送指令：/tp ' + str(round(x_position_2)) + ' 100 ' + str(round(z_position_2)) +
                  ' (y轴坐标可适当修改)\n')
    elif -90 < theta < 0:
        if x_position_1 > x and z_position_1 > z:
            print('★估算坐标：x=' + str(round(x_position_1)) + ',z=' + str(round(z_position_1)) +
                  '\n★传送指令：/tp ' + str(round(x_position_1)) + ' 100 ' + str(round(z_position_1)) +
                  ' (y轴坐标可适当修改)\n')
        elif x_position_2 > x and z_position_2 > z:
            print('★估算坐标：x=' + str(round(x_position_2)) + ',z=' + str(round(z_position_2)) +
                  '\n★传送指令：/tp ' + str(round(x_position_2)) + ' 100 ' + str(round(z_position_2)) +
                  ' (y轴坐标可适当修改)\n')
    elif -180 < theta < -90:
        if x_position_1 > x and z_position_1 < z:
            print('★估算坐标：x=' + str(round(x_position_1)) + ',z=' + str(round(z_position_1)) +
                  '\n★传送指令：/tp ' + str(round(x_position_1)) + ' 100 ' + str(round(z_position_1)) +
                  ' (y轴坐标可适当修改)\n')
        elif x_position_2 > x and z_position_2 < z:
            print('★估算坐标：x=' + str(round(x_position_2)) + ',z=' + str(round(z_position_2)) +
                  '\n★传送指令：/tp ' + str(round(x_position_2)) + ' 100 ' + str(round(z_position_2)) +
                  ' (y轴坐标可适当修改)\n')
    else:
        print('▲暂不支持对朝向角度为90°时的特殊情况进行估算，请更换地点重新测量，或使用点斜式交点法进行计算\n')
    active_back = True
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


# 操作指南模块
def Help():
    print("●使用方法：\n①先在游戏中定位到末影之眼的方向\n②按下F3+C复制当前玩家位置信息\n"
          "③将玩家位置信息粘贴到指定的输入框中\n④获取结果坐标\n▲注意：点斜式估算法暂不支持对朝向角度为90°时的特殊情况进行估算，"
          "但可以使用点斜式交点法计算\n")
    Menu()


# 主菜单模块
def Menu():
    active = True
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
