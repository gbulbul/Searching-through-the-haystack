class CommonMotif:
      def FindCommonMotif(rosalind1, rosalind2):
         if len(rosalind1)<=len(rosalind2):
             list1 = list(rosalind1)
             list2 = list(rosalind2)
         else:
              list1=list(rosalind2)
              list2=list(rosalind1)
              rosalind2=rosalind1
         common_motif = []
         output = ""
         length = 0
         for i in range(0, len(list1)):
              if list1[i] in list2:
                 common_motif.append(list1[i])
                 for j in range(i +1, len(list1)):
                     if ''.join(list1[i:j]) in rosalind2:
                        common_motif.append(''.join(list1[i:j]))    
                        for k in range(j+1, len(list1)):             
                            if list1[j:k] in list2:
                                common_motif.append(list1[j:k])                        
                                for m in range(k+1, len(list1)):
                                    if ''.join(list1[k:m]) in rosalind2:
                                       common_motif.append(''.join(list1[k:m]))
         for string in common_motif:
                if length < len(list(string)):
                   length = len(list(string))
                   output = string
         return output
if __name__=="__main__":
    d={}
    d['Rosalind1']='GATTACA'
    d['Rosalind2']='TAGACCA'
    d['Rosalind3']='ATACA'
    values_list=list(d.values())
    pairs=[(a, b) for idx, a in enumerate(values_list) for b in values_list[idx + 1:]]
    print(pairs)
    import pandas as pd 
    d_pair_to_common={}
    for pair in pairs:
        for i in range(0, len(list(pair[0]))-2):
            d_pair_to_common[pair]= ''.join(CommonMotif.FindCommonMotif(pair[0].replace(pair[0][:i],''),pair[1]))
            #print(d_pair_to_common)
            df = pd.DataFrame.from_dict(d_pair_to_common,orient='index')
            #print(df)
            if len(df.index)==3:
               arr = df[0].to_numpy()
              
               if (arr[0] == arr).all()==True:
                   print((arr[0]))
        
