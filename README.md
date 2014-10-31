MIDIConsoleOut
======================
MIDIConsoleOutはMIDI::Message型のデータをコンソール上に表示する[RT-Component][rtm]です．  
MIDI::Messageについては[こちら][idl]をごらんください．

[rtm]:http://www.openrtm.org/openrtm/ja
[idl]: https://github.com/HiroakiMatsuda/MIDIDataType

動作確認環境
------
Python:  
2.6.6  

OS:  
Windows 8/8.1 64bit / 32bit  

ファイル構成
------
MIDIParser  
│― idl   
│― MIDI  
│― MIDI_POA  
│― MIDIDataType_idl.py  
│― MIDIConsoleOut.conf  
│― MIDIConsoleOut.py  

* MIDI, MIDI_POA, MIDIDataType.py  
独自データ型 MIDIDataTypeに関するファイルです．  
 
* MIDIConsoleOut.conf  
受け取ったMIDIメッセージの表示モードをコンフィグレーションを使用して指定します．    

* MIDIConsoleOut.py  
MIDIConsoleOut RTC本体です．  

＊ 本RTCにおいてユーザーが操作すると想定しているファイルのみ説明しています．  

RTCの構成
------  
<img src="https://farm6.staticflickr.com/5604/15666637945_6168d9bcac.jpg" width="400px" />    
データポートは1つあり、以下のようになっています  
  
* midi\_in port :InPort  
データ型; MIDI::MIDIMessage  
MIDIメッセージを受け取り，受け取ったデータをコンソール上に表示します．  

* コンフィグレーション  
  ```mode```  
 MIDIメッセージの表示方法を指定します．  
 ```configuration.active_config: <mode number>```  
 表示方法は以下の様なモードから選択することができます．  
 ```0```:  
 受け取ったMIDI::MIDIMessage型のデータ構造をそのまま表示します．  
 このモードではデータは見づらいですが，全てのデータを見ることができます．  
 ```1```:   
 受け取ったMIDI::MIDIMessage型のイベントを調べ，Note OnとNote Offの場合のみその情報を表示します．  
 このモードではMIDIデータの大半を占めるNote OnとNote Offを見ることができます．  
 ```2```:  
 受け取ったMIDI::MIDIMessage型のイベント名を表示します．  
 このモードではイベント名だしか表示されませんが，その分データ量は減るので可読性は向上します．   
 

 コンフィグレーションはonStartUpで読み込みます．  
 モードを変更する場合は，一度MIDIConsoleOutを終了し，コンフィグレーション変更後に再度実行して下さい．


使い方：　MIDIParserを使用してテストする
------
###1. MIDIParserを入手する###
[MIDIParser][parser]はMIDIファイルを解析し，MIDI::MIDIMessage型のデータを曲のタイミングに合わせて出力するRTCです．  
[こちら][parser]よりDLしてください．

[parser]:https://github.com/HiroakiMatsuda/MIDIParser  


###2. 解析するMIDIファイルを設定する###
MIDIParser RTCに解析させるMIDIファイルを設定します．  

MIDIParser.confをテキストエディタなどで開きます．  
以下のようにコンフィグレーションが設定されていると思います．  

```conf.mode0.midi_file: ./midifile/simpletest.mid ```     

以下のように，mode numberとfile nameを設定することで複数MIDIファイルを登録することができます．  
＊MIDIファイルはmidifileフォルダ内に配置することを前提としています．  

```conf.mode<mode number>.midi_file: ./midifile/<file name>.mid ```     
 
###3. MIDIConsoleOutの表示モードを設定する###
MIDIConsoleOutでは受け取ったMIDIメッセージの表示方法を変更することができます．  

MIDIConsoleOut.confをテクストエディタなどで開きます．
以下のようにmode0がアクティブコンフィグレーションに設定されていると思います．  

```configuration.active_config: mode0```   

このmodeをmode0, mode1, mode2から選択することで表示方法を変えることができます．  
今回は，mode1を使用します．  
アクティブコンフィグレーションを以下のようにmode1に変更してください．  

```configuration.active_config: mode1```  
  
###4. MIDIメセージを受け取る###
MIDIParser RTCとMIDIConsoleOut RTCを実行してください．  
各RTCが起動したらMIDIParser RTCのmidi\_outポートとMIDIConsoleOut RTCのmidi\_inポートを接続します．  
各ポートを接続したらMIDIParser RTCをActivateします．  
すると，MIDIConsoleOut RTCのコンソール上に以下のようなメッセージが表示されると思います． 

<img src="https://farm8.staticflickr.com/7525/15480659597_7b957a5788.jpg" width="400px" />   

MIDIConsoleOut RTCのmode1ではNote OffとNote Onのメッセージ内容が表示されます．  
      
以上が本RTCの使い方となります  

ライセンス
----------
Copyright &copy; 2014 Hiroaki Matsuda  
Licensed under the [Apache License, Version 2.0][Apache]  
Distributed under the [MIT License][mit].  
Dual licensed under the [MIT license][MIT] and [GPL license][GPL].  
 
[Apache]: http://www.apache.org/licenses/LICENSE-2.0
[MIT]: http://www.opensource.org/licenses/mit-license.php
[GPL]: http://www.gnu.org/licenses/gpl.html