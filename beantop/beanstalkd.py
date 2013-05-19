
import yaml

class Beanstalkd:
    host = None
    port = None
    conn = None  
    def __init__(self,  conn,  host,  port):
        self.conn = conn       
        self.host = host
        self.port = port
     
    def connect(self):
        self.conn.open(self.host, self.port)
    
    def send(self, mess):
        self.conn.write(mess+"\r\n")
      
    def readline(self):
        return self.conn.read_until("\n")    
      
    def yaml_data_filtered(self, msg, fields_to_show):
        stats =  self.yaml_data(msg)
        ret_data = dict()
        for field in fields_to_show:
            ret_data[field] = stats[field]
        return ret_data
        
    def yaml_data(self, msg):
        self.send(msg)
        self.readline()      
        self.readline()
        stats =  yaml.load(self.conn.read_until("\r\n"))
        return stats
