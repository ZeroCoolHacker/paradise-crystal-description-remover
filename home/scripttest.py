from bs4 import BeautifulSoup



text = """
<div class="text-section" style="">
<div class="panel-body" style="">
<div align="left" style="">
<font size="3" style="font-size: 17.5px;"><span style="font-weight: 700;">DESCRIPTION: </span></font><span style='color: rgb(51, 51, 51); font-family: "Helvetica neue", Helvetica, Verdana, sans-serif;'><font size="3">1980s vintage Dartington Anita Harris “Palm” design crystal bowls</font></span>
</div>
<div align="left" style="font-size: 14pt;"><font size="3"><b><br></b></font></div>
<div align="left" style="font-size: 14pt;"><font size="3"><b>MARKING: Unm</b>arked / Unsigned on the base. Sticker on it.</font></div>
<div align="left" style="font-size: 17.5px;"><span style="font-weight: 700; font-size: medium;"><br></span></div>
<div align="left" style="font-size: 17.5px;">
<span style="font-weight: 700; font-size: medium;">CONDITION</span><span style="font-size: medium;">: Excellent condition. There is no chips and cracks.</span>
</div>
<div align="left" style="font-size: 17.5px;"><span style="font-weight: 700; font-size: medium;"><br></span></div>
<div align="left" style="font-size: 17.5px;">
<span style="font-weight: 700; font-size: medium;">DIMENSIONS: </span><span style="font-size: medium;">5</span><span style="font-size: medium;"> 1/8</span><span style="font-size: medium;">"</span><span style="font-size: medium;">(13</span><span style="font-size: medium;"> cm) tall one side and other side is 2"(5.2 cm), Diameter is top rim 12 1/2"(31.5 cm)</span>
</div>
<div align="left" style="font-size: 17.5px;"><span style="font-size: medium;"><br></span></div>
<div align="left" style="font-size: 17.5px;"><span style="font-size: medium;"><b>WEIGHT: </b>1.3 kg each.</span></div>
<div align="left" style="font-size: 17.5px;"><span style="font-size: medium;"><b><br></b></span></div>
<div align="left" style="font-size: 17.5px;"><span style="font-size: 14pt;">**Please check out our updated eBay shop by clicking on the link above**</span></div>
<!--Decription Body-->
</div>
</div>"""


to_remove = r'<div align="left" style="font-size: 17.5px;"><span style="font-size: 14pt;">**Please check out our updated eBay shop by clicking on the link above**</span></div>'

new = text.replace(to_remove, "")
print(new)

soup = BeautifulSoup(text, 'html.parser')






