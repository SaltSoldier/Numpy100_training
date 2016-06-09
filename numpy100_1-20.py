# -*- coding: utf-8 -*-
"""
numpy100_training 1~20
Spyder Editor

This is a temporary script file.
"""
#1 numpyのインポート
print("No.1 numpyのインポート")
import numpy as np
print("\n")

#2 numpyのバージョンおよび設定の出力
print("No.2 numpyのバージョンおよび設定の出力")
print(np.__version__)
np.show_config()
print("\n")

#3 サイズ10の零ベクトルの出力
print("No.3 サイズ10の零ベクトルの出力")
Z = np.zeros(10)
print(Z)
print("\n")

#4 何がしたいの？
#print("No.4 サイズ10の零ベクトルを作成，5つ目に1を代入")
#python -c "import numpy; numpy.info(numpy.add)"
#print("\n")

#5 サイズ10の零ベクトルを作成，5つ目に1を代入
print("No.5 サイズ10の零ベクトルを作成，5つ目に1を代入")
Z = np.zeros(10)
Z[4] = 1
print(Z)
print("\n")

#6 10～49の値を入れたベクトルの作成
print("No.6 10～49の値を入れたベクトルの作成")
Z = np.arange(10,50)
print(Z)
print("\n")

#7 0から49までのベクトルを作成し，それを逆順にする
print("No.7 49までのベクトルを作成し，それを逆順にする")
Z = np.arange(50)
Z = Z[::-1]
print(Z)
print("\n")

#8 9までのベクトルを作成し，それを3*3の行列にする
print("No.8 9までのベクトルを作成し，それを3*3の行列にする")
Z = np.arange(9).reshape(3,3)
print(Z)
print("\n")

#9 非0要素のインデックス配列を返す
print("No.9 非0要素のインデックス配列を返す")
nz = np.nonzero([1,2,0,0,4,0])
print(nz)
print("\n")

#10 3*3の単位行列の出力
print("No.10 3*3の単位行列の出力")
Z = np.eye(3)
print(Z)
print("\n")

#11 ランダムな値を持つ3*3*3の行列を出力
print("No.11 ランダムな値を持つ3*3*3の行列を出力")
Z =np.random.random((3,3,3))
print(Z)
print("\n")

#12 ランダムな10*10のベクトルを作成して，そのうちの最小値と最大値を出力
print("No.12 ランダムな10*10のベクトルを作成して，そのうちの最小値と最大値を出力")
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)
print("\n")

#13 サイズ30のランダムなベクトルを作成し，平均値をみつける
print("No.13 サイズ30のランダムなベクトルを作成し，平均値をみつける")
Z = np.random.random(30)
m = Z.mean()
print(m)
print("\n")

#14 値が全部1の10*10の行列を作成，そして行列の内側の値だけ0に置き換える
print("No.14 値が全部1の10*10の行列を作成，そして行列の内側の値だけ0に置き換える")
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)
print("\n")

#15 以下の式の結果は?
print("No.15 以下の式の結果は?")
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
0.3 == 3 *0.1
print("\n")

#16 対角のひとつしたの部分に1,2,3,4を順に入れた5*5の行列を作成
print("No.16 対角のひとつしたの部分に1,2,3,4を順に入れた5*5の行列を作成")
Z = np.diag(1+np.arange(4),k=-1)
print(Z)
print("\n")

#17 8*8の市松模様の行列を作成
print("No.17 8*8の市松模様の行列を作成")
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)
print("\n")

#18 6*7*8の行列から100番目の要素を取り出してくる(8*7の行列が6個)
print("No.186*7*8の行列から100番目の要素を取り出してくる(8*7の行列が6個)")
print(np.unravel_index(100,(6,7,8)))
print(Z)
print("\n")

#19 [(0,1),(1,0)]の行列を4*4回生成
print("No.19 [(0,1),(1,0)]の行列を4*4回生成")
Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(Z)
print("\n")

# 5*5のランダムな行列を正規化
print("No.20 5*5のランダムな行列を正規化")
Z = np.random.random((5,5))
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)
print("\n")
