# ロボットシステム学2020　課題2
___

## 実験目的・概要
ROS１を用いて電卓プログラムを作成しました。

## 環境
___
  ubuntu 18.04 LTS
  Ros Melodic
  Pythin 2.7.17
  
## 環境構築
____
## ・ROS
  下記スクリプトを利用し、ROS環境を構築しました。
  　https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu18.04_server.git
  
## ・ワークスペース
   下記資料を参考にワークスペースを作成しました。
    https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md
  　
## 実行方法
____
Ubuntuの端末を３つ立ち上げます。

初めに1つ目で　`$roscore` を実行してrosocoreを立ち上げます。

・Publisher
  別の端末で
  `$rosrun calc scan.py`
  を実行
  式を入力します。
・Subscriber
  また別の端末で
  `$rosrun calc calc.py`
  を実行
  計算結果が出力されます。
  
## 参考
  Prof. Ryuichi Ueda
    robosys2020 - ros
    [ros_setup_scripts_Ubuntu18.04_desktop](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu18.04_server.git)
    
## ライセンス
    ROS - [BSD 3-Clause License](https://github.com/YuiTsubaki/calc/blob/main/LICENSE)
  
  
