import os

cmdNewTab = "osascript -e \'tell application \"Terminal\" to do script \"ssh -i ~/AWS/first.pem ec2-user@"

#Accesing the web server
os.system(cmdNewTab + "ec2-13-59-212-176.us-east-2.compute.amazonaws.com\"\'")

#Accessing kafka nodes
#Zookeeper
os.system(cmdNewTab + "ec2-18-216-182-18.us-east-2.compute.amazonaws.com \"\'")

#I need several command lines to operate correctly
#DataNode0
os.system(cmdNewTab + "ec2-13-59-190-223.us-east-2.compute.amazonaws.com \"\'")
#DataNode0
os.system(cmdNewTab + "ec2-13-59-190-223.us-east-2.compute.amazonaws.com \"\'")

#DataNode1
os.system(cmdNewTab + "ec2-18-217-106-184.us-east-2.compute.amazonaws.com \"\'")
#DataNode1
os.system(cmdNewTab + "ec2-18-217-106-184.us-east-2.compute.amazonaws.com \"\'")
