function f(start, endn:integer):integer;
begin
  if start = endn then f:=1
  else if start < endn then f:=0
  else if (start mod 3) <> 0 then
    f:=f(start - 2, endn) + f((start div 3)*3, endn)
  else if (start mod 3) = 0 then
    f:=f(start - 2, endn)
end;

begin
  Write('Ответ: ', f(23, 3))
end.