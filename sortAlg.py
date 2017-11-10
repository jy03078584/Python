#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Xiang mingzhe


# bubbleSort
def bubble(data):
    length = len(data)
    for i in range(length - 1):
        flag = True
        for j in range(length - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag = False
        if flag:
            break
    return data


# quickSort
# 快排本质是分治 对数组以标志位为中点位 大于/小于标志位的元素分居标志位左右两端
# 以下quick虽然也是借助快排分治的思想 但并非正统的快排 因为借助了python列表的slice特性 实质是切片后重组的列表并非原来的列表
def quickBySlice1(data):
    length = len(data)
    if length <= 1:
        return data
    flagData = data[0]
    leftIndex = 0
    rightIndex = length - 1
    while leftIndex < rightIndex:
        while rightIndex > leftIndex and data[rightIndex] >= flagData:
            rightIndex -= 1
        data[leftIndex] = data[rightIndex]

        while rightIndex > leftIndex and data[leftIndex] <= flagData:
            leftIndex += 1
        data[rightIndex] = data[leftIndex]
    # 标志位重置
    data[leftIndex] = flagData

    # 递归拼接子列表
    leftData = quickBySlice1(data[:leftIndex + 1])
    rightData = quickBySlice1(data[leftIndex + 1:])
    return leftData + rightData


# 依然是借助slice 但凭借python列表推导特性 代码更加简洁
# 参考：tobe https://github.com/tobegit3hub
def quickBySlice2(data):
    if len(data) <= 1:
        return data
    # 标志位
    flagData = data[0]
    return quickBySlice2([x for x in data[1:] if x <= flagData]) + [flagData] + quickBySlice2([x for x in data[1:] if x > flagData])


if __name__ == '__main__':
    arrData = [1, 22, 15, 16, 21, 33, 3, 17, 5, 12, 19, 223, 30, 44, 33, 44]
    print(quickBySlice2(arrData))
    print(quickBySlice1(arrData))
