# -*- coding: utf-8 -*-
from pyecharts import Geo

def formatter_for_tooltip(params):
    return params.value[2]

def plotmap():
    geo = Geo("湖南省地质中学G1115班同学本科毕业去向（持续更新）",
              "Made by YJT, Module provided by pyecharts",
              title_color="#fff",
              title_pos="center",
              width=1366,
              height=768,
              page_title ='湖南省地质中学G1115班同学本科毕业去向',
              background_color="#404a59")

    with open("G1115.txt") as file:
        temp = file.readline().split("：")
        data = []
        while temp != [""]:
            data.append(tuple(temp))
            temp = file.readline().split("：")

    attr, value = geo.cast(data)

    geo.add("", attr, value,
            type="effectScatter",
            is_random=False,
            maptype='world',
            effect_scale=5,
            tooltip_formatter=formatter_for_tooltip,
            symbol_size=10,
            #geo_normal_color="#F0F8FF",
            #geo_emphasis_color="#4169E1",
            label_formatter="{b}",
            label_text_size=15,
            label_emphasis_textsize=15,
            label_color=['#FFFFFF']*len(attr),
            label_emphasis_textcolor='#FFFFFF',
            #tooltip_tragger_on='click',
            tooltip_font_size=15,
            tooltip_background_color="rgba(50,50,50,0.3)",)

    geo.render("G1115.html")

plotmap()
