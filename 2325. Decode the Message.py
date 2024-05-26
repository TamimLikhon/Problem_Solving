class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        a={}
        res=""
        aa="abcdefghijklmnopqrstuvwxyz"
        aa=list(aa)
        jj=""
        #print(aa)
        for i in range(len(key)):
            if(key[i]!=' ' and key[i] not in jj):
                  jj+=key[i]         
        jj=(list(jj))
        for i,j in zip(jj,aa):
            a[i]=j
        for i in message:
            if(i!=" "):
                res+=a[i]
            else:
                res+=' '
        return res