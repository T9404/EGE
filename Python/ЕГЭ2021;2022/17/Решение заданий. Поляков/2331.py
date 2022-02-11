a=[x for x in range(2495,7084) if (x%5!=0) and (x%9!=0) and (((x%16==10) and (x%256==26)) or ((x%16==15) and (x%256==31)))]
print(len(a),min(a))