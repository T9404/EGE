function f(start, endn:integer):integer;
begin
  var k := Trunc(Power(2, Trunc(Log2(start))));
  if start = endn then f:=1
  else if start < endn then f:=0
  else if k = start then f:=f(start - 1, endn)
  else if k <> start then f:=f(start - 1, endn) + 
                                f(k, endn)
end;

begin
  Write('Ответ: ', f(12, 4))
end.