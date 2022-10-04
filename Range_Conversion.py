def Range_Conversion(*args: object) -> object:
    # args[0] = x1
    # args[1] = x2
    # args[2] = y1
    # args[3] = y2
    # args[4] = z1
    # args[5] = z2
    # args[6] = input value
    # args[7] = selection  0 = find x , 1 = find y , 2 = find z

    if args[7] == 0.0:
        # Given y , find x and z

        x = (args[6] - args[2]) / (args[3] - args[2]) * (args[1] - args[0]) + args[0]
        z = (args[6] - args[2]) / (args[3] - args[2]) * (args[5] - args[4]) + args[4]
        return x, args[6], z

    elif args[7] == 1.0:
        # Given x , find y and z

        y = (args[6] - args[0]) / (args[1] - args[0]) * (args[3] - args[2]) + args[2]
        z = (y - args[2]) / (args[3] - args[2]) * (args[5] - args[4]) + args[4]
        return args[6], y, z

    elif args[7] == 2.0:
        # Given z , find x and y

        x = (args[6] - args[4]) / (args[5] - args[4]) * (args[1] - args[0]) + args[0]
        y = (args[6] - args[4]) / (args[5] - args[4]) * (args[3] - args[2]) + args[2]
        return x, y, args[6]
