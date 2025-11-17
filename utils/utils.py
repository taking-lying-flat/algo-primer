def canonical_shape_D4(
    shape: List[Tuple[int, int]],
) -> Tuple[Tuple[int, int], ...]:
    """
    输入：
        shape: List[(x, y)]，可以是相对坐标也可以是绝对坐标，只要都是整数即可。

    输出：
        该点集在「平移 + 旋转（0/90/180/270）+ 翻转」等价意义下的
        唯一标准表示（字典序最小的那个）。

    思路（D4 群）：
        - 用 (sx, sy) ∈ {(1,1),(1,-1),(-1,1),(-1,-1)} 做四种符号翻转
        - 用 swap ∈ {0,1} 控制是否交换 x,y
        - 这 8 种组合刚好覆盖 D4 的 8 个元素
        - 每种变换后都做一次平移归一化（左上对齐到 (0,0)），再排序成 tuple
        - 8 个结果里取字典序最小者返回
    """
    cand = []

    for sx, sy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        for swap in (0, 1):
            tmp = []
            for x, y in shape:
                # ① 符号翻转
                px, py = x * sx, y * sy
                # ② 是否交换 x / y
                if swap:
                    px, py = py, px
                tmp.append((px, py))

            # ③ 平移归一化：左上角对齐到 (0,0)
            minx = min(px for px, _ in tmp)
            miny = min(py for _, py in tmp)
            norm = tuple(sorted((px - minx, py - miny) for px, py in tmp))

            cand.append(norm)

    # ④ 8 个候选表示里取字典序最小的作为 canonical 形状
    return min(cand)
