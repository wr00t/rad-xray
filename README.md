# rad-xray
xray+rad 批量主动扫描

## Usage: 

## 社区版用户

url 一行一个放 url.txt 中，和 rad 放同文件夹

xray 开启监听，

./xray webscan --listen 127.0.0.1:7777 --html-output report__datetime__.html

运行py

python3 rad+xray.py

注意：单个任务结束后会kill所有的chrome进程

## 高级版用户

url一行一个放 url.txt 中

advanced_xray_scanner.py 和 xray 和 rad 放同一文件夹，注意命名

运行py:

python3 advanced_xray_scanner.py -i url.txt


## etc
1. 开源的样本大部分可能已经无法免杀,需要自行修改

2. 我认为基础核心代码的开源能够帮助想学习的人
 
3. 本人从github大佬项目中学到了很多
 
4. 若用本人项目去进行：HW演练/红蓝对抗/APT/黑产/恶意行为/违法行为/割韭菜，等行为，本人概不负责，也与本人无关

5. 本人已不参与大小HW活动的攻击方了，若溯源到timwhite id与本人无关
