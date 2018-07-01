 #!/usr/bin/env python  
 # Server  
 import sys  
 import socket  
 import os  

 host = '';  
 SIZE = 512;  

 try :  
     port = sys.argv[1];  

 except :  
     port = 31337;  
 
 try :  
     sockfd = socket.socket(socket.AF_INET , socket.SOCK_STREAM);  

 except socket.error , e :  

     print "Error in creating socket : ",e ;  
     sys.exit(1);   

 sockfd.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1);  

 try :  
     sockfd.bind((host,port));  

 except socket.error , e :        
     print "Error in Binding : ",e; 
     sys.exit(1);  
 
 print("\n\n======================================================"); 
 print("-------- Server Listening on Port %d --------------" % port);  
 print("======================================================\n\n"); 
 
 try :  
     while 1 : # listen for connections  
         sockfd.listen(1);  
             clientsock , clientaddr = sockfd.accept();  
         print("\n\nGot Connection from " + str(clientaddr));  
         while 1 :  
             try :  
                 cmd = clientsock.recv(SIZE);  
             except :  
                 break;  
             pipe = os.popen(cmd);  
             rawOutput = pipe.readlines();  
 
             print(cmd);  
           
             if cmd == 'g2g': # close the connection and move on for others  
                 print("\n-----------Connection Closed----------------");  
                 clientsock.shutdown();  
                 break;  
                        try :  
                 output = "";  
                 # Parse the output from list to string  
                 for data in rawOutput :  
                      output = output+data;  
                   
                 clientsock.send("Command Output :- \n"+output+"\r\n");  
               
             except socket.error , e :  
                   
                 print("\n-----------Connection Closed--------");  
                 clientsock.close();  
                 break;  
  except  KeyboardInterrupt :  
 

     print("\n\n>>>> Server Terminated <<<<<\n");  
     print("==========================================================="); 
     print("\tThanks for using Simple-CMD");  
     print("\tEmail : lionaneesh@gmail.com");  
     print("============================================================");
 
 
