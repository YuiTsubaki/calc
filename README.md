# ロボットシステム学2020　課題2
___

## 概要
ROS１を用いて電卓プログラムを作成しました。

## 動作環境
___
  ubuntu 18.04 LTS <br>
  Ros Melodic<br>
  Pythin 2.7.17<br>
  
## インストール方法
____
## ・ROS
  下記スクリプトを利用し、ROS環境を構築しました。<br>
  　https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu18.04_server.git<br>
  
## ・ワークスペース
   下記資料を参考にワークスペースを作成しました。<br>
    https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md<br>
  　
## 実行方法
____
Ubuntuの端末を３つ立ち上げます。<br>

初めに1つ目で　`$roscore` を実行してrosocoreを立ち上げます。<br>

 〇Publisher <br>
  別の端末で<br>
  `$rosrun calc scan.py`<br>
  を実行<br>
  式を入力します。<br>
〇Subscriber<br>
  また別の端末で<br>
  `$rosrun calc calc.py`<br>
  を実行<br>
  計算結果が出力されます。<br>
  
## 参考
  Prof. Ryuichi Ueda<br>
    robosys2020 - ros <br>
    [ros_setup_scripts_Ubuntu18.04_desktop](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu18.04_server.git)
    
## ライセンス
   [BSD 3-Clause License](https://github.com/YuiTsubaki/calc/blob/main/LICENSE)
  
 
