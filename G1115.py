# -*- coding: utf-8 -*-
from pyecharts import Geo

def formatter_for_tootip(params):
    return params.value[2]

def plotmap():
    geo = Geo("G1115班本科毕业去向", "Made by YJT", title_color="#fff",
              title_pos="center", width=1366,
              height=768, background_color="#404a59")

    with open("G1115.txt") as file:
        temp = file.readline().split("：")
        data = []
        while temp != [""]:
            data.append(tuple(temp))
            temp = file.readline().split("：")

    attr, value = geo.cast(data)

    geo.add("", attr, value, type="effectScatter", is_random=True, maptype='world',
            effect_scale=5, tooltip_formatter=formatter_for_tootip,
            label_formatter="{b}")
    geo.render("test.html")

plotmap()
