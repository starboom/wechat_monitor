# usage: python wechat_jarvis.py [-t msg] [-s]
#         -t msg: for test, run by your own environment with msg
#         -s: start jarvis now.
import itchat
import time, sys, getopt, json

#it.auto_login(enableCmdQR=2)

#r = itchat.search_chatrooms(name='issp')
#issp_xj_zone = r[0].UserName

def usage():
  print("usage: python wechat_jarvis.py [-t msg] [-s]")
  print("         -t msg: for test, run by your own environment with msg")
  print("         -s: start jarvis now.")
  sys.exit()

def send_to_filehelper(msg):
    send_msg = "[MESSAGE]%s\n[WHERE]%s" % (msg.get("msg", "nil"), msg.get("sendFrom", "nil"))
    itchat.send(send_msg, toUserName='filehelper')

def send_to_wechatroom(msg):
    if msg["SendTo"] is None:
      print("the json is not have snedTo key, may be lost, skip this warning.")
      sys.exit()
    print("send to wechat room todo")

# auto login WeChat 
def login_wechat(msg, test):
  itchat.auto_login(enableCmdQR=2, hotReload=True)
  if test == 1:
    send_to_filehelper(msg)
  else:
    send_to_wechatroom(msg)

def jarvis_test(attach):
  print("the attach msg is %s" % attach)
  msg_json = json.loads(attach)
  # try:
      
  # except:
  #     print("this attach is not json format.")
  #     usage()
  login_wechat(msg_json, 1)

def jarvis_start():
  print("start it ")

#start here
if __name__ == "__main__":
  # check usage
  try:
    opts, args = getopt.getopt(sys.argv[1:], "t:s")
    if len(opts):
        print(opts)
        for option, attach in opts:
          if option in ("-t"):
              print(attach)
              jarvis_test(attach)
          elif ooption in ("-s"):
              jarvis_start()
    else:
        usage()
  except getopt.GetoptError:
    usage()

  # analyze msg

  # msg format: simple json {"msg": "hello!", "sendFrom":"issp xj", "time":"123454322", "sendTo": "issp"}

  # send to WeChatRoom 

  # if test then send to fileHelper

  # keep running
  while 1:
    time.sleep(3)
  
