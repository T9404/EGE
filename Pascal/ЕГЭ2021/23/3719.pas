function f(start, endn:integer):integer;
begin
  if start = endn then f:=1
  else if start > endn then f:=0
  else f:=f(start + 2, endn) + f(start + 3, endn) 
            + f(start * 4, endn)
end;

begin
  Write('Ответ: ', f(1,16))
end.