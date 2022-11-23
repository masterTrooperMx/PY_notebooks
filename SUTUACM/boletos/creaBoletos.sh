convert -size 1736x478 xc:white boleto_c.png
convert gfg_QR.png -resize 478x478 gfg_res_Qr.png
composite -geometry  +0+0 b_der.png boleto_c.png boleto_c.png
composite -geometry  +868+0 b_izq.png boleto_c.png boleto_c.png
composite -geometry  +1086+0 gfg_res_Qr.png boleto_c.png boleto_c.png

